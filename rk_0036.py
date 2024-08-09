class MyClass:
    # 类属性
    class_attribute = 'I am a class attribute'

    def __init__(self, instance_attribute):
        # 实例属性
        self.instance_attribute = instance_attribute

    @classmethod
    def class_method(cls):
        # 可以访问类属性
        print(f"Class method accessed class attribute: {cls.class_attribute}")

    @staticmethod
    def static_method():
        # 静态方法不能访问类属性或实例属性
        print("Static method does not have access to class or instance attributes")

# 调用类方法
MyClass.class_method()  # 通过类直接调用

# 创建一个类的实例
my_instance = MyClass('-----------I am an instance attribute')

# 通过实例调用类方法
my_instance.class_method()  # 通过实例调用，尽管它不需要实例的任何信息

# 调用静态方法
MyClass.static_method()  # 通过类直接调用

# 通过实例调用静态方法
my_instance.static_method()  # 静态方法不依赖于类或实例的属性

'''
类方法（Class method）和静态方法（Static method）是Python中类定义中的两种特殊方法，它们的主要区别在于它们如何与类和实例关联：

类方法：

使用 @classmethod 装饰器定义。
第一个参数是类本身，通常命名为 cls。
可以访问和修改类属性，但不能访问或修改实例属性。
可以通过类直接调用，也可以通过类的实例调用。
静态方法：

使用 @staticmethod 装饰器定义。
不需要类或实例的引用作为第一个参数。
不能访问类或实例的属性，它们与类没有直接关联，只是组织代码的一种方式。
可以通过类直接调用，也可以通过类的实例调用，但通常用于工具函数或不依赖于类或实例状态的函数。
简而言之，类方法与类关联，可以访问类属性，而静态方法与类没有直接关联，通常用作工具函数。
'''