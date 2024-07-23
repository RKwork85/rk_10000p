import os

class FileManager:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def collect_file_paths(self):
        sft_args_paths = []
        logging_paths = []

        # 遍历文件夹中的所有文件
        for filename in os.listdir(self.folder_path):
            # 检查文件扩展名是否为 '.json'
            if filename.endswith('.json'):
                full_path = os.path.join(self.folder_path, filename)
                sft_args_paths.append(full_path)
            # 检查文件扩展名是否为 '.jsonl'
            elif filename.endswith('.jsonl'):
                full_path = os.path.join(self.folder_path, filename)
                logging_paths.append(full_path)

        return sft_args_paths, logging_paths

    def print_paths(self):
        sft_args_paths, logging_paths = self.collect_file_paths()
        print("sft_args_paths:", sft_args_paths)
        print("logging_paths:", logging_paths)

# 使用示例
folder_path = "example/2024-07-18"
file_manager = FileManager(folder_path)
file_manager.print_paths()