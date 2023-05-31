#Павлов Арсений, задача 4.54
abcd = int(input())
n = int(input())
a = (abcd % 10000) // 1000
b = (abcd % 1000) // 100
c = (abcd % 100) // 10
d = abcd % 10
if a == 4 or b == 4 or c == 4 or d == 4:
    print('в числе', abcd, 'есть цифра 4')
else:
    print('в числе', abcd, 'есть нет цифры 4')
if a == n or b == n or c == n or d == n:
    print('в числе', abcd, 'есть цифра', n)
else:
    print('в числе', abcd, 'есть нет цифры', n)