#Павлов Арсений, задача 3.23

abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
print(b,c,a, sep='')