# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
import re

with open('mytask03.doc', 'w') as my_file:
    for _ in range(2500):
        my_file.write(str(random.randint(0, 9)))
with open('mytask03.doc', 'r') as my_file:
    longest_sequences = list()
    huge_number = my_file.read()
    print(huge_number)
    for number in range(0, 10):
        if str(number) in huge_number:
            lst = re.findall('[%s]+' % number, huge_number)
            longest_sequences.append(max(lst, key=len))
    result = max(longest_sequences, key=len)
    print(result)