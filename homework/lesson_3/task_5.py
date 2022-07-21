# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

fibo_limit = int(input("Введите предел последовательности Фибоначчи: "))

fibo_list = []
for index in range(fibo_limit * 2 + 1):
    fibo_list.append(0)

fibo_list[fibo_limit-1] = 1
fibo_list[fibo_limit+1] = 1
sign = -1

for index in range(fibo_limit-1):
    fibo_list[fibo_limit + 2 + index] = fibo_list[fibo_limit+1+index]+fibo_list[fibo_limit+index]
    fibo_list[fibo_limit - 2 - index] = (sign**(index+1)*(abs(fibo_list[fibo_limit-1-index])
                                                          +abs(fibo_list[fibo_limit-index])))

print(fibo_list)