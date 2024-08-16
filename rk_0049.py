# 假设的函数，返回网络服务地址
def fschat_controller_address():
    return "192.168.1.100:8080"

def fschat_model_worker_address():
    return "192.168.1.101:9090"

def fschat_openai_api_address():
    return "192.168.1.102:7070"

# 默认代理设置的字典
default_proxies = {
    # do not use proxy for locahost
    "all://127.0.0.1": None,
    "all://localhost": None,
}

# 遍历每个地址并更新代理设置
addresses = [
    fschat_controller_address(),
    fschat_model_worker_address(),
    fschat_openai_api_address(),
]

for address in addresses:
    # 提取主机名和端口号
    host = ":".join(address.split(":")[0:2])
    # 更新代理设置，这里设置为不使用代理
    default_proxies.update({host: None})
    

# 打印最终的代理设置
print(default_proxies)