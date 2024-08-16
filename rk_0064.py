import os

KB_ROOT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge_base") 
if not os.path.exists(KB_ROOT_PATH):
    os.mkdir(KB_ROOT_PATH)


file_path = './other/filePath/.kkk.txt'
if not os.path.isdir(os.path.dirname(file_path)):
    os.makedirs(os.path.dirname(file_path))


def get_kb_path(knowledge_base_name: str):
    return os.path.join(KB_ROOT_PATH, knowledge_base_name)


def list_kbs_from_folder():
    return [f for f in os.listdir(KB_ROOT_PATH)
            if os.path.isdir(os.path.join(KB_ROOT_PATH, f))]