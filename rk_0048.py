from enum import Enum

class MESSAGES(str, Enum):
    DEFAULT = lambda msg="": f"{msg if msg else ''}"
    MODEL_ADDED = lambda model="": f"The model '{model}' has been added successfully."
    MODEL_DELETED = lambda model="": f"The model '{model}' has been deleted successfully."

# 使用 DEFAULT 消息
print(MESSAGES.DEFAULT())  # 输出: ''
print(MESSAGES.DEFAULT("Hello, world!"))  # 输出: 'Hello, world!'

# 使用 MODEL_ADDED 消息
print(MESSAGES.MODEL_ADDED())  # 输出: 'The model '' has been added successfully.'
print(MESSAGES.MODEL_ADDED("MyModel"))  # 输出: 'The model 'MyModel' has been added successfully.'

# 使用 MODEL_DELETED 消息
print(MESSAGES.MODEL_DELETED())  # 输出: 'The model '' has been deleted successfully.'
print(MESSAGES.MODEL_DELETED("MyModel"))  # 输出: 'The model 'MyModel' has been deleted successfully.'