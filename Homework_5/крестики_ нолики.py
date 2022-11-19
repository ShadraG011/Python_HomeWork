import random

field = list(range(9, 0, -1))


win_combination = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),(2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def drow_field():
    print("-------------")
    for i in range(3):
        print('|', field[2 + i * 3], '|', field[1 + i * 3], '|', field[0 + i * 3], '|')
        print("-------------")

def take_step(plaer_step):
    while True:
        value = int(input("В какую ячейку поставить " + plaer_step + " ? "))
        if value < 1 or value > 9:
            print("Вы ввели неправильной номер ячейки. Повторите попытку.")
            continue
        if str(field[9 - value]) in "ox":
            print("Эта ячейка уже занята")
            continue
        field[9 - value] = plaer_step
        break


def check_win():
    for each in win_combination:
        if (field[each[2] - 1]) == (field[each[1] - 1]) == (field[each[0] - 1]):
            return field[each[0] - 1]
    else:
        return False


def game():
    count = random.randint(0, 1)
    while True:
        drow_field()
        if count % 2:
            take_step("x")
        else:
            take_step("o")
        if count > 3:
            winner = check_win()
            if winner:
                drow_field()
                print(winner, "Выйграл!")
                break
        count += 1
        if count > 8:
            drow_field()
            print('Ничья')
            break


game()
