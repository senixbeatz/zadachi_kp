#Павлов Арсений, задача 3.30

n = int(input())
d = (n % 100) // 10
s = n // 100
if n > 99:
    print('число сотен', s, 'число десятков', d)
else:
    print('неверный формат числа')