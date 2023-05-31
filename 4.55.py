#Павлов Арсений, задача 4.55
abcd = int(input())
a = (abcd % 10000) // 1000
b = (abcd % 1000) // 100
c = (abcd % 100) // 10
d = abcd % 10
if a == 2 or b == 2 or c == 2 or d == 2 or a == 7 or b == 7 or c == 7 or d == 7:
    print('в числе', abcd, 'есть цифра 2 или 7')
else:
    print('в числе', abcd, 'есть нет цифры 2 или 7')
if a == 3 or b == 3 or c == 3 or d == 3 or a == 6 or b == 6 or c == 6 or d == 6 or a == 9 or b == 9 or c == 9 or d == 9:
    print('в числе', abcd, 'есть цифра 3, 6 или 9')
else:
    print('в числе', abcd, 'есть нет цифры 3, 6 или 9')