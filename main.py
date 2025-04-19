import telebot
import datetime
bot=telebot.TeleBot('7295229682:AAFFcHBHkTjBlDdhGgiUBrRdsjAE_9nSEQQ')
now=datetime.datetime.now()

@bot.message_handler(content_types=["text"])
def dialog(message):
    today=now.day
    hour=now.hour
    if message.text=="привет" :
        if today==now.day and 6<=hour<12:
            bot.send_message(message.chat.id, "Приветствую \n")
                                             "по моим рассчётам,у вас сейчас утро"
        elif today==now.day and 12<=hour<17:
            bot.send_message(message.chat.id, "Приветствую \n")
    elif message.text=="Как у тебя дела?":
        bot.send_message(message.chat.id,"У меня всё хорошо,а у тебя?")
    elif message.text=="Привет":
        bot.send_message(message.chat.id, "Приветствую")
    elif message.text=="прив":
        bot.send_message(message.chat.id, "Приветствую")
    elif message.text == "Прив":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text=="ПрИвЕт":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "пРиВеТ":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Hi":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "hi":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Hello":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "hello":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "привет.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Привет.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "прив.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Прив.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "ПрИвЕт.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "пРиВеТ.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Hi.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "hi.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Hello.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "hello.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "привет!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Привет!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "прив!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Прив!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "ПрИвЕт!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "пРиВеТ!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Hi!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "hi!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Hello!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "hello!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "привет^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Привет^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "прив^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Прив^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "ПрИвЕт^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "пРиВеТ^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Hi^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "hi^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Hello^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "hello^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Приветствую":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "приветствую":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Приветствую.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "приветствую.":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Приветствую!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "приветствую!":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "Приветствую^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    elif message.text == "приветствую^^":
        bot.send_message(message.chat.id, "Приветствую")
        if message.text == "Как у тебя дела?":
            bot.send_message(message.chat.id, "У меня всё хорошо,а у тебя?")
    else:
       bot.send_message(message.chat.id, "?")


bot.infinity_polling()











