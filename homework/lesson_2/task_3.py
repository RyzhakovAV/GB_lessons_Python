# Задайте список из n чисел последовательностью $(1+\frac 1 n)^n$ и выведите на экран их сумму
# Пример
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Please, input digit: "))

def sequence (number):
    # Если честно, я не совсем понял формулу по заданию,
    # но судя по примеру прослеживается последовательность что каждое число увеличивается на 3
    seq = {0: 1}
    for index in range(1, number):
        seq[index] = seq[index-1]+3
    seq.pop(0)
    return seq

print(sequence(n))

