'''
希望直接读取JSONL文件的最后一行而不需要逐行处理，可以使用以下方法：

读取整个文件到内存：这种方法适用于文件不是特别大的情况。
使用文件指针移动：适合大文件，通过移动文件指针到文件末尾，然后读取最后几行。
方法1：读取整个文件到内存
'''
import json

from rk_0007 import logging_file

# 读取整个文件到内存
with open(logging_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 获取最后一行
last_line = lines[-1].strip()

# 解析JSON
last_line_data = json.loads(last_line)

print(last_line_data['global_step'])