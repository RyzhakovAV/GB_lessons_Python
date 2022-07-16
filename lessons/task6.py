# Напишите программу,которая принимает на вход число N
# и выдает последовательность из N членов
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

N = int(input("Введите число N: "))
number = 1

def digits_pow (arg1: int, arg2: int):
    i = 1
    print(arg2, end=', ')
    while i < arg1:
        i += 1
        arg2 *= -3
        if i != arg1:
            print(arg2, end=', ')
        else:
            print(arg2)

def list_from(numbers: int):  #пример с группы
    list_numbers = []
    for element in range(0, numbers):
        list_numbers.append((-3)**element)
    return list_numbers

print(list_from(N))
digits_pow(N, number)
