#Павлов Арсений, задача 4.80
a = int(input())
b = int(input())
c = int(input())
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print('треугольник прямоугольный')
else:
    print('непрямоугольный')