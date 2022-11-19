from aiogram import types
import view


async def start(message: types.Message):
    await view.startGame(message)

async def help(message: types.Message):
    await view.help_command(message)

async def end(message: types.Message):
    await view.endGame(message)

async def new_game(message: types.Message):
    await view.startNewGame(message)

async def rules(message: types.Message):
    await view.rulesGame(message)

async def step(message: types.Message):
    await view.viewSteps(message)

