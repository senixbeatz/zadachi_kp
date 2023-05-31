#Павлов Арсений, задача 4.47

a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    print('неравенство выполняется')
elif b > a > c:
    print('неравенство выполняется')
else:
    print('неравенство не выполняется')