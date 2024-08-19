'''
字典按值排序： 我还得考虑有效没效
'''

# 创建一个字典
my_dict = {'apple': 10, 'orange': 20, 'banana': 5, 'grape': 15}

# 使用sorted()函数和lambda函数按值排序
# 这里我们返回一个元组列表，每个元组包含字典的键和值
sorted_items = sorted(my_dict.items(), key=lambda item: item[1])

print("按值排序的字典项：")

hhh = [item[1] for item in sorted_items]
print(hhh)

print(my_dict)


# 给定的列表
values = [0.4971766, 0.4971766, 0.4935614, 0.4935614, 0.4981848, 0.4943343, 0.4952008, 0.4536986]

# 使用字典推导式将列表转换为字典，其中索引作为键，列表元素作为值
index_value_dict = {index: value for index, value in enumerate(values)}

print(index_value_dict)

# 字典转换为列表
rank  = sorted(index_value_dict.items(), key=lambda item: item[1])
print(rank)

kkk = [(8, 0.4536986), (3, 0.4935614), (4, 0.4935614), (6, 0.4943343), (7, 0.4952008), (1, 0.4971766), (2, 0.4971766), (5, 0.4981848)]
for i in kkk:
    print(i[1])


# 给定的元组列表
tuples_list = [
    (8, 0.4536986), (3, 0.4935614), (4, 0.4935614),
    (6, 0.4943343), (7, 0.4952008), (1, 0.4971766),
    (2, 0.4971766), (5, 0.4981848)
]


"统计重复次数"
# 给定的元组列表
tuples_list = [
    (8, 0.4536986), (3, 0.4935614), (4, 0.4935614),
    (6, 0.4943343), (7, 0.4952008), (1, 0.4971766),
    (2, 0.4971766), (5, 0.4981848)
]

# 提取后三个元组的第二个元素
last_three_values = [t[1] for t in tuples_list[-3:]]

# 初始化计数器
value_counts = {val: 0 for val in last_three_values}

# 遍历所有元组，统计特定值的出现次数
for _, value in tuples_list:
    if value in value_counts:
        value_counts[value] += 1

# 输出结果
print("后三个元组中元素的出现次数：")
for value, count in value_counts.items():
    print(f"元素 {value} 出现了 {count} 次。")