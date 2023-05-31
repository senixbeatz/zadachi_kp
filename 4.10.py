#Павлов Арсений, задача 4.10
km = int(input())
ft = int(input())
if (ft * 0.3048 * 1000) < km:
    print(f"{ft} футов меньше, чем {km} км")
else:
    print(f"{km} км меньше, чем {ft} футов")
