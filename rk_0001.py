import importlib.util

# 创建模块规范
spec = importlib.util.spec_from_file_location("my_module", "./other/my_module.py")
if spec:
    # 创建模块对象
    module = importlib.util.module_from_spec(spec)
    # 执行模块
    spec.loader.exec_module(module)
    # 使用模块
    result = module.some_function()
else:
    print("Failed to load the module")

    
'''
spec.loader.exec_module(module) 和常规的 import 语句在 Python 中都是用来加载模块的，但它们之间存在一些关键的区别：

导入机制:

import 语句是 Python 的标准导入机制，用于从模块的文件中导入定义的类、函数和变量等，并将它们集成到当前的命名空间中。
spec.loader.exec_module(module) 是一个更为底层的导入方式，它使用 importlib 库提供的接口来执行模块代码。这种方式允许你创建一个模块对象，但不会自动将模块的内容导入到当前命名空间。
命名空间污染:

使用 import 语句导入的模块会将其名称和定义的属性添加到当前的全局或局部命名空间中，可能会造成命名空间的污染。
使用 exec_module 方法执行的模块代码在模块对象自己的命名空间中运行，不会影响当前的命名空间。
灵活性:

import 语句相对简单，适用于大多数标准导入场景。
exec_module 提供了更高的灵活性，允许你控制模块的加载过程，例如动态创建模块对象、指定不同的加载器等。
使用场景:

import 是日常编程中最常见的导入模块的方式。
exec_module 通常用于需要动态加载模块的情况，或者当你需要在一个隔离的环境中执行模块代码时。
模块缓存:

使用 import 语句导入的模块会被缓存，这意味着第二次尝试导入同一个模块时，Python 会直接从缓存中获取模块，而不会重新执行模块代码。
使用 exec_module 时，你可以绕过模块缓存，每次调用 exec_module 都会重新执行模块代码。
重载模块:

要重载一个使用 import 导入的模块，你需要使用特殊的机制，如 importlib.reload()。
使用 exec_module 可以在不卸载模块的情况下重新执行模块代码。
'''
'''
在 Python 中，这种隔离可以通过几种方式实现（隔离：不会与全局作用域中的其他变量或函数发生冲突。）：

模块层面的隔离：

每个 Python 文件就是一个模块，模块有自己的全局命名空间。当你导入一个模块时，模块中定义的全局变量和函数不会自动成为主程序的全局变量和函数，除非显式地导入它们。
函数作用域的隔离：

函数有自己的局部命名空间。在函数内部定义的变量不会影响函数外部的变量，除非它们在函数外部已经被定义（并且是非局部或全局变量）。
类和实例的隔离：

类定义了自己的命名空间，类属性和方法不会影响类的外部。实例化对象时，每个实例有自己的状态，但共享类定义的方法。
上下文管理器：

使用 with 语句和上下文管理器（如文件操作中的 with open(...) as file:），可以创建一个临时的、干净的环境来执行代码，比如确保文件操作完成后正确关闭文件。
虚拟环境：

Python 虚拟环境（如 venv 或 virtualenv）允许你为不同的项目创建隔离的 Python 运行环境，每个环境有自己的 Python 二进制文件和一套独立的第三方库。
动态导入和执行：

使用 importlib 和 exec_module 进行动态导入和执行时，你可以控制模块的加载和执行过程，模块的命名空间可以被隔离，不会影响到当前的全局或局部命名空间。
'''

'''
sys.argv 列表的工作原理如下：

sys.argv[0] 总是脚本的名称，即你运行的 Python 文件的名称。
sys.argv[1] 是传递给脚本的第一个参数。
sys.argv[2] 是第二个参数，以此类推。
例如，如果你有一个 Python 脚本 my_script.py，并且你在命令行中这样调用它：

python my_script.py arg1 arg2 arg3
那么在 my_script.py 内部，sys.argv 将会是：

['my_script.py', 'arg1', 'arg2', 'arg3']'''