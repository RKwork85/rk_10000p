'''
生成器

生成器（Generator）是 Python 中的一种特殊的迭代器，它允许你逐个产生值，而不是一次性创建并存储所有值。这使得生成器非常适合处理大数据集，因为它可以节省内存。下面是一个生成器的用法示例：
'''
def count_up_to(max):               # 尽管 count_up_to(5) 这个函数调用只执行了一次，但生成器对象可以被多次迭代，每次迭代都会产生一个新的值，直到达到最大值。
    count = 1
    print('count的值：', count)
    while count <= max:
        yield count
        count += 1

# 使用生成器
for number in count_up_to(5):
    print(number)

    # 这个示例中的 count_up_to 函数是一个生成器，它逐个产生从 1 到 max 的整数。


def count_up_to(max):
    return [count for count in range(1, max + 1)]  # 使用列表推导式

# 使用列表
for number in count_up_to(5):
    print(number)
    '''
    执行逻辑：
    当定义一个使用 yield 的函数时，Python 将其视为一个生成器（generator）。每次调用生成器函数时，都会返回一个生成器对象。这个对象实现了迭代器协议，可以在 for 循环中使用。

下面是 count_up_to 函数的代码逻辑：

函数定义：count_up_to 函数接受一个参数 max，表示生成数字的最大值。

初始化变量：在函数开始时，定义了一个局部变量 count 并初始化为 1。print('count的值：', count) 这行代码会在函数开始时打印 count 的初始值。

循环和 yield：函数中有一个 while 循环，条件是 count 小于或等于 max。在循环体内部：

yield count：当循环执行到 yield 语句时，生成器会返回当前的 count 值给请求值的迭代器，并且暂停执行。此时，count 的当前值会被记住。
count += 1：在下一次迭代器请求值时，count 的值会增加 1，然后循环继续。
生成器对象：当 for 循环开始时，count_up_to(5) 被调用，创建了一个生成器对象。

迭代过程：for 循环迭代生成器对象：

第一次迭代：生成器开始执行，打印 count的值：1，然后 yield 1，for 循环接收到 1，打印出来。
第二次迭代：生成器从上次 yield 后暂停的地方恢复执行（count 已经是 2），count 增加到 3，然后 yield 2，以此类推，直到 count 达到 6，循环结束。
循环结束：当 count 的值超过 max（在这个例子中是 5），while 循环结束，生成器完成所有工作，for 循环也结束。



    函数 count_up_to 定义了一个生成器，它逐个产生从 1 到 max（在这个例子中是 5）的整数。当你不加 yield 语句，而是直接返回一个列表时，区别主要体现在以下几个方面：

    内存使用：尽管 count_up_to(5) 这个函数调用只执行了一次，但生成器对象可以被多次迭代，每次迭代都会产生一个新的值，直到达到最大值。

    生成器（yield）：使用生成器时，每次只产生一个值，不需要一次性在内存中存储整个序列，这在处理大量数据时可以节省大量内存。
    列表（不加 yield）：如果使用列表，你需要一次性创建并存储整个序列，这可能会消耗大量内存。
    性能：

    生成器：生成器在迭代时是惰性的（lazy），即只有在需要下一个值时才会计算它，这可以提高性能，特别是对于大数据集。
    列表：列表需要先计算并存储所有元素，然后才能开始迭代。
    可读性和简洁性：

    生成器：使用生成器可以使代码更加简洁，特别是当你只需要迭代一次数据时。
    列表：使用列表可能需要更多的代码来创建和处理数据。
    灵活性：

    生成器：生成器可以很容易地进行修改以产生不同的序列，或者在迭代过程中添加额外的逻辑。
    列表：如果需要修改序列的生成方式，可能需要重写整个列表推导式或循环。
    异常处理：

    生成器：生成器可以在迭代过程中捕获和处理异常，并且可以继续迭代。
    列表：列表一旦创建，其内容就固定了，如果需要处理异常，可能需要在创建列表之前或之后进行。
    '''


def string_generator(phrases):
    for phrase in phrases:
        yield phrase
        yield from [letter for letter in phrase]  # 这里使用了列表推导式

phrases = ["hello", "world"]
for value in string_generator(phrases):
    print(value)


# 创建一个生成器表达式
numbers = (x*2 for x in range(5))

# 使用生成器表达式
for number in numbers:
    print('numbers:', number)

def simple_generator():
    for i in range(3):
        try:
            yield i
        except:
            print("异常捕获")
            # raise

gen = simple_generator()
print(next(gen))  # 输出 0  单个输出
print(next(gen))  # 输出 1
# gen.throw(ZeroDivisionError)  # 抛出异常






