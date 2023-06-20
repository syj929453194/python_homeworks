import random
import string

def dataSampling(**kwargs):
    result = []
    for data_type, data_num in kwargs.items():
        if data_type == 'int':
            result.extend(random.sample(range(1, 100), data_num))
        elif data_type == 'float':
            result.extend([random.uniform(1, 100) for _ in range(data_num)])
        elif data_type == 'str':
            result.extend([''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 50))) for _ in range(data_num)])
    return result


# 调用示例
random_data = dataSampling(int=5, float=3, str=4)
print(random_data)
