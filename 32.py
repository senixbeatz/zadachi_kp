#Павлов Арсений, задача 32
abcd = int(input('введите число'))
d = abcd % 10
c = (abcd % 100) // 10
b = (abcd % 1000) // 100
a = (abcd % 10000) // 1000
s = a + b + c +d 
print(a, '+', b, '+', c, '+', d, '=', s)
