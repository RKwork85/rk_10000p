import re

# 原始字符串

# 要匹配的模式
pattern = r"广东众承教育科技股份有限公司"

# 替换的目标字符串
replacement = "我们公司"

# 使用re.sub()进行替换
# modified_string = re.sub(pattern, replacement, original_string)

import json

with open ('/home/rkwork/work_place/project/rk_llm/project/rk_python/other/tempp.json', mode='r') as f:
    data = json.load(f)
    print(len(data))

with open('./ttt.jsonl', mode='w', encoding='utf-8') as f :
    for dataset in data:
        dataset['output']= re.sub(pattern, replacement, dataset['output'],count=1)

        f.write(json.dumps(dataset, ensure_ascii =False) + '\n')