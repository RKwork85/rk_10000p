'''
字典的设置和遍历

'''

def make_request(url, **kwargs):
    print(f"Making request to {url}")
    print("Request options:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    # 这里可以添加实际的请求逻辑


# 定义一些默认的请求选项
default_timeout = 30  # 超时时间30秒
default_proxies = {
    "http": "http://proxyserver:8080",
    "https": "https://proxyserver:8080"
}

# 创建一个空字典来存储额外的关键字参数
kwargs = {}

# 更新 kwargs 字典，添加默认的超时时间和代理设置
kwargs.update(timeout=default_timeout, proxies=default_proxies)
print("hhhhhhhhhhhhh", kwargs)

# 调用函数，使用 **kwargs 来传递所有关键字参数
make_request("http://example.com", **kwargs)


