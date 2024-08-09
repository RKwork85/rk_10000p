from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses import dataclass
from typing import Optional

@dataclass
class HfTrainingArguments:
    output_dir: str = "default_output_dir"
    per_device_train_batch_size: int = 4
    per_device_eval_batch_size: int = 4
    evaluation_strategy: str = "epoch"
    learning_rate: float = 5e-5
    # 假设 __post_init__ 方法在 HfTrainingArguments 中定义了某些逻辑
    def __post_init__(self):
        print("HfTrainingArguments __post_init__ called")
        # 这里可以添加额外的初始化逻辑

@dataclass
class SwiftArgumentsMixin:
    save_only_model: bool = False
    train_sampler_random: bool = True
    push_hub_strategy: str = field(
        default='push_best',
        metadata={'choices': {'end', 'push_best', 'push_last', 'checkpoint', 'all_checkpoints'}}
    )
    acc_strategy: str = field(
        default='token', metadata={'choices': ['token', 'sentence']}
    )
    additional_saved_files: Optional[List[str]] = None

    def __post_init__(self):
        # 这里可以添加 SwiftArgumentsMixin 的初始化逻辑
        print("SwiftArgumentsMixin __post_init__ called")
        if self.additional_saved_files is None:
            self.additional_saved_files = []
        super().__post_init__()

@dataclass
class TrainingArguments(SwiftArgumentsMixin, HfTrainingArguments):
    pass  # 目前没有添加额外的字段或方法

# 创建 TrainingArguments 的实例
training_arguments = TrainingArguments(
    output_dir="./my_model_output",
    per_device_train_batch_size=8,
    evaluation_strategy="steps",
    learning_rate=3e-5,
    save_only_model=True,
    train_sampler_random=False,
    push_hub_strategy='push_last',
    acc_strategy='sentence',
    additional_saved_files=["config.json", "sample.txt"]
)

# 打印实例查看初始化结果
print(training_arguments)


class A:
    def __init__(self):
        print("Initializing A")
        super().__init__()

    def example_method(self):
        print("Method in A")

class B:
    def __init__(self):
        print("Initializing B")
        super().__init__()  # 这将调用 A 的 __init__ 方法，因为 B 继承自 A

    def example_method(self):
        print("Method in B")
        super().example_method()  # 这将调用 A 的 example_method 方法

class C(A, B):
    def __init__(self):
        print("Initializing C")
        super().__init__()  # 这将调用 B 的 __init__ 方法，因为 B 在 C 的类定义中排在 A 之后

    def __example_method__(self):
        print("Method in C")
        super().example_method()  # 这将调用 B 的 example_method 方法

c_instance = C()
# c_instance.example_method()


'''当 __post_init__() 方法在 SwiftArgumentsMixin 中被调用时，
super().__post_init__() 会尝试调用下一个基类的 __post_init__() 方法。按照MRO，
下一个基类是 HfTrainingArguments，所以 super().__post_init__() 将调用 HfTrainingArguments 中的 __post_init__() 方法。'''

'''
__post_init__ 方法并不是一个私有方法，但它也不是一个常规的公共方法。在Python中，方法名前的双下划线 (__) 通常表示该方法是特殊的或者受保护的，但这并不意味着它们是私有的。实际上，Python 中没有严格意义上的私有方法，因为理论上任何方法都可以被子类覆盖或在类外部被调用。

__post_init__ 方法是一个特殊方法，它遵循特定的约定：

特殊方法：它是由 dataclasses 模块定义的，用于在数据类的初始化过程之后执行额外的逻辑。
受保护：按照惯例，以单下划线 (_) 开头的方法被认为是受保护的，不应该被类外部直接调用。__post_init__ 虽然没有单下划线，但它的使用场景类似于受保护的方法，因为它是为特定目的设计的，而不是作为类的公共接口。
约定俗成：__post_init__ 方法遵循特定的使用约定，即在数据类的 __init__ 方法之后自动调用，而不是由用户显式调用。
总结来说，虽然 __post_init__ 不是一个私有方法，但它也不是用来作为公共接口的方法。它是一个按照特定约定使用的受保护的特殊方法，用于在数据类的初始化过程中执行后续逻辑。开发者应该遵循这个约定，不要从类的外部直接调用 __post_init__ 方法。


'''