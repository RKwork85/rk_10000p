from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Product:
    name: str
    price: float
    in_stock: int = 0
    tags: List[str] = field(default_factory=list)
    release_date: datetime = field(default_factory=datetime.now)

from dataclasses import fields

def get_default_values_from_dataclass(dataclass_instance):
    default_values = {}
    for field in fields(dataclass_instance):
        # 尝试从实例获取字段的值，如果失败则使用字段的默认值
        value = getattr(dataclass_instance, field.name, field.default)
        default_values[field.name] = value
    return default_values

# 创建 Product 类的实例，不提供任何参数以使用默认值
product_instance = Product("Gadget", 19.99)

# 获取 Product 实例的默认值
default_values = get_default_values_from_dataclass(product_instance)

# 打印结果
print(default_values)