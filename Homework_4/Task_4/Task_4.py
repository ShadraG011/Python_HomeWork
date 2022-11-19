# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random
file = "Homework_4/Task_4/result.txt"

k = int(input("Введите натуральную степень k: "))

def get_ratio(k):
    ratio = []
    for _ in range(k):
        ratio.append(random.randint(-100, 100))
    print(f"Коэффициенты многочлена: {ratio}")
    return ratio

def get_degree(k):
    degree = []
    for _ in range(k):
            degree.append(f"x^{k}")
            k-=1
    return degree

def result_polynomial(ratio, degree):
    result = ""
    for i in range(0, len(degree)):
        if ratio[i] == 0:
            continue
        elif degree[i] != "x^1" and ratio[i] != 0:
            if ratio[i] > 0:
                result += " + " + str(ratio[i]) + degree[i]
            elif ratio[i] < 0: result += " - " + str(abs(ratio[i])) + degree[i]
        elif degree[i] == "x^1" and ratio[i] != 0 and ratio[i] > 0:
            result += " + " + str(ratio[i]) + "x"
            break
        elif degree[i] == "x^1" and ratio[i] != 0 and ratio[i] < 0:
            result += " - " + str(abs(ratio[i])) + "x"
            break
    result += " = 0"
    return result

ratio = get_ratio(k)
degree = get_degree(k)

print(f"Многочлен степени k:{result_polynomial(ratio, degree)}")

with open(file, "w", encoding="UTF-8") as data:
    data.write(f"Введеная степен: {k}\n")
    data.write(f"Коэффициенты многочлена: {ratio}\n")
    data.write(f"Многочлен степени k:{result_polynomial(ratio, degree)}")