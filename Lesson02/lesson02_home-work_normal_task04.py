__author__ = 'Korotkov Andrey'

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 11, 13, 67, -23, 77, 99, 90, 190, 750]
new_list = set(list)
print(new_list)

