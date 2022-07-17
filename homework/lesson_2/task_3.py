# Задайте список из n чисел последовательностью (1+1/n)**n и выведите на экран их сумму
# Пример
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Please, input digit: "))

def sequence (number: int):
    seq = []
    for index in range(1, number+1):
        seq.append((1 + 1 / index) ** index)
    return seq

sum_list = sum(sequence(n))
print(round(sum_list, 0))

