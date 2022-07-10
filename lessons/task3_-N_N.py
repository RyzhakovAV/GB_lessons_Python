# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

N = int(input('Please, input digit N: '))
negativeN = -N

while negativeN <= N:
    print(negativeN, end=' ')
    negativeN += 1