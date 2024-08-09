'''
try...except Execption:
await.. async

'''

class SessionState:
    def __init__(self, blocks: Blocks):
        self.blocks = blocks
        self._data = {}

    def __getitem__(self, key: int) -> Any:
        if key not in self._data:
            block = self.blocks.blocks[key]
            if getattr(block, "stateful", False):
                self._data[key] = deepcopy(getattr(block, "value", None))
            else:
                self._data[key] = None
        return self._data[key]

    def __setitem__(self, key: int, value: Any):
        self._data[key] = value

    def __contains__(self, key: int):
        return key in self._data


def restore_session_state(app: App, body: PredictBody):
    event_id = body.event_id
    session_hash = getattr(body, "session_hash", None)
    if session_hash is not None:
        session_state = app.state_holder[session_hash]
        # The should_reset set keeps track of the fn_indices
        # that have been cancelled. When a job is cancelled,
        # the /reset route will mark the jobs as having been reset.
        # That way if the cancel job finishes BEFORE the job being cancelled
        # the job being cancelled will not overwrite the state of the iterator.
        if event_id is None:
            iterator = None
        elif event_id in app.iterators_to_reset:
            iterator = None
            app.iterators_to_reset.remove(event_id)
        else:
            iterator = app.iterators.get(event_id)
    else:
        session_state = SessionState(app.get_blocks())
        iterator = None

    return session_state, iterator

async def call_process_api(
    app: App,
    body: PredictBody,
    gr_request: Union[Request, list[Request]],
    fn_index_inferred: int,
):
    session_state, iterator = restore_session_state(app=app, body=body)

    dependency = app.get_blocks().dependencies[fn_index_inferred]
    event_data = prepare_event_data(app.get_blocks(), body)
    event_id = body.event_id

    session_hash = getattr(body, "session_hash", None)
    inputs = body.data

    batch_in_single_out = not body.batched and dependency["batch"]
    if batch_in_single_out:
        inputs = [inputs]

    try:
        with utils.MatplotlibBackendMananger():
            output = await app.get_blocks().process_api(
                fn_index=fn_index_inferred,
                inputs=inputs,
                request=gr_request,
                state=session_state,
                iterator=iterator,
                session_hash=session_hash,
                event_id=event_id,
                event_data=event_data,
                in_event_listener=True,
            )
        iterator = output.pop("iterator", None)
        if event_id is not None:
            app.iterators[event_id] = iterator  # type: ignore
        if isinstance(output, Error):
            raise output
    except BaseException:
        iterator = app.iterators.get(event_id) if event_id is not None else None
        if iterator is not None:  # close off any streams that are still open
            run_id = id(iterator)
            pending_streams: dict[int, list] = (
                app.get_blocks().pending_streams[session_hash].get(run_id, {})
            )
            for stream in pending_streams.values():
                stream.append(None)
        raise

    if batch_in_single_out:
        output["data"] = output["data"][0]

    return output

    try:
        output = await route_utils.call_process_api(
            app=app,
            body=body,
            gr_request=gr_request,
            fn_index_inferred=fn_index_inferred,
        )
    except Exception as error:
        show_error = app.get_blocks().show_error or isinstance(error, Error)
        traceback.print_exc()
        raise Exception(str(error) if show_error else None) from error
