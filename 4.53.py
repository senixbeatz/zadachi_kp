#Павлов Арсений, задача 4.53
abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
if a == 4 or b == 4 or c == 4 or a == 7 or b == 7 or c == 7:
    print('в него входит цифра 4 или 7')
else:
    print('не входит')
if a == 3 or b == 3 or c == 3 or a == 6 or b == 6 or c == 6 or a == 9 or b == 9 or c == 9:
    print('в него входит цифра 3, 6 или 9')
else:
    print('не входит')
