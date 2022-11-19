# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint as rT

num = int(input("Введите количество элементов списка: "))

file = 'Homework_6/Task_3/position.txt'
with open(file, 'r') as data:
    xy = data.read().split('\n')

# myList = []
# for _ in range(num):
#     myList.append(random.randint(-num, num))
# print(myList)
myList = [rT(-num, num) for _ in range(num)]


# multi = myList[int(xy[0])] * myList[int(xy[1])]
xy = list(map(int, xy))
multi = myList[xy[0]] * myList[xy[1]]

print(f"Произведение чисел на индексах {xy} списка {myList}: {multi}")