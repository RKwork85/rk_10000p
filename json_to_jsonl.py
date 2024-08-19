import json

with open ('/home/rkwork/work_place/project/rk_datasets/rk_experiment/4_gz_company/refer_data/v0.json', mode='r') as f:
    data = json.load(f)
    print(len(data))

with open('./temp.jsonl', mode='w', encoding='utf-8') as f :
    for dataset in data:
        f.write(json.dumps(dataset, ensure_ascii =False) + '\n')