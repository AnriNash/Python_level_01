__author__ = 'Korotkov Andrey'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n,m):
    f1 = 1
    f2= 1
    i = 2
    fibonacci_sum1 = 0
    while i<=m:
        fibonacci_sum = f2 + f1
        f1 = f2
        f2 = fibonacci_sum
        i +=1
        if i == n-1:
            fibonacci_sum1 = fibonacci_sum
            return fibonacci_sum - fibonacci_sum1
        print(fibonacci(7,13))

