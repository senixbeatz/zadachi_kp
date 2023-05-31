#Павлов Арсений, задача 3.28

abcd = int(input())
d = abcd % 10
c = (abcd % 100) // 10
b = (abcd % 1000) // 100
a = (abcd % 10000) // 1000
print(d,c,b,a, sep='')
print(b,a,d,c, sep='')
print(a,c,b,d, sep='')
print(c,d,a,b, sep='')