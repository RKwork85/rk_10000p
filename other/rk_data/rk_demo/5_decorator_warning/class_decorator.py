def uppercase_decorator(cls):
    """
    将类中的所有方法的返回值转换为大写
    """
    class DecoratedClass(cls):
        def __getattribute__(self, name):
            # 获取原始方法
            attribute = super().__getattribute__(name)
            
            # 如果是方法，则将其返回值转换为大写
            if callable(attribute):
                def wrapper(*args, **kwargs):
                    result = attribute(*args, **kwargs)
                    if isinstance(result, str):
                        return result.upper()
                    return result
                
                return wrapper
            
            return attribute
    
    return DecoratedClass


@uppercase_decorator
class MyString:
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value


my_string = MyString("Hello, World!")
print(my_string.get_value())  # 输出 "HELLO, WORLD!"
