'''
这段代码定义了一个名为 KBService 的抽象基类（Abstract Base Class, ABC），它使用 Python 的 abc 模块。下面是对代码的逐行解释：

class KBService(ABC):：

定义了一个名为 KBService 的类，它继承自 ABC，这意味着 KBService 是一个抽象基类，不能被直接实例化，通常用于定义其他子类必须实现的接口。
__init__(self, knowledge_base_name: str, embed_model: str = EMBEDDING_MODEL)：

这是类的构造函数，用于初始化类的实例。
knowledge_base_name: str：一个参数，用于指定知识库的名称，类型为字符串。
embed_model: str = EMBEDDING_MODEL：一个带默认值的参数，用于指定嵌入模型的名称。如果调用构造函数时没有提供 embed_model，则使用 EMBEDDING_MODEL 常量的值。
self.kb_name = knowledge_base_name：

将传入的 knowledge_base_name 参数赋值给实例变量 kb_name。
self.kb_info = KB_INFO.get(knowledge_base_name, f"关于{knowledge_base_name}的知识库")：

从 KB_INFO 字典中获取与 knowledge_base_name 对应的信息，如果找不到，则使用默认信息 "关于{knowledge_base_name}的知识库"。
self.embed_model = embed_model：

将传入的 embed_model 参数赋值给实例变量 embed_model。
self.kb_path = get_kb_path(self.kb_name) 和 self.doc_path = get_doc_path(self.kb_name)：

调用 get_kb_path 和 get_doc_path 函数，分别获取知识库和文档的路径，并将它们赋值给 kb_path 和 doc_path 实例变量。
self.do_init()：

调用一个方法 do_init，这可能是一个抽象方法，需要在子类中实现具体的初始化逻辑。
def __repr__(self) -> str：

定义了 __repr__ 特殊方法，用于返回类的字符串表示，通常用于调试。
return f"{self.kb_name} @ {self.embed_model}"：返回格式化字符串，包含知识库名称和嵌入模型名称。
整体来看，KBService 类是一个抽象基类，用于定义知识库服务的基本结构和接口。它包含了初始化知识库名称、嵌入模型、知识库和文档路径等属性，并提供了一个 __repr__ 方法来方便地表示类的实例。KB_INFO、EMBEDDING_MODEL、get_kb_path 和 get_doc_path 应该是在类定义之外定义的常量或函数。

'''

from typing import Dict
from abc import ABC, abstractmethod

# 假设的常量和字典
EMBEDDING_MODEL = "default-embedding-model"
KB_INFO: Dict[str, str] = {
    "general": "General knowledge base",
    "medical": "Medical knowledge base"
}

# 假设的函数，用于获取知识库和文档的路径
def get_kb_path(kb_name: str) -> str:
    return f"/path/to/{kb_name}/knowledge_base"

def get_doc_path(kb_name: str) -> str:
    return f"/path/to/{kb_name}/docs"

class KBService(ABC):

    def __init__(self, knowledge_base_name: str, embed_model: str = EMBEDDING_MODEL):
        self.kb_name = knowledge_base_name
        self.kb_info = KB_INFO.get(knowledge_base_name, f"关于{knowledge_base_name}的知识库")
        self.embed_model = embed_model
        
        self.kb_path = get_kb_path(self.kb_name)
        self.doc_path = get_doc_path(self.kb_name)
        self.do_init()

    def do_init(self):
        # 抽象方法，应该在子类中实现
        pass

    def __repr__(self) -> str:
        return f"{self.kb_name} @ {self.embed_model}"
    

class SpecificKBService(KBService):

    def do_init(self):
        # 在这里实现具体的初始化逻辑
        print(f"Initializing {self.kb_name} with embed model {self.embed_model}")

# 使用 SpecificKBService 类
if __name__ == "__main__":
    # 创建一个 SpecificKBService 的实例
    specific_kb_service = SpecificKBService(knowledge_base_name="general")
    
    # 打印实例的字符串表示
    print(specific_kb_service)