# numbers = (x*2 for x in range(5))

# # 使用生成器表达式
# for number in numbers:
#     print('numbers:', number)

# def simple_generator():
#     for i in range(3):
#         try:
#             yield i
#         except:
#             print("异常捕获")
#             raise

# gen = simple_generator()
# print(next(gen))  # 输出 0  单个输出
# print(next(gen))  # 输出 1




def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 使用生成器
fib = fibonacci()
for _ in range(5):
    print(next(fib))


#other
def some_generator():
    yield 1
    yield 2

def another_generator():
    yield from some_generator()
    yield from (x * 2 for x in range(3))

# 使用 another_generator
for value in another_generator():
    print(value)
print("last")

def nested_generator():
    yield 1
    yield from [2, 3]
    yield 4

for value in nested_generator():
    print(value)


'''使用条件
yield from 语句在 Python 中用于将一个可迭代对象的元素集成到生成器中，使得这些元素可以被当前生成器的迭代器逐个 yield 出来。以下是使用 yield from 的一些条件和场景：

可迭代对象：yield from 后面必须跟一个可迭代对象。这可以是另一个生成器、迭代器，或者任何实现了 __iter__() 或 __getitem__() 协议的类。

生成器函数：yield from 只能在生成器函数内部使用。如果你在普通函数中使用 yield from，Python 解释器会抛出一个语法错误。

逐元素分发：使用 yield from 时，可迭代对象中的每个元素都会被当前生成器函数逐个 yield 出来。这意味着元素的分发是按顺序进行的。

递归生成器：yield from 可以用于递归调用生成器自身，这在实现某些算法时非常有用，例如深度优先搜索。

简化代码：当一个生成器需要产生另一个生成器产生的所有元素时，使用 yield from 可以简化代码，避免显式地调用 next() 函数或使用循环。

错误传播：当 yield from 的可迭代对象引发异常时，异常会传播到包含生成器，除非在生成器内部捕获。

保持状态：使用 yield from 不会改变当前生成器的状态。当前生成器的 __iter__() 和 __next__() 方法仍然有效，并且在分发完成后可以继续产生值。

与 send 方法交互：当使用 yield from 时，如果外部迭代器使用 generator.send(value) 发送值给生成器，该值会被传递给 yield from 的可迭代对象。

兼容性：yield from 是 Python 3.3 引入的特性，因此在 Python 3.2 或更早版本中不可用。

'''