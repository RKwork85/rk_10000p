import csv

# 创建CSV文件
with open('competition_scores.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # 写入标题行
    writer.writerow(["选手编号", "参数", "参数得分", "总得分"])
    
    # 假设选手编号和参数得分如下
    competitor_id = "001"
    scores = [90, 85, 88, 92, 87, 91, 84, 93]
    
    # 写入选手编号
    writer.writerow([competitor_id])
    
    # 写入每个参数和参数得分
    for i in range(8):
        writer.writerow(["", f"参数{i + 1}", scores[i]])
    
    # 写入总得分
    total_score = sum(scores)
    writer.writerow(["", "总得分", total_score])