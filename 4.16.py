#Павлов Арсений, задача 4.16
from math import sqrt
a = int(input())
b = int(input())
c = int(input())
d = b**2 - 4*a*c 
x1 = (-b + sqrt(d))/2*a 
x2 = (-b - sqrt(d))/2*a 
if d > 0:
    print(x1, x2)
elif d < 0:
    print('уравнение не имеет корней')

