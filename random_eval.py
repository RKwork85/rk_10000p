import random
import json


start = 0
end = 50
with open('temp.jsonl', 'r') as f:     

    # data = json.load(f)             # 处理json格式
    data = [json.loads(line) for line in f]

with open('temp_eval.jsonl', 'w', encoding='utf-8') as f:

    for number in range(20):
        for item in range(10):
            # query = item['instruction']
            random_number = random.randint(start, end)
            print(f"生成的随机数是: {random_number}")
            f.write(json.dumps(data[random_number], ensure_ascii= False ) + '\n')
        
        start += 50
        end  += 50
        


print(end)
