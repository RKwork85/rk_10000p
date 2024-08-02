result_eval_list = [0.4971766, 0.4971766, 0.4935614, 0.4935614, 0.4981848, 0.4943343, 0.4952008, 0.4536986]

sorted_list = sorted(result_eval_list)

# 初始化排名列表
rank = []

# 遍历原始列表，找到排序后的位置，并记录排名
for value in result_eval_list:
    rank.append(sorted_list.index(value)+1)

# 打印排名列表
print(result_eval_list)
print(sorted_list)

print(rank)