# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_number = [1.1, 1.2, 3.1, 5, 10.01]

def find_in_list(arr: list) -> float:
    minumum = 1
    maximum = 0
    for i in arr:
        if i % 1 < minumum:
            minumum = i % 1
        elif i % 1 > maximum:
            maximum = i % 1
        else:
            continue
    difference = maximum - minumum
    return difference

print(list_number)
print(f"Разница между максимальным и минимальным значением дробной части элементов = {find_in_list(list_number)}")
