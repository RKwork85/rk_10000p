# 字典赋值
# 当然，有几种不同的方法可以向字典中添加键值对。以下是一些示例：

# 方法1：直接赋值
# python
# self.competitor_info["number"] = 123
# 这会将 "number" 键的值设置为 123。

# 方法2：使用 update 方法
# python
# self.competitor_info.update({"number": 123})
# 这会更新字典，将 "number" 键的值设置为 123。

# 方法3：使用 setdefault 方法
# python
# self.competitor_info.setdefault("number", 123)
# 这会将 "number" 键的值设置为 123，但如果该键已经存在，则不会更改其值。

# 方法4：使用 dict 类的构造函数
# python
# self.competitor_info = {"number": 123}
# 这会创建一个新的字典，其中包含 "number" 键及其值。

# 方法5：使用 ** 操作符（适用于更复杂的字典结构）
# python
# new_info = {"number": 123}
# self.competitor_info = {**self.competitor_info, **new_info}
# 这会将 new_info 字典中的键值对合并到 self.competitor_info 中。

# 方法6：使用 collections.defaultdict
# 如果你希望在添加新键时自动赋予默认值，可以使用 collections.defaultdict：

# python
# from collections import defaultdict

# class Competition:
#     def __init__(self):
#         self.competitor_info = defaultdict(int)  # 默认值为整数类型

#     def add_competitor_number(self, competitor_id, number):
#         self.competitor_info[competitor_id] = number

#     def display_info(self):
#         print(dict(self.competitor_info))

# comp = Competition()
# comp.add_competitor_number("001", 10)
# comp.add_competitor_number("002", 20)
# comp.display_info()
# 在这个示例中，defaultdict 确保了如果尝试访问不存在的键，它将自动创建并赋予默认值（这里为整数类型）。这样，你可以简单地添加键值对而不必担心键不存在的情况。