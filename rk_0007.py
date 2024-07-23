'''
A卷
1 验证集拆分比例为30%；             1               //  固定值对即可得分
6 权重更新的样本量为1               1               //  固定值对即可得分

       训练轮数     梯度累计      交叉验证步数

case1:   10、        14、          100
case2:   20、        28、          50
case3:   25、        30、          40

--梯度累计不大于40  训练轮数不少于10--


gradient_accumulation_steps_box:[14,28,30]
num_train_epochs_box: [10,20,25]
train_box:[10,20,25]
eval_steps_box: [100, 50, 40]




2 训练轮数不少于10轮；              2               // 在正确范围内得1分 
4 交叉验证要求训练一轮验证一次；      2               // 在正确范围内得1分
5 梯度累计不大于40； case:          2              // 在正确范围内得1分
                                                // 一组设置正确的3分

3 总计步长为1000；                 2              //  文件中步长等于1000 对即可得分

--------------------------------------------------------------------------------------------
B卷
1 使用提供的验证集；                1
6 权重更新的样本量为1               1

       训练轮数     梯度累计      交叉验证步数
case1: 10、         5、         200
case2: 16、         8、         125
case3: 20、         10、        100

--梯度累计不大于20  训练轮数不少于10--


2训练轮数不少于10轮；               2
3 总计步长为2000；                 2
4 交叉验证要求训练一轮验证一次；      2
5 梯度累计不大于20；                2

数据分为两个部分：

1 评分数据
2 可视化数据
'''
gradient_accumulation_steps_box=[14,28,30]
num_train_epochs_box= [10,20,25]
eval_steps_box= [100, 50, 40]


## score
dataset_test_ratio_score = None
batch_size_score = None

num_train_epochs_score = None
gradient_accumulation_steps_score = None
eval_steps_score = None
group_args_score = None


file_path = '/home/rkwork/work_place/project/rk_llm/project/rk_python/other/contest_machine_review/sft_args.json'

with open (file_path, mode='r') as f:
    import json
    params = json.load(f)

def is_new_case_in_cases(new_case, cases):
    return new_case in cases


for key, value in params.items():
    print(f"{key}: {value}")

print('*******选手参数设置评分*******')

# 第一阶段：固定参数值评分

if params['dataset_test_ratio'] == 0.3:
    print(f"验证集拆分比例为:{params['dataset_test_ratio']}", "Score: 1")
else:
    print(f"验证集拆分比例为:{params['dataset_test_ratio']}", "Score: 0")

if params['batch_size'] == 1:
    print(f"batch_size:{params['batch_size']}", "Score: 1")
else:
    print(f"batch_size:{params['batch_size']}", "Score: 0")

# 第二阶段：一组参数值评分

if params['num_train_epochs'] in num_train_epochs_box:
    print(f"num_train_epochs:{params['num_train_epochs']}", "Score: 1")
else:
    print(f"num_train_epochs:{params['num_train_epochs']}", "Score: 0")

if params['gradient_accumulation_steps'] in gradient_accumulation_steps_box:
    print(f"gradient_accumulation_steps:{params['gradient_accumulation_steps']}", "Score: 1")
else:
    print(f"gradient_accumulation_steps:{params['gradient_accumulation_steps']}", "Score: 0")

if params['eval_steps'] in eval_steps_box:
    print(f"eval_steps:{params['eval_steps']}", "Score: 1")
else:
    print(f"eval_steps:{params['eval_steps']}", "Score: 0")

# 第三阶段：组参数值评分全部正确奖励

groupA_args =[
    [10, 14, 100],
    [20, 28, 50], 
    [25, 30, 40]
]

group_args = [params['num_train_epochs'],params['gradient_accumulation_steps'], params['eval_steps'] ]
print(group_args)

print('group_args_score:3' if is_new_case_in_cases(group_args, groupA_args) else 'group_args_score:0')



## global_step 评分

logging_file = '/home/rkwork/work_place/project/rk_llm/project/rk_python/other/contest_machine_review/logging.jsonl'
with open(logging_file, mode='r') as f:
    import json 
    params = [json.loads(line) for line in f ]
    global_step = params[-1]['global_step']

if global_step == 1000 :
    global_step_score = 2
    print(f"eval_steps:{global_step}", "Score: 2")
else:
    print(f"eval_steps:{global_step}", "Score: 0")




total_score = dataset_test_ratio_score + batch_size_score + num_train_epochs_score + gradient_accumulation_steps_score + eval_steps_score+group_args_score + global_step_score
print(total_score)
