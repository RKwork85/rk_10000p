'''
自定义特殊方法

'''

class CustomClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __custom__(self, message):
        # 这个方法可以根据需要执行任何操作，但在这里我们只是简单地打印一条消息
        print(f"Custom method called with message: {message}")

# 使用自定义特殊方法
if __name__ == "__main__":
    custom_obj = CustomClass("Alice", 30)
    
    # 直接调用自定义的特殊方法
    custom_obj.__custom__("Hello, this is a custom message!")


def custom_special_method(func):
    """装饰器，用于模拟特殊方法的行为。"""
    def wrapper(self, *args, **kwargs):
        # 在调用原始方法之前执行一些操作
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        
        # 调用原始方法
        result = func(self, *args, **kwargs)
        
        # 在调用原始方法之后执行一些操作
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

class MyClass:
    def __init__(self, value):
        self.value = value

    @custom_special_method
    def my_custom_method(self, message):
        """一个自定义的方法，使用装饰器模拟特殊方法的行为。"""
        return f"Custom method says: {message}"

# 使用示例
if __name__ == "__main__":
    my_obj = MyClass(42)
    print(my_obj.my_custom_method("Hello, World!"))