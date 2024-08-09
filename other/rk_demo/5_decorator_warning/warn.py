
'''
Warning	所有警告类别类的基类，它是 Exception 的子类
UserWarning	函数 warn() 的默认类别
DeprecationWarning	用于已弃用功能的警告（默认被忽略）
SyntaxWarning	用于可疑语法的警告
RuntimeWarning	用于有关可疑运行时功能的警告
FutureWarning	对于未来特性更改的警告
PendingDeprecationWarning	对于未来会被弃用的功能的警告（默认将被忽略）
ImportWarning	导入模块过程中触发的警告（默认被忽略）
UnicodeWarning	与 Unicode 相关的警告
BytesWarning	与 bytes 和 bytearray 相关的警告 (Python3)
ResourceWarning


"error"	    将匹配警告转换为异常
"ignore"	忽略匹配的警告
"always"	始终输出匹配的警告
"default"	对于同样的警告只输出第一次出现的警告
"module"	在一个模块中只输出第一次出现的警告
"once"	    输出第一次出现的警告,而不考虑它们的位置

https://blog.csdn.net/low5252/article/details/109334695
'''

import warnings


def deprecated_function():
    warnings.warn("This function is deprecated", DeprecationWarning)
    # ... 其他代码
    print("Please try using a different running method.")


if __name__ == '__main__':
    deprecated_function()

