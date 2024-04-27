import telebot

TOKEN = '6153975130:AAFkPPUqX6mCcCxfvYkIurJHl6o2yIUu9yc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! Use /mute to mute a user and /unmute to unmute a user.")

@bot.message_handler(commands=['mute'])
def mute_user(message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    bot.restrict_chat_member(chat_id, user_id, until_date=0)

@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    bot.restrict_chat_member(chat_id, user_id, until_date=None)

bot.polling()
