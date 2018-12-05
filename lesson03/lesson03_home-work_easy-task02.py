__author__ = 'Korotkov Andrey'

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    if (len(str(ticket_number))!= 6) or (type(ticket_number) is not int):
        return 'Некорректный номер билета'
    else:
        ticket_number1 = list(str(ticket_number))
        sum1 = int(ticket_number1[0]) + int(ticket_number1[1]) + int(ticket_number1[2])
        sum2 = int(ticket_number1[3]) + int(ticket_number1[4]) + int(ticket_number1[5])
        if sum1 == sum2:
            return 'Билет %s счастливый' %ticket_number
        else:
            return 'Билет %s несчастливый' %ticket_number
number = int(input('Введите номер билета:'))
number = 123456
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
