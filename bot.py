import telebot
bot = telebot.TeleBot("6153975130:AAFkPPUqX6mCcCxfvYkIurJHl6o2yIUu9yc")
@bot.message_handler(func=lambda message: True)
def logo(message):
    logo = f"https://bcassetcdn.com/asset/logo/4b4b23e4-f3d3-42b1-9c5d-615ac62ef5ac/logo?v=4&text={message.text}"
    bot.send_photo(message.chat.id, logo)
bot.infinity_polling()
