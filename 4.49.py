#Павлов Арсений, задача 4.49
num = int(input())
a = int(input())
num1 = num // 10
num2 = num % 10
if num1 == 3 or num2 == 3:
    print('в него входит цифра три')
elif num1 == a or num2 == a:
    print('в него входит цифра', a)
else:
    print('не входит')
