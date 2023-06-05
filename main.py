import json
import requests
from bs4 import BeautifulSoup as BS

import telebot
from decouple import config

from BUTS.b import get_db, get_dbb
from BUTS.b import get_keyboard, get_keyboardd




main_url = 'https://tickets.kg/'

def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup


def get_product_info(product:BS) -> dict:
    title = product.find('div', {'class':'pl-1'}).text.lstrip().rstrip()
    return title
    # print(title)

# get_product_info(soup)

def get_all_products_from_page(url:str) -> list:
    res = []
    soup = get_soup(url)
    box = soup.find('div', {'class':'bg-1 bg-dark-49 border-radius-8 bs-2 bs-dark-3 pl-2 pr-2 overflow-h'})
    # print(box)
    products = box.find_all('div', {'class':'f-center-space-between'})
    for product in products:
        product_info = get_product_info(product)
        res.append(product_info)
    return res


def write_to_json(data:dict):
    with open('top.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

write_to_json(get_all_products_from_page(main_url))





def get_product_info(product:BS) -> dict:
    title = product.text.lstrip().rstrip()
    return title
    # print(title)

# get_product_info(soup)

def get_all_products_from_page(url:str) -> list:
    res = []
    soup = get_soup(url)
    box = soup.find('ul', {'class':'footer-seo__list directions'})
    # print(box)
    products = box.find_all('li', {'class':'footer-seo__item'})
    for product in products:
        product_info = get_product_info(product)
        res.append(product_info)
    return res


def write_to_json(data:dict):
    with open('dir.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

write_to_json(get_all_products_from_page(main_url))






bot = telebot.TeleBot(config('TOKEN'))

@bot.message_handler(commands=['start'])
def start(message):
    text = """
Здравствуйте!
Мы парсим сайт: tickets.kg!
"""
    textt = "Напишите что-нибудь)"
    texttt = "Для выхода можете написать 'quit'"

    bot.send_message(message.chat.id, text, disable_web_page_preview=True)
    bot.send_message(message.chat.id, textt)
    bot.send_message(message.chat.id, texttt)

@bot.message_handler(content_types=['text'])
def aaaa(message):

    if message.text.lower() == "quit":
        bot.send_message(message.chat.id, "До свидания!")
        bot.stop_polling()
    else:
        db = get_db()
        list_ = []
        for k,v in enumerate(db, 1):
            string = f'{k}. {v}'
            list_.append(string)
        s = ''
        for i in list_:
            s += i + '\n'
        text2 = f"ТОП-10 авиакомпаний\n\n {s}"
        bot.send_message(message.chat.id, text2)

        bot.send_message(message.chat.id, 'Выберите авиакомпанию:', reply_markup=get_keyboard())



@bot.callback_query_handler(lambda x: True)
def send_data(call):
    # db = get_dbb()
    # page = call.data
    # prod = db[page]
    text = f"""
    Выберите направление:
"""
    bot.send_message(call.from_user.id, text, reply_markup=get_keyboardd())

bot.polling()
