import telebot
from telebot import types
import requests
from telebot.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton

URL = 'https://cataas.com/cat'
# TOKEN = '6741853928:AAHC7FVsukNoVYNzXkK1fjKKZr-7Qo_FPY8'
bot = telebot.TeleBot(TOKEN)

right_replies = 0
count_answers = 0


def get_cat():
    response = requests.get(URL)
    return response.content


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(
        InlineKeyboardButton('Москва', callback_data='yes'),
        InlineKeyboardButton('Берн', callback_data='no'),
        InlineKeyboardButton('Закончить игру', callback_data='end')
    )
    item1 = types.KeyboardButton('Котика!')
    markup.add(item1)
    # bot.send_message(chat_id, 'Привет!'.format(message.from_user))
    bot.send_message(chat_id, 'Назови столицу страны России?'.format(message.from_user),
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def echo_message(message):
    chat_id = message.chat.id
    if message.text == 'Котика!':
        bot.send_photo(chat_id, get_cat())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global right_replies, count_answers
    if call.data == 'yes':
        right_replies += 1
        count_answers += 1
        bot.answer_callback_query(call.id, f'Верно!Вы угадали {right_replies}/{count_answers} ')
        send_welcome(message='заново')
    if call.data == 'no':
        count_answers += 1
        bot.answer_callback_query(call.id, f'Неверно!Вы угадали {right_replies}/{count_answers} ')
        send_welcome(message='заново')
    if call.data == 'end':
        bot.answer_callback_query(call.id, f'Игра окончена!Вы угадали {right_replies}/{count_answers}.Вы большой молодец! ')
        bot.delete_message(call.message.chat.id, call.message.message_id)


bot.infinity_polling()
