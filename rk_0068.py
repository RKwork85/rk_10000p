import os
from pathlib import Path

class FileHandler:
    def __init__(self, filename):
        self.filename = str(Path(filename).as_posix())  # 存储文件的完整路径
        self.ext = os.path.splitext(filename)[-1].lower()  # 存储文件的扩展名，转换为小写

# 示例使用
file_handler = FileHandler("/path/to/your/file/example.TXT")
print("Filename:", file_handler.filename)
print("Extension:", file_handler.ext)



from typing import List, Union, Tuple, Dict

# 假设 KnowledgeFile 是一个已经定义的类
class KnowledgeFile:
    def __init__(self, content):
        self.content = content

# 使用类型注解的变量
files: List[Union[KnowledgeFile, Tuple[str, str], Dict]] = []

# 添加不同类型的元素到列表
files.append(KnowledgeFile("这是一个KnowledgeFile对象"))
files.append(("example.txt", "/path/to/example.txt"))  # 元组形式
files.append({"filename": "example.txt", "path": "/path/to/example.txt"})  # 字典形式

# 打印列表查看元素
for file in files:
    print(file)


def validate_kb_name(knowledge_base_id: str) -> bool:
    # 检查是否包含预期外的字符或路径攻击关键字
    if "../" in knowledge_base_id:
        return False
    return True


# def hhh(knowledge_base_name):
#     if not validate_kb_name(knowledge_base_name):
#         return BaseResponse(code=403, msg="Don't attack me")