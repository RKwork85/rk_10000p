import sys
import os


new_path = sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# print(sys.path)       
from config import AGE
print(new_path)           # 默认的返回值为none,返回值没有意义，修改了sys.path[]的列表
print(AGE)