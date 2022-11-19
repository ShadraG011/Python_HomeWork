# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
size = int(input("Введите размер списка: "))

def get_list(size):
    list = []
    for _ in range(0, size):
        list.append(random.randint(1, 11))
    return list

def multiply_elem(list, size):
    mult_elem = []
    for i in range((size + 1) // 2):
        mult_elem.append(list[i] * list[size - (i + 1)])
    return mult_elem

list = get_list(size)
print(f"Произведение пар элементов в списке {list} -> {multiply_elem(list, size)}")