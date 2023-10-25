import telebot
import requests
import json
import time
from settings import *

bot = telebot.TeleBot(TELEGRAMM_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='привет')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text=f'Здравствуйте! Я - бот с актуальными данными о погоде)\nЯ помогу вам при помощи команд:\n{COMMANDS_LINE}')


@bot.message_handler(commands=['pogodabrn'])
def pogoda_brn(message):
    req = requests.get(BRN_URL)
    inter_data = json.loads(req.text)['list'][0]
    data = inter_data['main']
    bot.send_message(message.chat.id, text=f'Сейчас в Барнауле {round(data["temp"]-273.15)}°.\nОщущается как {round(data["feels_like"]-273.15)}°.\nАтмосферное давление - {data["pressure"]} мм.рт.ст.\nВлажность - {data["humidity"]} %.')
@bot.message_handler(commands=['pogodabsk'])
def pogoda_bsk(message):
    req = requests.get(BSK_URL)
    inter_data = json.loads(req.text)['list'][0]
    data = inter_data['main']
    bot.send_message(message.chat.id, text=f'Сейчас в Бийске {round(data["temp"]-273.15)}°.\nОщущается как {round(data["feels_like"]-273.15)}°.\nАтмосферное давление - {data["pressure"]} мм.рт.ст.\nВлажность - {data["humidity"]} %.')


@bot.message_handler(commands=['pogodansk'])
def pogoda_nsk(message):
    req = requests.get(NSK_URl)
    inter_data = json.loads(req.text)['list'][0]
    data = inter_data['main']
    bot.send_message(message.chat.id, text=f'Сейчас в Новосибирске {round(data["temp"]-273.15)}°.\nОщущается как {round(data["feels_like"]-273.15)}°.\nАтмосферное давление - {data["pressure"]} мм.рт.ст.\nВлажность - {data["humidity"]} %.')


@bot.message_handler(commands=['pogodakbv'])
def pogoda_kbv(message):
    req = requests.get(KBV_URL)
    inter_data = json.loads(req.text)['list'][0]
    data = inter_data['main']
    bot.send_message(message.chat.id, text=f'Сейчас в Куйбышеве {round(data["temp"]-273.15)}°.\nОщущается как {round(data["feels_like"]-273.15)}°.\nАтмосферное давление - {data["pressure"]} мм.рт.ст.\nВлажность - {data["humidity"]} %.')


@bot.message_handler(commands=['pogodankz'])
def pogoda_nkz(message):
    req = requests.get(NKZ_URl)
    inter_data = json.loads(req.text)['list'][0]
    data = inter_data['main']
    bot.send_message(message.chat.id, text=f'Сейчас в Новокузнецке {round(data["temp"]-273.15)}°.\nОщущается как {round(data["feels_like"]-273.15)}°.\nАтмосферное давление - {data["pressure"]} мм.рт.ст.\nВлажность - {data["humidity"]} %.')

bot.polling(none_stop=True)
