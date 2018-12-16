# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class People:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname


class Staff_list(People):
    def __init__(self, name, surname, payment, position, norm_hours):
        People.__init__(self, name, surname)
        self._payment = payment
        self._position = position
        self._norm_hours = norm_hours


class Real_hours(People):
    def __init__(self, name, surname, real_hours):
        People.__init__(self, name, surname)
        self.real_hours = real_hours


f_1 = open('data/workers', 'r', encoding='UTF-8')
str_lst_1 = f_1.readlines()
i = 1
while i in range(len(str_lst_1)):
    People.name, People.surname, Staff_list.payment, Staff_list.position, Staff_list.norm_hours = str_lst_1[
        i].split()
    i += 1
# По идее эта часть долна считать из строк файла данные в классы

f_1 = open('data/hours_of', 'r', encoding='UTF-8')
str_lst_2 = f_1.readlines()
k = 1
while k in range(len(str_lst_2)):
    Staff_list.name, Staff_list.surname, Real_hours.real_hours = str_lst_2[k].split()
    k += 1