def decorator(func):
    def wrapper(*args, **kwargs):
        print("装饰器开始")
        result = func(*args, **kwargs)
        print("装饰器结束")
        return result
    return wrapper

@decorator
def say_hello():
    print("Hello, World!")

say_hello()