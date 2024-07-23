'''
zip 使用示例
'''
# 假设的文件路径列表
sft_args_paths = [
    '/path/to/config1.json',
    '/path/to/config2.json',
    '/path/to/config3.json'
]

logging_paths = [
    '/path/to/logs1.log',
    '/path/to/logs2.log',
    '/path/to/logs3.log'
]

# 现在我们使用 zip 函数来同时迭代这两个列表
for sft_args_path, logging_path in zip(sft_args_paths, logging_paths):
    print(f"处理配置文件: {sft_args_path}")
    print(f"处理日志文件: {logging_path}")
    # 这里可以添加处理每个文件对的代码