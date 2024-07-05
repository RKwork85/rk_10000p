class ConfigLoader:
    def __getattr__(self, name: str):
        print('我被调用啦')
        if name == "ConfigBasic":
            return _import_ConfigBasic()
        # 可以根据需要添加更多的条件
        else:
            # 如果属性名不匹配任何已知属性，抛出 AttributeError
            raise AttributeError(f"{name} is not defined")
            # print("没有这个属性名")

def _import_ConfigBasic():
    return "ConfigBasic instance"

# 实例化 ConfigLoader 类
loader = ConfigLoader()

# 当你尝试访问一个属性，而这个属性在 ConfigLoader 类或 loader 实例中未定义时
config_basic = loader.ConfigBasi  # 这将触发 __getattr__ 方法
print(config_basic)

'''
在这个例子中：

ConfigLoader 类定义了 __getattr__ 方法，它覆盖了类的默认行为。
当我们创建了 ConfigLoader 的一个实例 loader 后，我们尝试访问 loader.ConfigBasic 属性。
因为 ConfigBasic 属性在 ConfigLoader 类或 loader 实例中没有明确定义，所以 __getattr__ 被自动调用。
__getattr__ 方法检查请求的属性名 name，如果它等于 "ConfigBasic"，它就调用 _import_ConfigBasic() 函数，并返回该函数的结果。
在这个过程中，loader 是 ConfigLoader 的一个实例，也就是你提到的“对象”。这个对象在访问不存在的属性时触发了 __getattr__ 方法的调用。


'''
