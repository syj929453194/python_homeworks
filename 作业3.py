import random
import string

class DataSampling:
    def __init__(self):
        self.data = []

    def generate_data(self, data_type, data_num):
        if data_type == 'int':
            self.data.extend(random.sample(range(1, 100), data_num))
        elif data_type == 'float':
            self.data.extend([random.uniform(1, 100) for _ in range(data_num)])
        elif data_type == 'str':
            self.data.extend([''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 50))) for _ in range(data_num)])

    def get_data(self):
        return self.data


class MachineLearningMethods:
    def __init__(self, *args):
        self.methods = args

    def __call__(self, func):
        def wrapper(data):
            print("Performing machine learning operations:", ', '.join(self.methods))
            return func(data)
        return wrapper


class ValidationMetrics:
    def __init__(self, *args):
        self.metrics = args

    def __call__(self, func):
        def wrapper(data):
            print("Calculating validation metrics:", ', '.join(self.metrics))
            return func(data)
        return wrapper


# 调用示例
data_sampling = DataSampling()


@MachineLearningMethods('SVM', 'RF')
@ValidationMetrics('ACC', 'F1')
def process_random_data(data):
    print("Processing random data:", data)


data_sampling.generate_data('int', 5)
data_sampling.generate_data('float', 3)
data_sampling.generate_data('str', 4)
random_data = data_sampling.get_data()
process_random_data(random_data)
