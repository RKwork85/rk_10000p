'''
as_completed 是 Python concurrent.futures 模块中的一个函数，它用于迭代一个 Future 对象的列表，按完成的顺序产生这些对象。Future 对象代表了一个异步操作，可能尚未完成。当你使用 ThreadPoolExecutor 或 ProcessPoolExecutor 提交任务时，每个任务都会返回一个 Future 对象。

以下是 as_completed 的一些关键点：

迭代完成的任务：as_completed(fs) 接受一个 Future 对象列表 fs，并返回一个迭代器。当列表中的某个 Future 对象对应的任务完成时，迭代器就会产生（yield）这个 Future 对象。

任务完成的顺序：产生的顺序是任务实际完成的顺序，而不是它们被提交的顺序。这意味着，最先完成的任务会被最先处理。

使用场景：当你需要在任务完成时立即处理结果，而不是等待所有任务都完成后再处理时，as_completed 是非常有用的。这可以用于实时数据处理或当任务运行时间差异较大时，避免不必要的等待。

阻塞行为：as_completed 会阻塞直到至少有一个任务完成。如果所有任务都还没有完成，调用 next(as_completed(fs)) 将会阻塞执行，直到至少有一个任务完成。

异常处理：当使用 as_completed 迭代器产生的 Future 对象调用 result() 方法时，如果对应的任务中抛出了异常，result() 将会重新抛出这个异常。因此，在使用 as_completed 时，通常需要在调用 result() 后进行异常处理。

与 wait 比较：与 as_completed 类似的另一个函数是 wait，但 wait 会阻塞直到所有任务都完成或超时，而 as_completed 则是在每个任务完成时立即返回。
'''

from concurrent.futures import ThreadPoolExecutor, as_completed

# 定义一个简单的函数，模拟耗时操作
def task(n):
    print(f"Processing {n}")
    return n * 2

# 创建一个线程池
with ThreadPoolExecutor(max_workers=2) as executor:
    # 提交多个任务
    futures = [executor.submit(task, i) for i in range(5)]

    # 使用 as_completed 迭代完成的任务
    for future in as_completed(futures):
        result = future.result()
        print(f"Task returned: {result}")


'''
fs: The sequence of Futures (possibly created by different Executors) to
            iterate over.什么意思
            fs: 这是一个参数名称，代表一个序列（sequence），在这个上下文中，它是一个 Future 对象的列表或集合。
The sequence of Futures: 这是在描述 fs 参数的内容，即一系列 Future 对象。
(possibly created by different Executors): 这是一个附加说明，指出这些 Future 对象可能是由不同的 Executor 实例创建的。在 concurrent.futures 模块中，

Executor 是一个抽象基类，其子类 ThreadPoolExecutor 和 ProcessPoolExecutor 用于创建线程池和进程池，进而可以提交任务并返回 Future 对象。
to iterate over: 这部分说明了 as_completed 函数的目的，即迭代（iterate）这些 Future 对象。


综合来看，这句话的意思是：as_completed 函数接受一个 Future 对象的序列作为参数 fs，这些 Future 对象可以由不同的 Executor 实例创建，然后 as_completed 会迭代这些 Future 对象。

这提供了一种灵活性，允许你将来自不同线程池或进程池的任务 Future 组合在一起，然后按它们完成的顺序进行处理。然而，需要注意的是，虽然 as_completed 可以接受来自不同 Executor 的 Future 对象，但在实际使用中，通常我们会将相同类型的 Future 对象（即由相同类型的 Executor 创建）传递给 as_completed，以避免潜在的复杂性和错误。
'''