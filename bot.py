from pyrogram import Client, filters

app = Client("my_bot", api_id=23136380, api_hash="6ae6541159e229499615953de667675c", bot_token="6153975130:AAFkPPUqX6mCcCxfvYkIurJHl6o2yIUu9yc")

@app.on_message(filters.command("mute"))
def mute_user(client, message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    client.restrict_chat_member(chat_id, user_id, until_date=None, can_send_messages=False)

@app.on_message(filters.command("unmute"))
def unmute_user(client, message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    client.restrict_chat_member(chat_id, user_id, until_date=None, can_send_messages=True)

app.run()
