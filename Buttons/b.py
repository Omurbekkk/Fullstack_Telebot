import json
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def write_to_json(data:dict):
    with open('top.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

def get_db():
    try:
        with open("top.json") as file:
            return json.load(file)
    except:
        # если файл db.json не существует
        # или он пустой
        return {}


def write_to_json(data:dict):
    with open('dir.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

def get_dbb():
    try:
        with open("dir.json") as file:
            return json.load(file)
    except:
        # если файл db.json не существует
        # или он пустой
        return {}


# def get_keyboard():

#     pages_keyboard = InlineKeyboardMarkup()

#     buttons = []
#     for page in range(1,11):
#         button = InlineKeyboardButton(page, callback_data=page)
#         buttons.append(button)

#     pages_keyboard.add(*buttons)
#     return pages_keyboard




def get_keyboard():
    pages = get_db()

    pages_keyboard = InlineKeyboardMarkup()

    buttons = []
    for page in pages:
        button = InlineKeyboardButton(page, callback_data=page)
        buttons.append(button)

    pages_keyboard.add(*buttons)
    return pages_keyboard



def get_keyboardd():
    dirs = get_dbb()

    pages_keyboard = InlineKeyboardMarkup()

    buttons = []
    for page in dirs:
        button = InlineKeyboardButton(page, callback_data=page)
        buttons.append(button)

    pages_keyboard.add(buttons[0]).add(buttons[1]).add(buttons[2]).add(buttons[3]).add(buttons[4]).add(buttons[5])
    return pages_keyboard