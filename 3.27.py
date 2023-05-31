#Павлов Арсений, задача 3.27

abcd = int(input())
d = abcd % 10
c = (abcd % 100) // 10
b = (abcd % 1000) // 100
a = (abcd % 10000) // 1000
s = a + b + c + d
print(s)