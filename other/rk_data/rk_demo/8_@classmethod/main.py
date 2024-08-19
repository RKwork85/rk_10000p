from enum import Enum, auto


class DispatchMethod(Enum):
    LOTTERY = auto()
    SHORTEST_QUEUE = auto()

    @classmethod
    def from_str(cls, name):
        if name == "lottery":
            return cls.LOTTERY
        elif name == "shortest_queue":
            return cls.SHORTEST_QUEUE
        else:
            raise ValueError(f"Invalid dispatch method")



method = DispatchMethod.from_str("lottery")
print(method)  # 输出：DispatchMethod.LOTTERY

method = DispatchMethod.from_str("shortest_queue")
print(method)  # 输出：DispatchMethod.SHORTEST_QUEUE

# method = DispatchMethod.from_str("invalid_method")
# 引发ValueError异常，提示输入了无效的调度方法

# dispatch_method = DispatchMethod()
# dispatch_method.from_str("lottery")
'''
这个 from_str() 方法可以加上 @classmethod 装饰器,但是不是必须的。

使用 @classmethod 装饰器的主要目的是让这个方法可以在不实例化类的情况下调用。这意味着你可以直接使用 DispatchMethod.from_str("lottery") 来调用这个方法,而不需要先创建一个 DispatchMethod 实例。

如果没有 @classmethod 装饰器,你仍然可以调用这个方法,但需要先创建一个 DispatchMethod 实例,比如 dispatch_method = DispatchMethod(); dispatch_method.from_str("lottery")。

所以使用 @classmethod 装饰器可以让代码更加简洁和方便。不过,如果你不需要在没有实例化类的情况下调用这个方法,那么不加 @classmethod 装饰器也没有问题。

总的来说,使用 @classmethod 装饰器是一种良好的实践,可以提高代码的可读性和可维护性,但并不是必须的。最终决定是否使用取决于您的具体需求和编码风格。
'''