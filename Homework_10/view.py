from aiogram import types
from button import kb
from bot import bot
import model

HELP_COMMAND = """
<b>/help</b> - <em>Список команд</em>
<b>/help</b> - <em>Правила игры</em>
<b>/new_game</b> - <em>Запуск игры</em>
<b>/end</b> - <em>Завершение игры</em>
"""


async def startGame(message: types.Message):
    model.total_candyes = "notGame"
    await bot.send_message(message.chat.id,
                           f'{message.from_user.first_name}, привет! Это игра в конфетки.\nЧтобы увидеть правила нажми на /rules.\nЧтобы начать игру нажми /new_game.', reply_markup=kb)


async def rulesGame(message: types.Message):
    await bot.send_message(message.chat.id, f'Правила:\nНа столе 150 конфет, ты можешь взять от 1 до 28 конфет кто забирает последние конфеты со стола побеждает и забирает все конфеты.\nНажми на /new_game, чтобы начать.\nУдачной игры!')


async def help_command(message: types.Message):
    await bot.send_message(message.chat.id, text=HELP_COMMAND, parse_mode="HTML")


async def endGame(message: types.Message):
    model.total_candyes = "end"
    await bot.send_message(message.chat.id,
                           f'{message.from_user.first_name}, спасибо за игру, '
                           f'возвращайся скорее!')


async def startNewGame(message: types.Message):
    model.total_candyes = 150
    await bot.send_message(message.chat.id,
                           f'{message.from_user.first_name}, '
                           f'Игра запущена, введи количество конфет, которые ты хочешь взять!)')


async def viewSteps(message: types.Message):
    step = model.getStep(message)
    if model.total_candyes == "notGame":
        await bot.send_message(message.chat.id, 'Игра не запущена!\nДля запустка нажмите /new_game.\nЕсли хотите посмотреть правила\nнажмите /rules.')
    else:
        try:
            if 0 < int(step) < 29:
                cand = model.getTotal(message)
                if cand == "end":
                    await bot.send_message(message.chat.id, 'Игра завершена,\nдля запустка нажмите /new_game')
                else:
                    if cand > 0:
                        await bot.send_message(message.chat.id, text=f"{message.from_user.first_name} взял {step} конфет\nосталось {cand}")
                        cand_bot = model.getTotalBot()
                        if cand_bot > 0:
                            await bot.send_message(message.chat.id, text=f"Бот взял {cand - cand_bot} конфет\nосталось {cand_bot}")
                        else:
                            await bot.send_message(message.chat.id, f'Бот забрал {cand - cand_bot} конфет и победил!\nИгра окончена\nдля перезапуска нажмите /new_game')
                            model.total_candyes = "end"
                    else:
                        await bot.send_message(message.chat.id, f'Игра окончена\nпобедитель {message.from_user.first_name}\nдля перезапуска нажмите /new_game')
                        model.total_candyes = "end"
            elif model.total_candyes != "end":
                await bot.send_message(message.chat.id, 'За один ход можно взять от 1 до 28 конфет!')
            else:
                await bot.send_message(message.chat.id, 'Игра завершена\nдля запуска нажмите /new_game')
        except:
            if model.total_candyes != "end":
                await bot.send_message(message.chat.id, "Введи количество конфет цифрой!")
            else:
                await bot.send_message(message.chat.id, 'Игра завершена\nдля запуска нажмите /new_game')
