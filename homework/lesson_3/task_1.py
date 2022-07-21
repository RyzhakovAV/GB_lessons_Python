# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def fill_list(digit: int = 20) -> list:
    digits = []
    for i in range(0, digit):
        digits.append(random.randint(0, 100))
    return digits

def sum_in_list (digits: list) -> int:
    pos_list = digits[1::2]
    x = 0
    for i in pos_list:
        x += i
    return x

mul_list = (fill_list())
print(f"Сгенерированные числа: {mul_list}")
print(f"Сумма чисел: {sum_in_list(mul_list)}")