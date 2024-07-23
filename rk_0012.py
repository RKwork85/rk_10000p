import json

class ContestEvaluator:
    def __init__(self, sft_args_paths, logging_paths):
        self.sft_args_paths = sft_args_paths
        self.logging_paths = logging_paths
        self.params = None
        self.global_step = None
        self.eval_loss = None
        self.eval_acc = None
        self.total_scores = []

    def load_params(self, sft_args_path):
        with open(sft_args_path, mode='r') as f:
            self.params = json.load(f)

    def load_logging(self, logging_path):
        with open(logging_path, mode='r') as f:
            logs = [json.loads(line) for line in f]
            self.global_step = logs[-1]['global_step']
            self.eval_loss = logs[-3]['eval_loss']
            self.eval_acc = logs[-3]['eval_acc']

    def evaluate_params(self):
        self.dataset_test_ratio_score = 1 if self.params['dataset_test_ratio'] == 0.3 else 0
        self.batch_size_score = 1 if self.params['batch_size'] == 1 else 0

        self.num_train_epochs_score = 1 if self.params['num_train_epochs'] in [10, 20, 25] else 0
        self.gradient_accumulation_steps_score = 1 if self.params['gradient_accumulation_steps'] in [14, 28, 30] else 0
        self.eval_steps_score = 1 if self.params['eval_steps'] in [100, 50, 40] else 0

        groupA_args = [
            [10, 14, 100],
            [20, 28, 50], 
            [25, 30, 40]
        ]

        self.group_args = [self.params['num_train_epochs'], self.params['gradient_accumulation_steps'], self.params['eval_steps']]
        self.group_args_score = 3 if self.group_args in groupA_args else 0

        self.global_step_score = 2 if self.global_step == 1000 else 0

    def calculate_total_score(self):
        total_score = (self.dataset_test_ratio_score + self.batch_size_score + self.num_train_epochs_score + 
                        self.gradient_accumulation_steps_score + self.eval_steps_score + self.group_args_score + self.global_step_score) * 1.2
        return total_score

    def evaluate_all(self):
        for sft_args_path, logging_path in zip(self.sft_args_paths, self.logging_paths):
            self.load_params(sft_args_path)
            self.load_logging(logging_path)
            self.evaluate_params()
            total_score = self.calculate_total_score()
            self.total_scores.append(total_score)
            print(f"文件 {sft_args_path} 的最终得分：{total_score}")
            print(f"eval_acc: {self.eval_acc}, eval_loss: {self.eval_loss}")

# 使用示例
sft_args_paths = [
    '/home/rkwork/work_place/project/rk_llm/project/rk_python/other/contest_machine_review/sft_args1.json',
    '/home/rkwork/work_place/project/rk_llm/project/rk_python/other/contest_machine_review/sft_args2.json',
    # 更多文件路径
]
logging_paths = [
    '/home/rkwork/work_place/project/rk_llm/project/rk_python/other/contest_machine_review/logging1.jsonl',
    '/home/rkwork/work_place/project/rk_llm/project/rk_python/other/contest_machine_review/logging2.jsonl',
    # 更多文件路径
]

evaluator = ContestEvaluator(sft_args_paths, logging_paths)
evaluator.evaluate_all()