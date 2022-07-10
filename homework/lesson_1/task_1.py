# Напишите программу, которая принимает на вход цифру, обозначающая день недели, и проверяет. является ли этот день выходным.
# Пример:
# - 6 --> yes
# - 7 --> yes
# - 1 --> no

day = int(input('Введите день недели: '))

if day < 1 or day > 7:
    print('Input wrong')
elif day == 6 or day == 7:
    print('This is weekend')
else:
    print('Excuse me, this is a work day')