import telebot
import requests
from telebot import types
from config import TOKEN, API_KEY, URL_WEATHER_API

EMOJI_CODE = {200: '⛈',
              201: '⛈',
              202: '⛈',
              210: '🌩',
              211: '🌩',
              212: '🌩',
              221: '🌩',
              230: '⛈',
              231: '⛈',
              232: '⛈',
              301: '🌧',
              302: '🌧',
              310: '🌧',
              311: '🌧',
              312: '🌧',
              313: '🌧',
              314: '🌧',
              321: '🌧',
              500: '🌧',
              501: '🌧',
              502: '🌧',
              503: '🌧',
              504: '🌧',
              511: '🌧',
              520: '🌧',
              521: '🌧',
              522: '🌧',
              531: '🌨',
              600: '🌨',
              601: '🌨',
              602: '🌨',
              611: '🌨',
              612: '🌨',
              613: '🌨',
              615: '🌨',
              616: '🌨',
              620: '🌨',
              621: '🌨',
              622: '🌨',
              701: '',
              711: '',
              721: '',
              731: '',
              741: '',
              751: '',
              761: '',
              762: '',
              771: '',
              781: '',
              800: '☀️',
              801: '🌥',
              802: '☁️',
              803: '☁️',
              804: '☁️'}
json_file_dict = ''
bot = telebot.TeleBot(TOKEN)


def get_weather(lat, lon):
    params = {'lat': lat,
              'lon': lon,
              'lang': 'ru',
              'units': 'metric',
              'appid': API_KEY}
    response = requests.get(url=URL_WEATHER_API, params=params).json()
    return response


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Получить погоду', request_location=True)
    item2 = types.KeyboardButton('О проекте')
    text = 'Отправь мне свое местоположение и я отправлю тебе погоду.'
    markup.add(item1, item2)
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(content_types=['location'])
def send_weather(message):
    global json_file_dict, EMOJI_CODE
    latitude = message.location.latitude
    longitude = message.location.longitude
    json_file_dict = get_weather(latitude, longitude)
    print(get_weather(latitude, longitude), json_file_dict['weather'][0]['description'],
          json_file_dict['main']['temp'], json_file_dict['main']['feels_like'], json_file_dict['name'])
    messagee = f' 🏙️Погода в: {json_file_dict["name"]}\n'
    messagee += f'{EMOJI_CODE[json_file_dict["weather"][0]["id"]]}{json_file_dict["weather"][0]["description"].capitalize()}.\n'
    messagee += f' 🌡️Температура {json_file_dict["main"]["temp"]}°C.\n'
    messagee += f' 🌡️Ощущается {json_file_dict["main"]["feels_like"]}°C.\n'
    messagee += f'💧Влажность {json_file_dict["main"]["humidity"]}%.\n'
    bot.send_message(message.chat.id, messagee)


@bot.message_handler(content_types=['text'])
def echo_message(message):
    if message.text == 'О проекте':
        text = '🎯Проект по программе школы Учи.Дома, который подскажет Вам погоду в Вашем городе🎯'
        bot.send_message(message.chat.id, text)


bot.infinity_polling()
