__author__ = 'Korotkov Andrey'

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
# (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
# (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# дата = '01.11.1985'

# Примеры некорректных дат
# дата = '01.22.1001'
# дата = '1.12.1001'
# дата = '-2.10.3001'

data = input("введите дату, разделяя точкой: ")
converted_data = data.split(".")
converted_day = int(converted_data[0])
converted_month = int(converted_data[1])
converted_year = int(converted_data[2])
long_mounth = [1, 3, 5, 7, 8, 10, 12]
if len(converted_data[0]) != 2 or len(converted_data[1]) != 2 or len(converted_data[2])!= 4:
    print("Формат даты введен не корректно")
elif converted_day > 31 or converted_day < 1:
    print("День указан не корректно")
elif converted_month > 12 or converted_month < 1:
    print("Месяц указан не корректно")
elif converted_year > 9999 or converted_year < 1:
    print("Год указан не корректно")
elif converted_month not in long_mounth and converted_day > 30:
    print("День указан не корректно")
else:
    print("Дата казана корректно:", data)
