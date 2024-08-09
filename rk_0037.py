# 使用 *args 的示例
# *args 用于传递任意数量的位置参数给函数。这些参数在函数内部被解析为一个元组。

# python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# 调用函数
print(sum_all(1, 2, 3, 4))  # 输出: 10
# 使用 **kwargs 的示例
# **kwargs 用于传递任意数量的关键字参数给函数。这些参数在函数内部被解析为一个字典。

# python
def greet(**kwargs):
    name = kwargs.get('name', 'Guest')
    greeting = kwargs.get('greeting', 'Hello')      # 提取关键字的值，若没有则默认
    print(f"{greeting}, {name}!")

# 调用函数
greet(name='Alice', greeting='Good morning')  # 输出: Good morning, Alice!
greet(name='Bob')  # 输出: Hello, Bob!
# 同时使用 *args 和 **kwargs
# 你可以在同一个函数中同时使用 *args 和 **kwargs，通常 *args 会在 **kwargs 之前。

# python
def print_all(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 调用函数
print_all(1, 2, 3, name='Alice', occupation='Engineer')
# 输出:
# 1
# 2
# 3
# name: Alice
# occupation: Engineer