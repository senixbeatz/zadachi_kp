#Павлов Арсений, задача 12
t1 = float(input('широта первой точки'))
g1 = float(input('долгота первой точки'))
t2 = float(input('широта второй точки'))
g2 = float(input('долгота второй точки'))
from math import pi, acos, sin, cos
t1 = t1 * pi / 180
g1 = t1 * pi / 180
t2 = t1 * pi / 180
g2 = t1 * pi / 180
print('расстояние между этими точками равно', 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2)))