#Павлов Арсений, задача 36
n = int(input('введите возраст собаки:'))
if n == 1:
    print('10.5 человеских лет')
elif n == 2:
    print('21 человеский год')
elif n > 2:
    print(21 + (n-2)*4, 'человеческих лет')
elif n < 0:
    print('вы ввели отррицательное число')