'''
海象表达式
环境变量可以是 一个字符串以固定标志分隔：export no_proxy="localhost,127.0.0.1,example.com, aaa,    "
在读取时使用split('')改变为 数组
'''
import os

# 假设的 default_proxies 字典
default_proxies = {}

# 检查 no_proxy 环境变量，如果有，更新 default_proxies 字典
no_proxy_hosts = os.environ.get("no_proxy", "").split(",")

print(no_proxy_hosts)
for host in no_proxy_hosts:
    # 使用海象运算符在条件表达式中处理空白
    if (processed_host := host.strip()):        # 如果 经过函数处理赋值给变量后 不为空 则执行相应逻辑 
        # 更新 default_proxies 字典，指示不应使用代理
        default_proxies[f'all://{processed_host}'] = None
    
    if isinstance(proxies, str):        
        proxies = {"all://": proxies}

    if isinstance(proxies, dict):
        default_proxies.update(proxies)     ## 添加字典方式

# 打印结果
print("Default Proxies Configuration:")
for host, proxy in default_proxies.items():
    print(f"{host}: {proxy}")
