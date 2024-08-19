# 这个是一个装饰器的联系

总结一下:

装饰器就是在函数执行前进行 **预处理** 和 **后处理** 控制

结构:

```
def method_decortor(func):
    def wrapper(*args, **kargs):

        预处理
        result = func(*args, **kwargs)
        后处理

        return result
    return wrapper 

@method_decortor
def function():

```
还有对于*args 和 **kwargs的使用      

位置参数args
```
for arg in args:            # args 是一个元组 <class 'tuple'>

    print(arg)

```
关键字参数kwargs

```
// 
for key, value in kwargs.items():  # 返回的是一个字典dict_items([('gender', 1), ('age', 18)]) 
    print(key, value)

for key in kwargs.keys()       # 返回的是一个字典dict_keys(['gender', 'age'])
    print(key)
```
