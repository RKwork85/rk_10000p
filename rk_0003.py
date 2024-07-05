from functools import cached_property
class ExpensiveResource:
    def __init__(self, size):
        self._size = size
        self._expensive_data = None

    @cached_property
    def expensive_data(self):
        print("RK***********************")
        # 假设这是一个计算代价很高的操作
        return [x**2 for x in range(self._size)]

from typing import overload, Union

class Calculator:
    @overload
    def add(self, x: int, y: int) -> int:
        print('整形道')
        pass

    # @overload
    # def add(self, x: float, y: float) -> float:
    #     print('浮点型道')
    #     pass

    def add(self, x, y):
        # 实际的加法逻辑
        print('hhh')
        return x + y
    
from typing import overload, List

class Example:
    @overload
    def process(self, data: List[int]) -> List[int]:
        pass

    @overload
    def process(self, data: str) -> str:
        pass

    def process(self, data):
        # 这里是实际的处理逻辑，可以根据需要实现
        return data




# 使用示例
resource = ExpensiveResource(1000)
print(resource.expensive_data)  # 第一次访问，将计算并缓存结果
print(resource.expensive_data)  # 第二次访问，直接返回缓存的结果




# 使用示例
calc = Calculator()
print(calc.add(1, 2))  # 静态类型检查器知道这是整数加法
print(calc.add(1.5, 2.3))  # 静态类型检查器知道这是浮点数加法

# 使用示例
example = Example()
# 如果使用 MyPy 或在 IDE 中，这里会有类型相关的提示和检查
print(example.process([1, 2, 3]))  # 正确使用，List[int] -> List[int]
print(example.process("hello"))    # 正确使用，str -> str
# 在这个例子中，process 方法被重载以接受 List[int] 或 str 类型的参数。虽然运行时行为没有变化，但类型检查器和 IDE 可以使用这些信息来提供更好的开发体验。


'''
@cached_property 装饰器:
这个装饰器用于将一个方法转变为一个只计算一次的属性。当你调用这个方法时，它的结果会被缓存，并且下一次访问这个属性时，会直接返回缓存的结果，而不是再次执行方法。这通常用于性能优化，避免重复计算。

示例：

class MyClass:
    @cached_property
    def expensive_property(self):
        # 这里可以放置一些计算成本高昂的代码
        return some_expensive_computation()
在这个示例中，expensive_property 只会被计算一次，之后每次访问这个属性时都会返回第一次计算的结果。

@overload 装饰器:
这个装饰器用于 Python 类型注解中，它允许你为同一个函数定义多个重载版本。这主要用于静态类型检查工具，如 MyPy，以帮助它们理解函数可以接受不同类型的参数。

示例：

from typing import overload

class MyClass:
    @overload
    def add(self, other: int) -> int:
        ...

    @overload
    def add(self, other: str) -> str:
        ...

    def add(self, other):
        # 实际的实现逻辑
        pass
'''