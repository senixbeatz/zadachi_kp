#Павлов Арсений, задача 2.32 Известна стоимость монитора, системного блока, клавиатуры и мыши. Сколько будут стоить 3 компьютера из этих элементов?
a = int(input('стоимость монитора:'))
b = int(input('стоимость системного блока:' ))
c = int(input('стоимость клавиатуры:' ))
e = int(input('стоимость мыши:' ))
print('стоимость трех компьютеров:', 3*(a+b+c+e))
