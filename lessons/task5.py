# Напишите программу, которая будет принимать на вход дробь и показывать первую ифру дробной части числа
# Примеры
# 6,78 - 7
# 5 - нет
# 0,34 - 3

number = input('number = ')

for i in range(len(number)):
    if number[i] == ',':
        print(number[i+1])
        break

a = float(input('Input number: '))
b = int(a * 10)
print(b % 10)