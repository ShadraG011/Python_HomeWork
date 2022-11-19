# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
from cmath import pi

count = 0
d = float(input("Введите точность для числа \"ПИ\" от 0.1 до 0.0000000001: "))
if d < 1:
    accuracy = d
    while accuracy != int(accuracy):
        accuracy *=10
        count += 1
    if accuracy == 1:
        print(f"Число \"ПИ\" с точностью {d} = {round(pi, count)}")
    else:
        print("Вывели не правильное число")
else:
        print("Вывели не правильное число")
