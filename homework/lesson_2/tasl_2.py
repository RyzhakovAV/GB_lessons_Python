# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
# Пример
# N = 4 -> [1, 2, 6, 24] (1, 1*2, 1*2*3, 1*2*3*4)

x = int(input("Please input digit: "))

def multiplication(digit):
    mult = [1]
    for i in range(1, digit):
        mult.append((i+1) * mult[i-1])
    return mult

print(multiplication(x))