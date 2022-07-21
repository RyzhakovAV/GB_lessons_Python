# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def fill_list(digit: int = 4) -> list:
    digits = []
    for i in range(0, digit):
        digits.append(random.randint(0, 10))
    return digits

def find_in_list (digits: list) -> list:
    multiplication = []
    i = 0
    while i <= (len(digits)-1) // 2:
        multiplication.append(digits[i] * digits[-i - 1])
        i += 1
    return multiplication


mul_list = (fill_list())
print(f"Сгенерированные числа: {mul_list}")
print(f"Произведение пар чисел: {find_in_list(mul_list)}")