import os

# 默认代理设置的字典
default_proxies = {}

# 更新代理设置的代码
default_proxies.update({
    "http://": os.environ.get("http_proxy"),
    "https://": os.environ.get("https_proxy"),
    "all://": os.environ.get("all_proxy"),  # 由于没有设置，这将返回None
})

# 打印最终的代理设置
print("Default Proxies:")
for protocol, proxy in default_proxies.items():
    print(f"{protocol}: {proxy}")

# export http_proxy=http://192.168.1.100:8080
# export https_proxy=https://192.168.1.101:8443
# python your_script.py