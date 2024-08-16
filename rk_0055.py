


import rk_0056

# 假设我们想要获取 TensorFlowWorker 类
provider = "TensorFlowWorker"
worker_class = getattr(rk_0056, provider, None)

if worker_class is not None:
    worker_instance = worker_class()  # 创建类的实例
    print(worker_instance)
else:
    print(f"The provider {provider} is not available.")


class ExampleClass:
    def method(self):
        print("Method called")

# 使用 getattr 来动态调用方法
example = ExampleClass()
method = "method"
getattr(example, method, None)()  # 这将调用 ExampleClass 的 method 方法