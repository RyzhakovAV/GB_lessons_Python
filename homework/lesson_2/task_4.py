# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции пользователь задает через пробел одной строкой.

import random
def randomi (digit: int)  -> list:
    digits = []
    for i in range(digit):
        digits.append(random.randint(-digit, digit))
    return digits

def input_position() -> list:
    pos = input("Пожалуйста введите индексы через пробел: ").split()
    pos_list = [int(i) for i in pos]
    return pos_list


def multiplication (arr: list, mult: list) -> int:
    multi = 1
    for i in range(0, len(arr)):
        multi *= mult[arr[i]]
    return multi

N = int(input("Please, input digit: "))

mul_list = (randomi(N))
print(f"Сгенерированные числа: {mul_list}")
position_list = input_position()
print(f"Выбранные индексы: {position_list}")
print(f"Сгенерированные числа: {mul_list}")
print(f"Произведение чисел по выбранным позициям равна = {multiplication(position_list, mul_list)}")