import os

# 设置文件夹路径
folder_path = '/home/rkwork/work_place/project/rk_llm/project/rk_python/other/contest_machine_review'

'''
B1001_03_02_sft_args.json
B1001_03_02_logging.jsonl

A1001_03_02_sft_args.json
A1001_03_02_logging.jsonl

'''
# 初始化列表
sft_args_paths = []
logging_paths = []

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件扩展名是否为 '.json'
    if filename.endswith('.json'):
        full_path = os.path.join(folder_path, filename)
        sft_args_paths.append(full_path)
    # 检查文件扩展名是否为 '.jsonl'
    elif filename.endswith('.jsonl'):
        full_path = os.path.join(folder_path, filename)
        logging_paths.append(full_path)

# 打印结果
print("sft_args_paths:", sft_args_paths)
print("logging_paths:", logging_paths)


