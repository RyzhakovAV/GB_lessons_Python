#Напишите программу, которая принимает на вход два числаи проверяет,
#является ли одно число квадратом другого.
#Примеры
# - 5, 25 -> yes
# - 4, 16 -> yes
# - 25, 5 -> yes
# - 8, 9 -> no

a = int(input('Please. Input digit a: '))
b = int(input('Please. Input digit b: '))

if (a == b * b ) or (b == a * a):
    print('Yes')
else:
    print('No')