# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности. Решать через множества и еще каким-нибудь способом кроме множества
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import random

num = int(input("Введите размер списка: "))

def get_list(num):
    list = []
    for _ in range(num):
        list.append(random.randint(1, 10))
    return list

list = get_list(num)

def list_unique_numbers(list):
    result_list = []
    for i in list:
        count = 0
        for j in list:
            if i == j:
                count += 1
        if count == 1:
            result_list.append(i)
    return result_list

print(f"Начальный список: {list}\nСписок с неповторяющимися элементами: {list_unique_numbers(list)} ")