'''
对于官方函数的补丁

重写函数的方法！！！
'''
import json  
  
# 保存原始的 json.dumps 函数  
_original_json_dumps = json.dumps  
  
# 定义一个新函数，它包装了原始的 json.dumps 并默认禁用 ensure_ascii  
def custom_json_dumps(obj, **kwargs):  
    # 如果 kwargs 中没有指定 ensure_ascii，则默认设置为 False  
    if 'ensure_ascii' not in kwargs:  
        kwargs['ensure_ascii'] = False  
    return _original_json_dumps(obj, **kwargs)  
  
# 使用示例  
if __name__ == "__main__":  
    data = {"name": "张三", "age": 30, "city": "上海"}  
      
    # 使用原始的 json.dumps  
    print("原始 json.dumps 输出（确保 ASCII）:")  
    print(_original_json_dumps(data))  
      
    # 使用自定义的 custom_json_dumps  
    print("\n自定义 custom_json_dumps 输出（禁用 ASCII）:")  
    print(custom_json_dumps(data))  
  
    # 如果你仍然想在某些情况下使用原始的 ensure_ascii=True，可以这样做：  
    print("\n使用自定义函数，但强制 ensure_ascii=True:")  
    print(custom_json_dumps(data, ensure_ascii=True))