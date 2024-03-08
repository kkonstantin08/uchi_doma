import telebot
import wikipediaapi



bot = telebot.TeleBot(TOKEN)
wiki_wiki = wikipediaapi.Wikipedia('ru')


@bot.message_handler(content_types=['text'])
def search(message):
    text = message.text
    result = wiki_wiki.page(text)
    if result.exists():
        bot.send_message(message.chat.id, result.summary)
    else:
        bot.send_message(message.chat.id, 'Ничего не нашел 😢')


bot.infinity_polling()
