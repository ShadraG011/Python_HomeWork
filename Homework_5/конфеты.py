import random

candyes = 150

# # Игра игроком - игрок
# def game(candyes):
#     num = (random.randint(1,2))
#     while candyes > 0:
#         step = int(input(f"Сколько конфет хочет взять {num}-й игрок ?: "))
#         if step > 28:
#             print("За один раз можно взять не более 28 конфет")
#             continue
#         elif step < 0:
#             print("Пожалуйста возьмите от 1 до 28 конфет или пропустите шаг взяв 0 конфет)")
#             continue
#         if (candyes - step) < 0:
#             print(f"Вы можете взять только {candyes} оставшихся конфет")
#             continue
#         else:
#             if (candyes - step) != 0:
#                 candyes -= step
#                 print(f"Осталось {candyes} конфет")
#                 if num == 1:
#                         num += 1
#                 else: num -= 1
#             else: 
#                 print(f"Игра окончена {num}-й игрок забирает все конфеты") 
#                 break
# game(candyes)

# Игра игроком - бот
def game_with_bot(candyes):
    print(f"На столе {candyes} конфет.")
    step = True
    while candyes > 0:
        if step: 
            step_gamer = int(input(f"Сколько конфет вы хочетите взять: "))
            if step_gamer > 28:
                print("За один раз можно взять не более 28 конфет")
                continue
            elif step_gamer < 0:
                print("Пожалуйста возьмите от 1 до 28 конфет или пропустите шаг взяв 0 конфет)")
                continue
            elif (candyes - step_gamer) < 0:
                print(f"Вы можете взять только {candyes} оставшихся конфет")
                continue
            else: 
                if (candyes - step_gamer) != 0:
                    candyes -= step_gamer
                    print(f"Осталось {candyes} конфет")
                    step = False
                else:
                    print(f"Вы победили и забераете все конфеты!")
                    break
        else: 
            step_bot = int(random.randint(1,28))
            if candyes <= 28:
                step_bot = int(candyes)
                print(f"Бот забирает {step_bot} конфет")
                candyes -= step_bot
                print(f"Осталось {candyes} конфет")
                print(f"Бот победил!")
                break
            else:
                print(f"Бот забирает {step_bot} конфет")
                candyes -= step_bot
                print(f"Осталось {candyes} конфет")
                step = True
game_with_bot(candyes)