# if self.eval_steps != int(self.eval_steps):       条件检查 self.eval_steps 的当前值与将它转换成整数后的结果是否相等。
#                 raise ValueError(f"--eval_steps must be an integer if bigger than 1: {self.eval_steps}")          如果条件语句为 True，那么就意味着 self.eval_steps 不是一个整数，代码随后会抛出一个 ValueError 异常。
'''
except Exception as error:
            show_error = app.get_blocks().show_error or isinstance(error, Error)
            traceback.print_exc()
            raise Exception(str(error) if show_error else None) from error

这是什么意思'''