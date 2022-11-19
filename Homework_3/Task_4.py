# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input("Введите число для преобразования его в двоичный код: "))

def Binary(num):
    list = []
    while(num//2 != 0):
        el = num - ((num//2)*2)
        list.insert(0, str(el))
        num //= 2
    list.insert(0, str(num - ((num//2)*2)))
    return "".join(list)

print(f"Двоичный код числа {num}: {Binary(num)}")