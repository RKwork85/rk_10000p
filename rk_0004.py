# 1 类方法示例:

class MyClass:
    class_attribute = 'I am a class attribute'

    @classmethod
    def get_class_attribute(cls):
        return cls.class_attribute

print(MyClass.get_class_attribute())  # 通过类直接调用
# 普通方法示例:

class MyClass:
    instance_attribute = 'I am an instance attribute'

    def get_instance_attribute(self):
        return self.instance_attribute

obj = MyClass()
print(obj.get_instance_attribute())  # 通过实例调用


# 2. 构造器方法
# 类方法作为替代构造器:

class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_age(cls, name, age):
        return cls(name + ", " + str(age) + " years old")

person = Person.from_age("Alice", 30)
# 普通方法作为构造器:

class Person:
    def __init__(self, name):
        self.name = name

    def rename(self, new_name):
        self.name = new_name

person = Person("Alice")
person.rename("Bob")  # 改变实例属性


# 3. 实现与类相关的功能
# 类方法示例:

class Circle:
    @classmethod
    def area(cls, radius):
        return 3.14159 * radius ** 2

print(Circle.area(5))  # 直接通过类调用
# 普通方法示例:

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14159 * self.radius ** 2

circle = Circle(5)
print(circle.get_area())  # 通过实例调用

# 4. 工厂模式
# 类方法工厂模式:

class Car:
    @classmethod
    def create(cls, model, year):
        return cls(model=model, year=year)

car = Car.create("Toyota", 2020)
# 普通方法工厂模式:

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    @staticmethod
    def factory(model, year):
        return Car(model, year)

car = Car.factory("Toyota", 2020)


# 5. 类方法和静态方法的区别
# 类方法示例:

class Math:
    @classmethod
    def add(cls, x, y):
        return x + y

print(Math.add(5, 3))  # 通过类调用
# 静态方法示例:

class Math:
    @staticmethod
    def multiply(x, y):
        return x * y

print(Math.multiply(5, 3))  # 通过类调用


'''
总结
类方法 (@classmethod) 需要类引用作为第一个参数（通常是 cls），可以访问和修改类属性，并且可以通过类或实例调用。
普通方法（实例方法，无装饰器）需要实例引用作为第一个参数（通常是 self），只能访问和修改实例属性，并且只能通过实例调用。
静态方法 (@staticmethod) 不需要类或实例引用作为参数，不能访问类或实例属性，通常用于实现与类无关的功能，可以通过类或实例调用。
'''
