# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))

def get_list_of_multipliers(num): 
    list_of_multipliers = []
    result_multipliers_list = []

    for i in range(2, num + 1):
        if num % i == 0:
            list_of_multipliers.append(i)
    
    for i in list_of_multipliers:
        while num % i == 0:
            result_multipliers_list.append(i)
            num /= i
        if num == 1: break
    return result_multipliers_list

print(f"Список множителей числа {num}: {get_list_of_multipliers(num)}")
