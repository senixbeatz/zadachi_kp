#Павлов Арсений, задача 4.59
a = int(input())
b = int(input())
c = int(input())
if a == b or a == c or b == c:
    print('треугольник равнобедренный')
elif a == b and a == c and b == c:
    print('треугольник равносторонний')
    