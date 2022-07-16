# Реализуйте алгоритм перемешивания списка.

import random

def fill_list(number):
    fill_list = []
    for i in range(number):
        fill_list.append(i)
    return fill_list

def change_list(arr):
    for i in range(len(arr)-1, -1, -1):
        j = random.randint(0, len(arr)-1)
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
    return arr

N = int(input("Please, input digit: "))
mul_list = fill_list(N)

print(mul_list)
print(change_list(mul_list))