# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите положительное число: "))

def dec_to_two (num: int) -> int:
    two = 0
    pos = 1
    while num != 0:
        two += (num % 2) * pos
        pos *= 10
        num = num // 2
    return two

print (f"{number} -> {dec_to_two(number)}")