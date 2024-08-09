import time  
  
def timing_decorator(func):  
    def wrapper(*args, **kwargs):  
        start_time = time.time()  
        print('******')
        result = func(*args,  **kwargs)  
        print(result)
        print('******')

        print(type(args),*args)


        for arg in args:
            print(arg, '----')

        for key, value in kwargs.items():  
            print(f"Key: {key}, Value: {value}")  
        if 'name' in kwargs:    
            print(f"Key: name (even if default), Value: {kwargs['name']}") 
        else:
            print('啥也没有')

        end_time = time.time()  
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute.")  
        return result  
    return wrapper  
  
@timing_decorator  
def slow_function(t,age:str ,  name= 'hhh'):  
    print('1')
    time.sleep(t)  # 模拟耗时操作  
    print('2')
    return "Finished"  
  
# 调用函数时，装饰器会自动计时  
slow_function(2,'18', name='hhhh')

'''
装饰器函数
先写一个转时期标在函数上面

然后， 定义装饰器函数，传入func,代表原函数

再， 定义实际操作的函数wrapper(*args, **kwargs) //获得参数
把  func和他的参数结合，赋予变量 result ， 即 在装饰其中实现原函数的执行，并拿到返回结果
    ***操作参数***
    返回result
    返回wrapper
    


'''