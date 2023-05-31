#Павлов Арсений, задача 3.19

abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
print(a,b,c, sep=',')