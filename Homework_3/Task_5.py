from distutils.command.clean import clean


clean()
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

num = int(input("Введите число: "))

def Negofibonacci(num):
    fib1 = 0
    fib2 = 1
    fibonacci = [fib2]
    for _ in range(1, num):
        sum_fib = fib1 + fib2
        fib1 = fib2
        fib2 = sum_fib
        fibonacci.append(sum_fib)
    fib1 = 1
    fib2 = 1
    for _ in range(0, num + 1):
        min_sum_fib = fib1 - fib2
        fib1 = fib2
        fib2 = min_sum_fib
        fibonacci.insert(0, min_sum_fib)
    return fibonacci

print(f"Список чисел Негафибоначчи: {Negofibonacci(num)}")

