#Павлов Арсений, задача 2.31 Известна стоимость 1 кг конфет, печенья и яблок. Найти стоимость всей покупки, если купили а: кг конфет, у кг печенья и z кг яблок.

a = int(input('стоимость кг конфет:' ))
b = int(input('стоимость кг печенья:' ))
c = int(input('стоимость кг яблок:' ))
x = int(input('сколько кг конфет:' ))
y = int(input('сколько кг печенья:' ))
z = int(input('сколько кг яблок:' ))
print('стоимость покупки равна', a*x + b*y + c*z)