#Павлов Арсений, задача 4.28
ab = int(input())
a = ab // 10
b = ab % 10
if  a + b > 9:
    print('сумма цифр заданного числа является двузначным числом')
elif  a + b > ab:
    print('сумма цифр больше заданного числа')