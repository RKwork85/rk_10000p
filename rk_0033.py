from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# 创建 Point 类的实例
p = Point(1, 2)

# 使用自动生成的 __repr__ 方法打印实例
print(p)  # 输出: Point(x=1, y=2)

# 使用自动生成的 __eq__ 方法比较两个实例
q = Point(1, 2)
print(p == q)  # 输出: True
'''在这个示例中，Point 类被定义为一个数据类，它有两个属性 x 和 y。使用 @dataclass 装饰器后，
Python 会自动为 Point 类生成 __init__() 和 __repr__() 方法，以及 __eq__() 方法来比较两个 Point 实例是否相等。'''


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))

# 创建 Point 类的实例
p = Point(1, 2)

# 使用手动实现的 __repr__ 方法打印实例
print(p)  # 输出: Point(x=1, y=2)

# 使用手动实现的 __eq__ 方法比较两个实例
q = Point(1, 2)
print(p == q)  # 输出: True