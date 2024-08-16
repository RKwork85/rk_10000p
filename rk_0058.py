'''在 Python 中，可调用对象（Callable）是指可以被调用执行的对象。以下是一些常见的可调用对象类型：

函数: Python 中最基本的可调用对象。例如：

python
def my_function():
    print("Hello, World!")
类: 类本身可以作为可调用对象来创建实例。例如：

python
class MyClass:
    pass
instance = MyClass()  # 类作为可调用对象使用
实例方法: 与类相似，实例方法也是可调用的。例如：

python
class MyClass:
    def my_method(self):
        print("Hello from a method!")
instance = MyClass()
instance.my_method()  # 实例方法的调用
静态方法: 静态方法可以通过类或实例来调用。例如：

python
class MyClass:
    @staticmethod
    def my_static_method():
        print("Hello from a static method!")
MyClass.my_static_method()  # 通过类调用静态方法
类方法: 类方法可以通过类或实例来调用，并且它们可以访问类变量。例如：

python
class MyClass:
    class_var = "I'm a class variable"

    @classmethod
    def my_class_method(cls):
        print(cls.class_var)
MyClass.my_class_method()  # 通过类调用类方法
Lambda 表达式: 匿名函数，用于创建小型的一次性函数。例如：

python
add = lambda x, y: x + y
print(add(5, 3))  # 输出 8
模块: 模块本身也可以作为可调用对象，通常用于执行模块级别的初始化代码。例如：

python
import some_module
some_module.some_function()  # 调用模块中的函数
内置函数: Python 提供的内置函数，如 print, len, range 等。

函数对象: 任何函数的实例，包括用户定义的函数和内置函数。

可调用的类实例: 某些类实例可以被调用，这通常通过定义 __call__ 方法来实现。例如：

python
class CallableClass:
    def __call__(self):
        print("I'm callable!")

callable_instance = CallableClass()
callable_instance()  # 类实例作为可调用对象使用
装饰器: 装饰器本质上是可调用的，它们可以应用于函数、方法或类来修改或增强它们的行为。

生成器: 虽然生成器主要用于迭代，但它们也可以通过 next() 函数来调用。'''