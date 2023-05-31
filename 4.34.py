#Павлов Арсений, задача 4.34
abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
if a == b == c:
    print('все его цифры одинаковы')
else:
    print('цифры не одинаковы')
if a == b or b == c or a == c:
    print('две его цифры одинаковы')
else:
    print('цифры не одинаковы')