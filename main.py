import telebot
from telebot import types
API_KEY="7295229682:AAFFcHBHkTjBlDdhGgiUBrRdsjAE_9nSEQQ"
# pip install pyTelegramBotAPI 
bot=telebot.TeleBot(API_KEY)
@bot.message_handler(commands=["start"])
def start(message:types.Message):
    chat_id=message.chat.id
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("Привет")
    btn2=types.KeyboardButton("Пока")
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(chat_id,"Что скажешь?",reply_markup=markup)
@bot.message_handler(content_types=["text","sticker"])
def handler_text(message:types.Message):
    print(message)
    chat_id=message.chat.id
    if message.text=="Привет":
        bot.send_message(chat_id,"Приветствую")
    elif message.text=="Пока":
        bot.send_message(chat_id,"Пока")
        bot.send_photo(chat_id,open("./Yoh_Asakura.jpg","rb"))
        bot.send_sticker(chat_id,"CAACAgEAAxkBAAMeZ_DjbiJmMif30O8wwFZH9vKgOHQAAnUBAAJ9dRFE-18T16hHhnQ2BA")
    elif message.content_type=="sticker":
        bot.send_message(chat_id,f"ID твоего стикера:{message.sticker.file_id}")

print("***бот запущен***")
bot.infinity_polling()