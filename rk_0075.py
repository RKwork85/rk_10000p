

aim = [(8, [0.4536986, False]), (3, [0.4935614, True]), (4, [0.4935614, True]), (6, [0.4943343, True]), (7, [0.4952008, True]), (1, [0.4971766, False]), (2, [0.4971766, True]), (5, [0.4981848, True])]
# 定义一个字典来存储统计结果

# aimList = [v[0] for i,v in aim]

# print(aimList)
unique_list = list(dict.fromkeys([v[0] for i,v in aim]))

print(unique_list)

result_dic = {  value: index + 1 for index, value in enumerate(unique_list[:3])}
print(result_dic)

for i in aim:
    if i[1][0] in result_dic:
        print(result_dic[i[1][0]]) 