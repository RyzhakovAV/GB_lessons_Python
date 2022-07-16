# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
def randomi (digit):
    digits = []
    for i in range(digit):
        digits.append(random.randint(-digit, digit))
    return digits

N = int(input("Please, input digit: "))
Position = int(input("Please, input index: "))

mul_list = (randomi(N))

print(mul_list)
if Position >= len(mul_list):
    print("Индекс уходит за границу списка")
else:
    print(mul_list[Position])