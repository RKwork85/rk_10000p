'''
多线程


这段代码是一个使用Python的concurrent.futures模块中的ThreadPoolExecutor来并发执行多个任务的示例。下面是对这段代码的详细解释：

创建线程池:
使用with ThreadPoolExecutor() as pool:语句创建了一个线程池。with语句确保线程池在代码块执行完毕后会被正确关闭，释放所有资源。

提交任务到线程池:
通过for kwargs in params:循环，遍历params列表中的每个字典。每个字典包含一个任务的关键字参数。

使用pool.submit(func, **kwargs)将任务提交到线程池。func是要执行的函数，**kwargs将字典解包为关键字参数，传递给func函数。

pool.submit()方法返回一个Future对象，代表一个尚未完成的异步操作。将这个Future对象赋值给thread变量，然后添加到tasks列表中。

收集结果:
使用for future in as_completed(tasks):循环，通过concurrent.futures.as_completed函数迭代tasks列表中的Future对象。as_completed函数会返回一个迭代器，当Future对象表示的任务完成时，迭代器就会产生这个Future对象。

生成结果:
在for future in as_completed(tasks):循环中，使用yield future.result()生成每个任务的结果。future.result()方法会等待对应的任务完成，并返回任务的返回值。如果任务抛出异常，result()方法会重新抛出这个异常。

使用生成器:
由于使用了yield关键字，这个函数返回的是一个生成器(Generator)对象。调用这个函数会得到一个生成器，可以迭代它来逐个获取任务的结果。
'''

def add(a, b):
    return a + b


from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, List, Dict, Generator

# 定义run_in_thread_pool函数
def run_in_thread_pool(
        func: Callable,
        params: List[Dict] = [],
) -> Generator:
    tasks = []
    with ThreadPoolExecutor() as pool:
        for kwargs in params:
            thread = pool.submit(func, **kwargs)            ## 字典解包并传递给一个函数
            tasks.append(thread)

        for future in as_completed(tasks):
            yield future.result()

# 使用示例
if __name__ == "__main__":
    # 准备参数列表，每个字典包含一个任务的关键字参数
    tasks_params = [
        {'a': 1, 'b': 2},
        {'a': 3, 'b': 4},
        {'a': 5, 'b': 6}
    ]

    # 运行任务并打印结果
    for result in run_in_thread_pool(add, tasks_params):
        print(result)

'''
解包
'''
def example_function(a, b):
    print(f"a: {a}, b: {b}")


kwargs = {'a': 1, 'b': 2}
example_function(**kwargs)

example_function(a=1, b=2)