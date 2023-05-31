#Павлов Арсений, задача 4.79
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('треугольник существует')
else:
    print('треугольник не существует')