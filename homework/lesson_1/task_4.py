# Напишите программу, которая по заданному номеру четверти, показывает диапозон возможных координат точек в этой четверти
number = int(input('введите номер четверти от 1 до 4: '))

if (number < 1 or number > 4):
    print('Wrong input')
elif (number == 1):
    print('x от 0 до +∞  и y от 0 до +∞')
elif (number == 2):
    print('x от 0 до -∞ и y от 0 до +∞')
elif (number == 3):
    print('x от 0 до -∞ и y от 0 до -∞')
else:
    print('x от 0 до +∞ и y от 0 до -∞')