import os

def collect_file_paths(directory):
    logging_paths = []
    sft_args_paths = []

    # 遍历指定目录
    for filename in os.listdir(directory):
        if filename.endswith('_logging.jsonl'):
            logging_paths.append(os.path.join(directory, filename))
        elif filename.endswith('_sft_args.json'):
            sft_args_paths.append(os.path.join(directory, filename))

    return logging_paths, sft_args_paths

# 指定目录路径
directory_path = '/home/rkwork/work_place/project/rk_llm/project/rk_python/other/contest_machine_review'

# 收集文件路径
logging_paths, sft_args_paths = collect_file_paths(directory_path)

# 打印结果
print("Logging Paths:")
for path in logging_paths:
    print(path)

print("\nSFT Args Paths:")
for path in sft_args_paths:
    print(path)