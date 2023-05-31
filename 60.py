#Павлов Арсений, задача 60
from math import floor
a = int(input('введите год:'))
d = (a + floor((a-1)/4) - floor((a-1)/100) + floor((a-1)/400))%7
if d == 0:
    print('воскресенье')
elif d == 1:
    print('понедельник')
elif d == 2:
    print('вторник')
elif d == 3:
    print('среда')
elif d == 4:
    print('четверг')
elif d == 5:
    print('пятница')
elif d == 6:
    print('суббота')