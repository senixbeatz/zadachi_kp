#Павлов Арсений, задача 4.14
r1 = int(input())
u1 = int(input())
r2 = int(input())
u2 = int(input())
if u1/r1 < u2/r2:
    print('напряжение первого участка меньше')
else:
    print('напряжение первого участка больше')