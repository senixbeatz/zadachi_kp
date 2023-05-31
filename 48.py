#Павлов Арсений, задача 48
m = input('введите месяц:')
d = int(input('введите день'))
if m == 'январь' or m == 'февраль':
    print('зима')
elif m == 'март':
    if d < 20:
        print('зима')
    else:
        print('весна')
elif m == 'апрель' or m == 'май':
    print('весна')
elif m == 'июнь':
    if d < 21:
        print('весна')
    else:
        print('лето')
elif m == 'июль' or m == 'август':
    print('лето')
elif m == 'сентябрь':
    if d < 22:
        print('лето')
    else:
        print('осень')
elif m == 'октябрь' or m == 'ноябрь':
    print('осень')
elif m == 'декабрь':
    if d < 21:
        print('осень')
    else:
        print('зима')

