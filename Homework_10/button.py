from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton(text="/new_game")
b2 = KeyboardButton(text="/rules")
b3 = KeyboardButton(text="/help")
b4 = KeyboardButton(text="/end")
kb.add(b1, b2).add(b3, b4)