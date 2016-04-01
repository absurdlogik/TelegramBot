import config
import telebot
import time
import texts

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, texts.start_msg)

@bot.message_handler(commands=['help'])
def send_help(message):
    msg = bot.send_message(message.chat.id, texts.help_msg)

@bot.message_handler(commands=['auth'])
def send_auth(message):
    msg = bot.send_message(message.chat.id, 'Нужно больше золота!')

if __name__ == '__main__':
    bot.polling(none_stop=True)