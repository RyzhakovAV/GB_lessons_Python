# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# -1, 4, 8, 7, 5 -> 8

num0 = int(input('Please. Input digit 1: '))
i = 2

while i <= 5:
    num1 = int(input(f'Please. Input digit {i}: '))
    i+=1
    if (num1 > num0):
        num0 = num1

print(f'Максимально введенное число: {num0}')