def flexible_function(*args, **kwargs):
    # 处理位置参数
    print("位置参数列表：")
    print(args)  # 打印所有位置参数的列表

    # 处理关键字参数
    print("关键字参数字典：")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    # 这里结合使用 *args 和 **kwargs 来调用另一个函数
    def inner_function(*inner_args, **inner_kwargs):
        print("内部函数接收到的位置参数：")
        print(inner_args)
        print("内部函数接收到的关键字参数：")
        for k, v in inner_kwargs.items():
            print(f"{k}: {v}")

    # 调用内部函数，传递所有外部接收到的 *args 和 **kwargs
    inner_function(*args, **kwargs)

# 现在我们调用灵活的外部函数，传递一些位置参数和关键字参数
flexible_function(1, 2, 3, name="Alice", job="Engineer")

# 输出将展示：
# 位置参数列表：
# (1, 2, 3)
# 关键字参数字典：
# name: Alice
# job: Engineer
# 内部函数接收到的位置参数：
# (1, 2, 3)
# 内部函数接收到的关键字参数：
# name: Alice
# job: Engineer


# 在Python中，self 通常指的是类实例的引用，它在类的非静态方法中自动传递。当你使用 self = args[0] 这样的代码时，通常是在装饰器中，尤其是当装饰器应用于类的方法时。这行代码的目的是捕获传递给方法的第一个参数，通常这个参数是 self。

# 以下是一个使用 self = args[0] 的示例，我们将创建一个简单的类，然后使用装饰器来增强类方法的行为：

# python

print('--------------------')
from functools import wraps

class MyClass:
    def __init__(self, name = 'muzihhh'):
        self.name = name

    # 假设这是一个需要被装饰的方法
    def greet(self, message):
        print(f"{self.name}: {message}")

# 定义一个装饰器
def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        self = args[0]  # 取出第一个参数作为 self
        # for i in args:
        #     print(i)

        # for k , v in kwargs.items():
        #     print(k)
        #     print(v)
        print(self.name)
        print("Something is happening before the method is called.")
        return fn(*args, **kwargs)  # 调用原始方法
    return wrapper

# 使用装饰器
MyClass.greet = my_decorator(MyClass.greet)

# 创建 MyClass 的实例
obj = MyClass("mmmm")

# 调用被装饰的方法
obj.greet("Hello, World!")

# obj = MyClass("muzi")
# MyClass.greet = my_decorator(obj.greet)
# 在这个示例中，我们首先定义了一个 MyClass 类，它有一个初始化方法 __init__ 和一个 greet 方法。然后我们定义了一个装饰器 my_decorator，它增强了 MyClass 的 greet 方法。在装饰器内部，我们使用 self = args[0] 来捕获传递给 greet 方法的第一个参数，这个参数是类实例 self。

# 当我们创建 MyClass 的一个实例 obj 并调用 obj.greet("Hello, World!") 时，实际上会触发装饰器中的 wrapper 函数。在 wrapper 函数中，我们首先打印一条消息，然后调用原始的 greet 方法。这样，我们就在不修改原始类定义的情况下，增加了额外的行为。