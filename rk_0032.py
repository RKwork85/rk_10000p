from dataclasses import dataclass, field

# 使用 default_factory 参数的 field 函数
from datetime import datetime

@dataclass
class Product:
    name: str
    price: float
    in_stock: int = field(default=0, repr=False)  # repr=False 表示在 __repr__ 输出时不包含该字段
    last_updated: datetime = field(default_factory=datetime.now)

# 创建 Product 类的实例
product = Product("Gadget", 19.99)

# 访问字段
print(product.name)         # 输出: Gadget
print(product.price)        # 输出: 19.99
print(product.in_stock)    # 输出: 0
print(product.last_updated) # 输出: 2024-08-02 12:00:00 (或其他当前时间)

# 使用 __repr__ 方法输出实例
print(product)              # 输出: Product(name='Gadget', price=19.99)
                             # 注意 in_stock 字段没有被包含


'''
在上面的代码中，Product 类使用 @dataclass 装饰器自动生成了 __init__() 和 __repr__() 方法。字段 in_stock 使用了 field 函数来设置默认值和控制 __repr__ 方法的输出。字段 last_updated 使用了 default_factory 参数，它接受一个无参的函数，该函数会在创建实例时被调用以生成默认值。

field 函数的参数包括：

default: 字段的默认值。
default_factory: 一个无参的函数，用于生成字段的默认值。
init: 布尔值，指示是否在自动生成的 __init__() 方法中包含该字段，默认为 True。
repr: 布尔值，指示是否在自动生成的 __repr__() 方法中包含该字段，默认为 True。
compare: 布尔值，指示是否在自动生成的比较方法中包含该字段，默认为 True。
hash: 布尔值，仅当 compare 为 True 时有效，指示是否在自动生成的 __hash__() 方法中包含该字段，默认为 False。
使用 dataclasses 可以大大简化数据存储类的定义，让代码更加简洁和易于维护
'''
