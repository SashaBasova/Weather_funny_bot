import telebot
import random

from telebot import types

#Токен телеграм-бота
bot = telebot.TeleBot('token', parse_mode='html')

#Приветственное сообщение при команде '/start'
@bot.message_handler(commands=['start'])
def zdarova(message):
    bot.send_message(message.chat.id, 'Privet', reply_markup=markup )

#Клавиатура
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Узнать прогноз погоды')

markup.add(item1)

weather = ['Полгода плохая погода. Полгода - совсем никуда', 
'На Дерибасовской хорошая погода', 
'На Брайтон Бич опять идут дожди', 
'А за окном, то дождь, то снег...',
'У природы нет плохой погоды. Каждая погода благодать',
'Ой, мороз, мороз, не морозь меня',
'Летний дождь, летний дождь начался сегодня рано',
'Главней всего погода в доме, а всё другое - суета', 
'Снег падает на всех, все падают на снег',
'Тучи, а тучи, а тучи как люди...',
'Погода нелётная на зло нам, падают капли с небосвода',
'Грохочет гром, сверкает молния в ночи',
'Облака этим летом, пожалуй, будут особенно хороши',
'За окном дикие минуса. Замело все дороги до тебя',
'Много солнца, много света, есть народная примета: На природе все раздеты, значит, время года — лето!']


@bot.message_handler(content_types=['text', 'photo'])
def messagelist(message):
  if message.text == 'Узнать прогноз погоды':
    bot.send_message(message.chat.id, random.choice(weather))
  else:
    bot.send_message(message.chat.id, 'ниче не понял')

#Запуск бота
bot.polling(none_stop=True, interval=0)
