__author__ = 'Korotkov Andrey'

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


first_list = [2,4,6,8,15,19,32]
new_list = []
last_name = len(first_list)
for i in range(last_name):
    if first_list[i] % 2 == 0:
        new_list.append(first_list[i]/4)
    else:
        new_list.append(first_list[i]*2)
        print(new_list)
