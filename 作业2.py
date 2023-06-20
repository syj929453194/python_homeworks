import random
import string


def dataSampling():
    def decorator(func):
        def wrapper(*args):
            result = []
            for data_type, data_num in args:
                if data_type == 'int':
                    result.extend(random.sample(range(1, 100), data_num))
                elif data_type == 'float':
                    result.extend([random.uniform(1, 100) for _ in range(data_num)])
                elif data_type == 'str':
                    result.extend([''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 50))) for _ in range(data_num)])
            return func(result)
        return wrapper
    return decorator


def machineLearningMethods(*args):
    def decorator(func):
        def wrapper(data):
            # Perform machine learning operations using args
            print("Performing machine learning operations:", ', '.join(args))
            return func(data)
        return wrapper
    return decorator


def validationMetrics(*args):
    def decorator(func):
        def wrapper(data):
            # Perform validation metric operations using args
            print("Calculating validation metrics:", ', '.join(args))
            return func(data)
        return wrapper
    return decorator


# 调用示例
@dataSampling()
@machineLearningMethods('SVM', 'RF')
@validationMetrics('ACC', 'F1')
def processRandomData(data):
    print("Processing random data:", data)


processRandomData(('int', 5), ('float', 3), ('str', 4))
