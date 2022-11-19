# Реализуйте алгоритм перемешивания списка.
import random

size = int(input("Введите размер списка: "))

def Get_list(size):
    arr = []
    for i in range(0, size):
        count = int(input(f"Введите {i + 1}-й элемент списка: "))
        arr.append(count)
    return arr
list = Get_list(size)

def Revers_list(list):
    for i in range(len(list)):
        k = random.randint(0, len(list) - 1)
        temp = list[i]
        list[i] = list[k]
        list[k] = temp
    return list
    
print( f"Список до перемешивания: {list}"+ '\n' + f"Список после перемешивания: {Revers_list(list)}")
