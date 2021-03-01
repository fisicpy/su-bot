import telebot
import random
import config


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "И тебе привет, {}".format(random.choice(config.words["appeals"])))


@bot.message_handler(commands=["help"])
def start_message(message):
    bot.send_message(message.chat.id, "Я могу:\n"
                                      "1. Прислать свое фото\n"
                                      "2. Прислать мем\n"
                                      "3. Поздароваться\n"
                                      "4. Попрощаться\n"
                                      "5. Сказать \"пожалуйста\" если ты скажешь мне спасибо\n"
                                      "6. Лаского назвать тебя")


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
    elif text in config.words["sendmeme"]:
        foto = open(f"img/meme/meme{random.randint(1, 6)}.jpg", "rb")
        bot.send_sticker(message.chat.id, foto)
        bot.send_message(message.chat.id, "вот тебе мем")
    elif text in config.words["thanks"]:
        bot.send_message(message.chat.id, random.choice(config.words["welcome"]))
    else:
        bot.send_message(message.chat.id, random.choice(config.words["phrases"]))


bot.polling()

