# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

size = int(input("Введите размер списка: "))

def get_list(size):
    list = []
    for i in range(0, size):
        el = float(input(f"Введите {i+1}-й элемент списка: "))
        list.append(el)
    return list

def rezult(list):
    float_list = []
    for i in list:
        i -= int(i)
        float_list.append(round(i,2))
    print(float_list)
    max = 0
    min = 1
    for i in float_list:
        if i > max: max = i
        if i == 0: continue
        if i < min: min = i
    return round((max - min), 2)

list = get_list(size)
print(f"Разница максимума и минимума дробной части элементов в списке {list}: {rezult(list)}")
