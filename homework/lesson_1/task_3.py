# Напишите программу, которая принимает на вход координаты точки (X и Y), причем X и Y не равны 0, 
# и выдает номер четверти плоскости, в которой находится эта точка
# Пример
# x=34; y= -30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3

x = int(input('Введите координату x: '))
y = int(input('Введите координату y: '))

if (x == 0) or (y == 0):
    print('Ошибка ввода. X и Y не должны быть равные 0')
elif (x > 0) and (y > 0):
    print('Четерть плоскости I')
elif (x < 0) and (y > 0):
    print('Четерть плоскости II')
elif (x < 0) and (y < 0):
    print('Четерть плоскости III')
else:
    print('Четерть плоскости IV')