'''
os.environ['USER']:当前使用用户。
os.environ['LC_COLLATE']:路径扩展的结果排序时的字母顺序。
os.environ['SHELL']:使用shell的类型。
os.environ['LAN']:使用的语言。
os.environ['SSH_AUTH_SOCK']:ssh的执行路径。

'''
import os

print(os.environ.keys())


print(os.environ.get('USER'))   
# # os.environ['LC_COLLATE']
# # os.environ['SHELL']
# # os.environ['LAN']
# # os.environ['SSH_AUTH_SOCK']


os.environ['AGE']='18'         # 设置临时
print(os.environ.get('AGE'))    # 获取
print(os.environ.keys())        # 所有的环境变量的keys

answer = 'AGE' in os.environ    #  判断是否存在环境变量
print(answer)
