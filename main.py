import telebot
import random
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "И тебе привет, {}".format(random.choice(config.words["appeals"])))

@bot.message_handler(content_types=["text"])
def text(message):
    text = message.text.lower()
    print("user's message:" + text)
    for i in config.words["unnecessary"]:
        text = text.replace(i, "")
    text = text.replace(" ", "")
    print("user's message after processing:" + text)
    if text in config.words["hello"]:
        bot.send_message(message.chat.id, random.choice(config.words["hello"]))
    elif text in config.words["goodbye"]:
        bot.send_message(message.chat.id, random.choice(config.words["goodbye"]))
    elif text in config.words["sendfoto"]:
        foto = open(f"img/su/su{random.randint(1, 8)}.png", "rb")
        bot.send_sticker(message.chat.id, foto)
        bot.send_message(message.chat.id, "вот тебе мое фото")
    else:
        bot.send_message(message.chat.id, random.choice(config.words["phrases"]))

bot.polling()

