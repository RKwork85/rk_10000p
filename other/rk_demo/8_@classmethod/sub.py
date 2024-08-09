
class A(object):
    bar = 1
    def func1(self):
        print ('foo')
    @classmethod
    def func2(cls):
        print ('func2')


A.func2()

# 下面代码需要先实例化
a = A()
a.func1()
print(a.bar)