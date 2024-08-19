import json

# 创建一个列表，用于存储所有的数据条目
data_list = []

# 填充列表，生成10条数据
for i in range(10):
    participant_number = f"A{1004 + i}"
    score = 0
    data_list.append({
        "participant_number": participant_number,
        "score": score
    })

# 将数据写入JSON文件
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent=4)

print("JSON文件已生成。")