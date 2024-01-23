import telebot
from telebot import types

# Конфиг/токен бота
bot = telebot.TeleBot('6230731881:AAE-UvrOAYgZ56ELMrjcdsgtaF-Jq4buyic')


# Функция Старт
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''
    Приветствую! Я телеграм-бот созданный Егором Мельниковым. Я выдаю цитаты и афоризмы на предложенные вам темы.
    ''', reply_markup=markup)
# Функция About
@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, '''
    Данный телеграм бот создан для самообучения и освоения языка программирования Python, при помощи библиотеки Telebot.
Это мой первый телеграм бот, скорее всего после достаточного изчения данной темы бот будте удален. И надеюсь мои следующие
боты будут гораздо лучше.
    ''', reply_markup=markup)


# Книпки
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

item1 = types.KeyboardButton("Цитата про успех")
item2 = types.KeyboardButton("Цитата про деньги")
item3 = types.KeyboardButton("Цитата про людей")
item4 = types.KeyboardButton("Цитата про эмоции")

markup.add(item1, item2, item3, item4)
# Ответ
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == "Цитата про успех":
            bot.send_message(message.chat.id, 'Дисциплина - ключ к успеху.',  reply_markup=markup)
        elif message.text == "Цитата про деньги":
            bot.send_message(message.chat.id, 'Деньги должны работать на вас, а не вы на деньги.',  reply_markup=markup)
        elif message.text == "Цитата про людей":
            bot.send_message(message.chat.id, 'Относитесь к людям так, как вы хотели бы, чтобы относились к вам.',  reply_markup=markup)
        elif message.text == "Цитата про эмоции":
            bot.send_message(message.chat.id, 'Вы не счастливы - потому что у вас есть время задуматься о счастье.',  reply_markup=markup)


# Онлайн/оффлайн
bot.polling(none_stop=True)