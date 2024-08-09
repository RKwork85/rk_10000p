def dog_decorator(func):
    def wrapper(*args, **kwargs):
        print('汪~汪~汪~')
        print('-------------')
        result = func(*args, **kwargs)
        print('-------------')

        print(f'谢谢光临！{args}')


        print('************对于arg参数的使用*************')
        print(type(args))
        
        for i in args:              
            print (i)

        print('****args的两种写法*****')    
        for i in range(len(args)):
            print(args[i])

        print('************对于arg参数的使用*************')


        print('************对于kwarg参数的使用*************')
        print(kwargs.items())
        for key, value in kwargs.items():
            print(key, value)
        print('*********')
        print(kwargs.keys())
        for i in kwargs.keys():
            print(i)
        print('*********')


        
        return result
    return wrapper


@dog_decorator
def hello(name, number, gender=0, age=0):
    
    print(f'{name}主人，欢迎您的光临！\n主人:{name}点了 {number} 桌')


if __name__ == '__main__':
    hello('muzi',10,gender=1, age=18 )









'''
装饰器函数

在函数执行前后进行预处理和后处理

    主函数是 欢迎主人
    在 欢迎主人前会有 狗 提前预警
    在 函数结束后会有 门 自动语音
'''