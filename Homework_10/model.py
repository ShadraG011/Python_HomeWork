from aiogram import types
import random

total_candyes = "end"
step = None

def getTotal(message: types.Message):
    global total_candyes
    if total_candyes == "end" or total_candyes == "notGame":
        return total_candyes
    else:
        total_candyes -= int(getStep(message))
        return total_candyes
    
def getTotalBot():
    global total_candyes
    if total_candyes == "end":
        return total_candyes
    else:   
        total_candyes -= getBotStep()
        return total_candyes

def getStep(message: types.Message):
    global step
    step = message.text
    return step

def getBotStep():
    bt_step = 0
    if total_candyes <= 150 and total_candyes > 143:
        bt_step = total_candyes - 143
        if bt_step == 0:
            bt_step = random.randint(1, 5)
    elif total_candyes <= 143 and total_candyes > 115:
        bt_step = total_candyes - 115
        if bt_step == 0:
            bt_step = random.randint(1, 5)
    elif total_candyes <= 115 and total_candyes > 86:
        bt_step = total_candyes - 87
        if bt_step == 0:
            bt_step = random.randint(1, 5)
    elif total_candyes <= 86 and total_candyes > 57:
        bt_step = total_candyes - 58
        if bt_step == 0:
            bt_step = random.randint(1, 5)
    elif total_candyes <= 57 and total_candyes > 28:
        bt_step = total_candyes - 29
        if bt_step == 0:
            bt_step = random.randint(1, 5)
    elif total_candyes <= 28:
        bt_step = total_candyes
    return bt_step
    