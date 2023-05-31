#Павлов Арсений, задача 28
d = int(input('рост в дюймах:'))
f = int(input('вес в футах:'))
sm = int(input('рост в см:'))
kg = int(input('вес в кг:'))
if d == 0 or f == 0: 
    print(kg/(sm**2))
else:
    print((f/(d**2))*703)