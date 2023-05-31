#Павлов Арсений, задача 3.24

abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
print(b,a,c, sep='')