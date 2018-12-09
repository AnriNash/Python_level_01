# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list_01 = ["apple", "banana", "pear", "lemon", "mango"]
fruit_list_02 = ["mandarin", "lemon", "pineapple", "kiwi", "apple"] # прям новогодний стол получается

dubl_list = [fruit for fruit in fruit_list_01 if fruit in fruit_list_02]
print(dubl_list)
