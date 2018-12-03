__author__ = 'Korotkov Andrey'

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
n = int(input("Введите количество случайных чисел в списке: "))
list_numbers = []
for el in range(n):
    list_numbers.append(random.randint(-100, 100))
    print(list_numbers)
