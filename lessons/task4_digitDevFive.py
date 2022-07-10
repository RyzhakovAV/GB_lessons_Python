#Напишите программу, которая принимает на вход число и проверяет,
#кратно ли оно 5 и 10 или 15, но не 30

number = int(input('Please, input digit: '))

if (number % 30 == 0):
    print('Число кратно 30')
elif (number % 5 == 0 and number % 10 == 0) or (number % 15 == 0):
    print('Число кратно 5, 10 или 15')
else:
    print('Число не кратно 5, 10 или 15')