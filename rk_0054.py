'''
locals() 将域内的变量都字典化
locals()['key']
'''

def get_server_configs():
    # 假设这些是函数内的局部变量
    server_name = "example_server"
    port = 8080
    _internal_config = "should_not_include"  # 以 _ 开头，应被排除

    # 一些自定义配置
    custom_config = {
        "api_version": "v1",
        "maintenance_mode": False,
    }

    # 使用字典推导式和 locals() 来收集所有非下划线开头的局部变量
    local_configs = {k: v for k, v in locals().items() if not k.startswith("_")}

    # 更新 local_configs 字典，合并 custom_config 字典
    server_configs = {**local_configs, **custom_config}

    # 返回合并后的配置字典
    return server_configs

# 调用函数并打印结果
configs = get_server_configs()
print("示例一")
print(configs)

def print_locals():
    a = 10
    b = 20
    print("示例二")

    print(locals())

print_locals()


def dynamic_access():
    x = 5
    y = 10
    print("示例三")

    print(locals()['x'])  # 直接通过变量名字符串访问变量
    print(locals()['y'])

dynamic_access()

def collect_non_private_variables():
    public_var = {"aaa": 42}
    _private_var = 100
    for k, v in locals().items():
        print("字典get用法",v.get("aaa"))

    return {k: v for k, v in locals().items() if not k.startswith('_')}

result = collect_non_private_variables()
print("示例四")

print(result)  # 输出将只包含 public_var