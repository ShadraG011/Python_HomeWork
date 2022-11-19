# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
size = int(input("Введите размер списка: "))

def get_list(size):
    list= []
    for _ in range(0, size):
        list.append(random.randint(1, 11))
    return list

def sum_elem_position(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]
    return sum

list = get_list(size)
print(f"Сумма элементов в списке {list}, которые стоят на нечетных позиция -> {sum_elem_position(list)}")
