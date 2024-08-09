# 假设 A 和 B 定义如下：

class A:
    def __init__(self):
        print("Initializing A")

class B(A):  # 确保 B 继承自 A
    def __init__(self):
        print("Initializing B")
        super().__init__()  # 正确调用 A 的 __init__

# 现在定义 C，它同时继承自 A 和 B
# 我们尝试交换 A 和 B 的顺序
class C(B, A):
    def __init__(self):
        print("Initializing C")
        super().__init__()  # 这将按照 MRO 调用 B 的 __init__，然后是 A

c_instance = C()