'''
assert 是 Python 中的一个关键字，用于断言某个条件是否为真。如果条件为真，则程序继续执行；如果条件为假（即 assert 后的表达式结果为 False），程序将抛出 AssertionError 异常。

'''

# 检查变量x是否为正数
x = -1
assert x > 0, "x 必须是正数"