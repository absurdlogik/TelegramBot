import config
import telebot
import time
import texts

bot = telebot.TeleBot(config.token)

"""def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            bot.send_message(m.chat.id, m.text)"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, texts.start_msg)

@bot.message_handler(commands=['help'])
def send_help(message):
    msg = bot.send_message(message.chat.id, texts.help_msg)

@bot.message_handler(commands=['now'])
def send_now(message):
    msg = bot.send_message(message.chat.id, texts.get_time())


@bot.message_handler(commands=[])
def send_error(message):
    msg = bot.send_message(message.chat.id, texts.error_msg)

@bot.message_handler()
def send_text(message):
    msg = bot.send_message(message.chat.id, texts.text_msg)


if __name__ == '__main__':
    #bot.set_update_listener(listener)
    bot.polling(none_stop=True)