#Павлов Арсений, задача 41
a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print('треугольник равносторонний')
elif a == b or a == c or b == c:
    print('треугольник равнобедренный')
else:
    print('треугольник равносторонний')