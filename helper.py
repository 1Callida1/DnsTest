
from aiogram import types

def generate_inline_kb(command):
    if(command == "start"):
        commands = {
            "Регламенты": "call_regulations",
            "Выкладки": "call_display"
        }

    elif(command == "display"):
        commands = {
            "Рег. Общие": "call_distributions",
            "Рег. Лок. сети": "call_distributions",
            "Рег. СБУ": "call_distributions",
            "Рег. Зонирование": "call_distributions",
        }
    elif(command == "regulations"):
        commands = {
            "Холод": "call_distributions",
            "Стирка": "call_distributions",
            "Посудомойка": "call_distributions",
            "Климат": "call_distributions",
            "Жарка варка": "call_distributions",
            "Уборка": "call_distributions",
            "TV": "call_distributions",
            "IT и офис": "call_distributions",
            "Посуда": "call_distributions",
            "Нарезка и смешивание": "call_distributions",
            "Товары для красоты": "call_distributions",
            "Уход за одеждой": "call_distributions",
            "Дом аудио": "call_distributions",
            "Умный дом и свет": "call_distributions",
            "Напитки": "call_distributions",
            "Инструменты": "call_distributions",
            "Наушники и колонки": "call_distributions",
            "Автотовары": "call_distributions",
            "GSM и фото": "call_distributions",
            "Предкасса": "call_distributions",
            "Последовательность размещения SIS": "call_distributions"
        }

    buttons = [[]]
    row = 0
    for key, value in commands.items():
        callbackButton = types.InlineKeyboardButton(text=key, callback_data=value)

        if(len(buttons[row]) == 2):
            buttons.append([])
            row += 1

        buttons[row].append(callbackButton)

    return types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)

def generate_kb(command):
    if(command == "Back"):
        kb = [
        [types.KeyboardButton(text="Назад")],
    ]
    elif(command == "ToStart"):
        kb = [
        [types.KeyboardButton(text="К началу")],
    ]
    
    return types.ReplyKeyboardMarkup(keyboard=kb)