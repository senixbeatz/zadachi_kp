#Павлов Арсений, задача 33
a = int(input('введите число:'))
b = int(input('введите число:'))
c = int(input('введите число:'))
print(min(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(max(a, b, c))