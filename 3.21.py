#Павлов Арсений, задача 3.21

abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
print(c,b,a, sep='')