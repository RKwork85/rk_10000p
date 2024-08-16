class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

# 创建一个Person对象
person = Person("Alice", 30)

# 打印对象
print(person)  # 输出: Person(name='Alice', age=30)