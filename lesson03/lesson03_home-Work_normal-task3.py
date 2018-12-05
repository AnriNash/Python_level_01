# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_function(func,iterable):
    output_iterable = []
    for i in range(len(iterable)):
        if func(iterable[i]) == True:
            output_iterable.append(iterable[i])
            return output_iterable
func = lambda x: type(x) == str
iterable = [-1, 2, 'a', 4, 'fgf']
print(filter_function(func, iterable))
