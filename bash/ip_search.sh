#!/bin/bash

# 获取第一个活动的IPv4地址
ip_address=$(ip -4 addr show scope global | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | head -1)

# 检查是否找到了IP地址
if [ -z "$ip_address" ]; then
    echo "未找到IP地址。"
else
    echo "本地IP地址是：$ip_address"
fi