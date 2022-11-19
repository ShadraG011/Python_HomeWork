# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

num = int(input("Введите количество элементов списка: "))
myList = []
for _ in range(num):
    myList.append(random.randint(-num, num))
print(myList)

with open('Homework_2/Task_4/position.txt', 'r') as data:
    xy = data.read().split('\n')

multi = myList[int(xy[0])] * myList[int(xy[1])]
print(multi)