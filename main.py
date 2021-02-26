import telebot
import random
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "И тебе привет, {}".format(random.choice(config.words["appeals"])))

@bot.message_handler(content_types = ["text"])
def text(message):
    text = message.text.lower()
    if text in config.words["hello"]:
        bot.send_message(message.chat.id, random.choice(config.words["hello"]))
    else:
        bot.send_message(message.chat.id, random.choice(config.words["phrases"]))

bot.polling()

