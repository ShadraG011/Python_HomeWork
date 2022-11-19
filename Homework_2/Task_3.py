#3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

num = int(input("Введите число: "))
arr = []
count = 0
for i in range (num):
    arr.append(round(((1+1/num)**num), 1))
    count += (1+1/num)**num
print(arr)
print(round(count, 0))

