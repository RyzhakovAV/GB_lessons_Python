# Напишите программу которая принимает на вход вещественное число и показывает сумму его.
# Пример
# 6782 -> 23
# 0,56 -> 11

x = input("Please. Input number: ")

def summa_digit_in_number(number):
    summa = 0
    for digit in number:
        if digit.isdigit():
            summa += int(digit)
    return summa

print(f"Сумма цифр в {x} равна = {summa_digit_in_number(x)}")