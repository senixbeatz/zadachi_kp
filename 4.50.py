#Павлов Арсений, задача 4.50
num = int(input())
num1 = num // 10
num2 = num % 10
if num1 == 4 or num2 == 4 or num1 == 7 or num2 == 7:
    print('в него входит цифра 4 или 7')
else:
    print('не входит')
if num1 == 3 or num2 == 3  or num1 == 6 or num2 == 6 or num1 == 9 or num2 == 9:
    print('в него входит цифра 3, 6 или 9')
else:
    print('не входит')
