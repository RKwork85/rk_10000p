# 如何定义一个特殊方法

# __init__(self, ...): 类的构造器，用于初始化新创建的对象。
class MyClass:
    def __init__(self, value):
        self.value = value

# __del__(self): 类的析构器，当对象被销毁时调用。

class MyClass:
    def __del__(self):
        print("Object is being destroyed")

# __str__(self): 当使用 print() 函数或 str() 时调用，返回对象的字符串表示。
# 
class MyClass:
    def __str__(self):
        return "MyClass with value " + str(self.value)

# __repr__(self): 当使用 repr() 函数时调用，返回对象的官方字符串表示，通常可以用来重新创建该对象。
class MyClass:
    def __repr__(self):
        return "MyClass(" + repr(self.value) + ")"
    
# __len__(self): 当使用 len() 函数时调用，返回容器类型的长度。
class MyClass:
    def __len__(self):
        return len(self.value)

# __getitem__(self, key): 用于获取序列的元素，如 obj[key]
class MyClass:
    def __getitem__(self, key):
        return self.value[key]
    
# __setitem__(self, key, value): 用于设置序列的元素，如 obj[key] = value。
class MyClass:
    def __setitem__(self, key, value):
        self.value[key] = value

# __delitem__(self, key): 用于删除序列的元素，如 del obj[key]。
class MyClass:
    def __delitem__(self, key):
        del self.value[key]

# __call__(self, *args, **kwargs): 允许一个对象像函数那样被调用，如 obj()。

class MyClass:
    def __call__(self, *args, **kwargs):
        print("Called with", args, kwargs)

# __enter__(self) 和 __exit__(self, exc_type, exc_value, traceback): 用于定义上下文管理器，在 with 语句中使用。

class MyClass:
    def __enter__(self):
        print("Entering context")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


# special_methods.py

class MyClass:
    def __init__(self, value):
        self.value = value
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

    def __str__(self):
        return "MyClass with value " + str(self.value)

    def __repr__(self):
        return "MyClass(" + repr(self.value) + ")"

    def __len__(self):
        return len(self.value)

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __delitem__(self, key):
        del self.value[key]

    def __call__(self, *args, **kwargs):
        print("Called with", args, kwargs)

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

# 使用示例
if __name__ == "__main__":
    # 构造和析构
    my_obj = MyClass([1, 2, 3])
    print(my_obj)  # 调用 __str__
    print(repr(my_obj))  # 调用 __repr__
    print(len(my_obj))  # 调用 __len__
    my_obj[1] = 4  # 调用 __setitem__
    print(my_obj[1])  # 调用 __getitem__
    del my_obj[1]  # 调用 __delitem__
    del my_obj  # 调用 __del__

    # 调用
    my_callable_obj = MyClass("callable")
    my_callable_obj("arg1", "arg2")

    # 上下文管理器
    with MyClass("context") as ctx:
        print("Inside the context")
















