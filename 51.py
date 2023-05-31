#Павлов Арсений, задача 51
from math import sqrt
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
d = b**2 - 4*a*c 
d1 = (-b + sqrt(d))/(2*a)
d2 = (-b - sqrt(d))/(2*a)
if d < 0:
    print('нет корней')
elif d == 1:
    print('имеется один корень - ', d1)
else:
    print('имеется два корня - ', d1, 'и', d2)