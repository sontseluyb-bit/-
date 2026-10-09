import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Функція '{func.__name__}' виконана за {execution_time:.6f} секунд")

        return result

    return wrapper

@timer_decorator
def test_fast():
    return sum(range(100000))


@timer_decorator
def test_sleep():
    a = 2 ** 952436727  # смажить ПК
    return "Пауза завершена"


@timer_decorator
def test_args(a, b):
    time.sleep(0.5)
    return a * b


# 3. Запуск тестів
if __name__ == "__main__":
    print("------ Запуск тестів ------")

    res1 = test_fast()
    print("результат 1:", res1)
    print("-" * 30)

    res2 = test_sleep()
    print("Результат 2:", res2)
    print("-" * 30)

    res3 = test_args(5, 10)
    print("Результат 3:", res3)
