import random
import time

# определение функии которая генерирует случайное число
def random_num(min_val, max_val):
    return random.randint(min_val, max_val)

# определяем функцию которая запускает алгоритм
def emergent_algorithm():
    max_val = random_num(1, 10)
    for i in range(1000):
        random_num(1, 5)  # генерируем рандомные числа
        max_val = max(max_val, random_num(1, 5))

    print("максимальное значение равно", max_val)

# принтим результат
emergent_algorithm()