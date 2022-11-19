from aiogram import Dispatcher

import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.help, commands=['help'])
    dp.register_message_handler(commands.end, commands=['end'])
    dp.register_message_handler(commands.new_game, commands=['new_game'])
    dp.register_message_handler(commands.rules, commands=['rules'])
    dp.register_message_handler(commands.step)