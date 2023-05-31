#Павлов Арсений, задача 3.25

abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
print(a,c,b, sep='')