# 假设 loader_kwargs 是一个配置字典，用于设置加载器的参数
loader_kwargs = {
    "max_connections": 5,
    "timeout": 30
}
loader_kwargs.setdefault("autodetect_encoding", True)
print(loader_kwargs)


# try:  # 一种解题思路 
#     text_splitter = TextSplitter.from_tiktoken_encoder(
#         encoding_name=text_splitter_dict[splitter_name]["tokenizer_name_or_path"],
#         pipeline="zh_core_web_sm",
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )
# except:   # 上面走不通再走下面的解题思路
#     text_splitter = TextSplitter.from_tiktoken_encoder(
#         encoding_name=text_splitter_dict[splitter_name]["tokenizer_name_or_path"],
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )