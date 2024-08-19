import json

with open ('/home/rkwork/work_place/project/rk_datasets/ttt.jsonl', mode='r') as f:
    data = [json.loads(line) for line in f]


with open('./temp.json', mode='w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)