def log_decorator(func):  
    def wrapper(*args, **kwargs):  
        print(f"Calling function {func.__name__} with arguments {args}, {kwargs}")  
        result = func(*args, **kwargs)  
        print(f"Function {func.__name__} returned {result}")  
        return result  
    return wrapper  
  
@log_decorator  
def greet(name): 
    print('***********') 
    return f"Hello, {name}!"  
  
# 调用函数时，装饰器会自动打印日志  
greet("Alice")