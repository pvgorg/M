import os
try:
  import pyrogram
  import requests
except:
  os.system("pip install --upgrade pip && pip install pyrogram && pip install requests")
  import pyrogram
  import requests
import json
import sys
from pyrogram.raw import functions , base , types
from pyrogram import Client, filters, idle , errors ,enums
from pyrogram.types import Message , ChatPermissions
from pyrogram.raw import functions , base , types
import time
api_id = "28985578"   API ID
api_hash = "5addd97449443afcc7240bffe9dbbf8a"  HASH ID
app = Client("@shothesam",api_id,api_hash)
admin = "1502490631" # ADMIN ID
 # به چیز دیگه ای دست نزنید #

if not os.path.isfile("Mode.json"):
 with open("Mode.json" , "w") as fjr:
  fjr.write('{"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0","mode_1": "0","mode_2": "0","mode_3": "0","mode_4": "0","mode_5": "0","mode_6": "0","mode_7": "0","mode_8": "0","mode_9": "0","mode_10": "0","mode_11": "0","mode_12": "0"}')
  fjr.close()

 with app:
  try:
    app.join_chat("")
    app.pin_chat("")
    app.join_chat("")
    app.pin_chat("")
  except:
    pass

with open("Mode.json", "r") as f:
    contents = f.read()
    data = json.loads(contents)

@app.on_message(filters.user(admin))
def admins(client , message):
 me = app.get_me()

 	
 if message.text == "پنل":
  app.edit_message_text(message.chat.id,message.id,f"""
به پنل سلف خوش امدید

➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code> modehelp </code>
◀️ بخش مدیریت مود ها
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code> gphelp </code>
◀️ بخش گروه
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code> funhelp </code>
◀️ بخش سرگرمی
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code> infohelp </code>
◀️ بخش مدیریت اکانت
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code> restart </code>
◀️ ریستارت سلف♻️
➿〰️〰️〰️〰️〰️〰️〰️➿
Owner : @La_shy

""")
 elif message.text == "panel":
  app.edit_message_text(message.chat.id,message.id,f"""
به پنل سلف خوش امدید

➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code> modehelp </code>
◀️ بخش مدیریت مود ها
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code> gphelp </code>
◀️ بخش گروه
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code> funhelp </code>
◀️ بخش سرگرمی
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code> infohelp </code>
◀️ بخش مدیریت اکانت
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code> restart </code>
◀️ ریستارت سلف♻️
➿〰️〰️〰️〰️〰️〰️〰️➿
Owner : @La_shy

""")
 elif message.text == "modehelp":
 	app.edit_message_text(message.chat.id,message.id,f"""
 به بخش مدیریت مود ها خوش آمدید

➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>strike </code> (on|off)
◀️ حالت متن خط خورده
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>hastg </code> (on|off)
▶️ حالت متن هشتگ
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>mension </code> (on|off)
◀️ حالت متن منشن
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>kahat </code> (on|off)
◀️ حالت متن زیرخط دار
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>bold </code> (on|off)
◀️ حالت متن ضخیم
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>italic </code> (on|off)
◀️ حالت متن کج
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>spoiler </code> (on|off)
◀️ حالت متن اسپویلر
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>coding </code> (on|off)
◀️ حالت متن کدینگ(قابلیت کپی)
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>coding2 </code> (on|off)
◀️ حالت متن کدینگ2
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>coding3 </code> (on|off)
◀️ حالت متن کدینگ3
""")
 	
 	
 elif message.text == "gphelp":
 	app.edit_message_text(message.chat.id, message.id,f"""
 	به بخش گروه خوش امدید
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>ban</code> (reply)
▶️بن کاربر (گروه)
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>unban</code> (reply)
▶️حذف بن (گروه)
➿〰️〰️〰️〰️〰️〰️〰️➿	
""")
 	
 elif message.text == "funhelp":
 	app.edit_message_text(message.chat.id, message.id,f"""
دستور های فان 
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>کص</code>
▶️ <code>دلقک</code>
▶️ <code>جق</code>
▶️ <code>قلب</code>
▶️ <code>سیگما</code>
▶️ <code>عشق</code>
▶️ <code>کیر</code>
▶️ <code>نه</code>
▶️ <code>دایناسور</code>
▶️ <code>هک</code>
▶️ <code>مرگ بر امریکا</code>
▶️ <code>ایران</code>
▶️ <code>هواپیما</code>
▶️ <code>بمب</code>
▶️ <code>فاک</code>
▶️ <code>فاک2</code>


بخش کاربردی 
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>Gpt </code>(text)
▶️چت با هوش مصنوعی
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>arz</code>
◀️ دریافت نرخ ارز
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>time</code>
▶️دریافت اطلاعات زمان 	
""")
 elif message.text == "infohelp":
 	app.edit_message_text(message.chat.id, message.id, """
 	بخش اطلاعات اکانت خوش امدید
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>block </code> (reply OR user OR userid)
▶️ بلاک کاربر 
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>unblock </code>(reply OR user OR userid)
▶️رفع بلاک کاربر 
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>setname </code> (text)
▶️تنظیم نام
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>setname2 </code> (text)
▶️تنظیم فامیلی
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>clearname2 </code>
▶️حذف فامیلی
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>setusername </code> (text)
▶️تنظیم یوزر
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>setbio </code> (text)
▶️تنظیم بیو
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>clearbio</code>
▶️حذف بیو
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>me</code>
▶️اطلاعات اکانت شما
➿〰️〰️〰️〰️〰️〰️〰️➿
▶️ <code>id </code>(reply OR user OR userid)
▶️اطلاعات کاربر 


""")
 	
 	
 
 
 
 elif message.text.startswith("strike "):
  if message.text.split()[1] == "on":
   data.update({"strike": "1", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "1", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith("bold "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "1", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "1", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith("mension "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "1", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "1", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith("spoiler "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "1", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith("italic "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "1", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith("kahat "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "1", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith("coding "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "1", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith("coding2 "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "1", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")
 elif message.text.startswith("hastg "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "1", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"1"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")

 elif message.text.startswith("coding3 "):
  if message.text.split()[1] == "on":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "1", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>ON</u></b>")
  elif message.text.split()[1] == "off":
   data.update({"strike": "0", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0", "mod_1":"0"})
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ Mode is <u>OFF</u></b>")
  else:
   app.edit_message_text(message.chat.id, message.id,f"<b>❋ ERROR IN FEEDING . . .</b>")


 elif message.text == "restart":
  app.edit_message_text(message.chat.id, message.id,f"<b>❋ Restart The Self . . .</b>")
  python = sys.executable
  os.execl(python, python, *sys.argv)

 elif message.text == "block" or message.text.startswith("block "):
  app.block_user(message.reply_to_message.from_user.id if message.reply_to_message else message.text.split()[1])
  app.edit_message_text(message.chat.id,message.id,f"**~ User Blocked**")

 elif message.text == "unblock" or message.text.startswith("unblock "):
  app.unblock_user(message.reply_to_message.from_user.id if message.reply_to_message else message.text.split()[1])
  app.edit_message_text(message.chat.id,message.id,f"**~ User Unblocked**")

 elif message.text == "ban" or message.text.startswith("ban "):
   try:
    app.ban_chat_member(message.chat.id , (message.reply_to_message.from_user.id if message.reply_to_message else message.text.split()[1]))
    app.edit_message_text(message.chat.id,message.id,f"**~ User Baned**")
   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")


 elif message.text == "unban" or message.text.startswith("unban "):
  app.ban_chat_member(message.chat.id , (message.reply_to_message.from_user.id if message.reply_to_message else message.text.split()[1]))
  app.edit_message_text(message.chat.id,message.id,f"**~ User Unbaned**")

 elif message.text.startswith("setname "):
  app.edit_message_text(message.chat.id,message.id,f"**~ Your name was changed from ( `{me.first_name}` ) to ( `{message.text.replace('.setname','')[1::]}` )**")
  app.update_profile(first_name=message.text.replace(".setname","")[1::])
 
 elif message.text.startswith("setname2 "):
  app.edit_message_text(message.chat.id,message.id,f"**~ Your Last name was changed from ( `{me.last_name}` ) to ( `{message.text.replace('.setname2','')[1::]}` )**")
  app.update_profile(last_name=message.text.replace(".setname2","")[1::])

 elif message.text == "clearname2":
  app.edit_message_text(message.chat.id,message.id,f"**~ Your Last name is clear**")
  app.update_profile(last_name="")

 elif message.text.startswith("setusername "):
   try:
    app.set_username(message.text.replace('.setusername','')[1::])
    app.edit_message_text(message.chat.id,message.id,f"**~ Your Last name was changed from ( `{me.username}` ) to ( `{message.text.replace('.setusername','')[1::]}` )**")
   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")

 elif message.text.startswith("setbio "):
   try:
    app.update_profile(first_name=me.first_name, bio=message.text.replace('setbio','')[1::])
    app.edit_message_text(message.chat.id,message.id,f"**~ Your bio was changed to ( `{message.text.replace('.setbio','')[1::]}` )**")
   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")

 elif message.text == "clearbio":
   app.update_profile(first_name=me.first_name, bio="")
   app.edit_message_text(message.chat.id,message.id,f"**~ Your bio is clear**")

 elif message.text == "کص":
  app.edit_message_text(message.chat.id,message.id,""" ⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⡆⣤⣾⣿⣿⣧⠹⠄⠄
 ⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⡇⠄⠄
 ⠄⠄⠐⡏⠉⠉⠉⠉⠉⠄⢸⠛⠿⣿⣿⡟⠄⠄⠄
 ⠄⠄⠄⠹⡖⠒⠒⠒⠒⠊⢹⠒⠤⢤⡜⠁⠄⠄⠄
 ⠄⠄⠄⠄⠱⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄""")
  app.edit_message_text(message.chat.id,message.id,"""⠄⠄⠄⠄⠄⠄⠄⢸⣉⠉⠉⠄⢀⠈⠉⢏⠁⠄⠄
 ⠄⠄⠄⠄⠄⠄⡰⠃⠄⠄⠄⠄⢸⠄⠄⢸⣧⠄⠄
 ⠄⠄⠄⠄⠄⣼⣧⠄⠄⠄⠄⠄⣼⠄⠄⡘⣿⡆⠄
 ⠄⠄⠄⢀⣼⣿⡙⣷⡄⠄⠄⠄⠃⠄⢠⣿⢸⣿⡀
 ⠄⠄⢀⣾⣿⣿⣷⣝⠿⡀⠄⠄⠄⢀⡞⢍⣼⣿⠇
 ⠄⠄⣼⣿⣿⣿⣿⣿⣷⣄⠄⠄⠠⡊⠴⠋⠹⡜⠄
⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⡆⣤⣾⣿⣿⣧⠹⠄⠄
 ⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⡇⠄⠄
 ⠄⠄⠐⡏⠉⠉⠉⠉⠉⠄⢸⠛⠿⣿⣿⡟⠄⠄⠄
 ⠄⠄⠄⠹⡖⠒⠒⠒⠒⠊⢹⠒⠤⢤⡜⠁⠄⠄⠄
 ⠄⠄⠄⠄⠱⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄""")
  app.edit_message_text(message.chat.id,message.id,"""⠄⠄⠘⣿⣿⣿⣦⣤⡀⢿⣿⣿⣿⣄⠄⠄⠄⠄⠄
 ⠄⠄⠄⠈⢿⣿⣿⣿⣿⣷⣯⣿⣿⣷⣾⣿⣷⡄⠄
 ⠄⠄⠄⠄⠄⢻⠏⣼⣿⣿⣿⣿⡿⣿⣿⣏⢾⠇⠄
 ⠄⠄⠄⠄⠄⠈⡼⠿⠿⢿⣿⣦⡝⣿⣿⣿⠷⢀⠄
 ⠄⠄⠄⠄⠄⠄⡇⠄⠄⠄⠈⠻⠇⠿⠋⠄⠄⢘⡆
 ⠄⠄⠄⠄⠄⠄⠱⣀⠄⠄⠄⣀⢼⡀⠄⢀⣀⡜⠄
⠄⠄⠄⠄⠄⠄⠄⢸⣉⠉⠉⠄⢀⠈⠉⢏⠁⠄⠄
 ⠄⠄⠄⠄⠄⠄⡰⠃⠄⠄⠄⠄⢸⠄⠄⢸⣧⠄⠄
 ⠄⠄⠄⠄⠄⣼⣧⠄⠄⠄⠄⠄⣼⠄⠄⡘⣿⡆⠄
 ⠄⠄⠄⢀⣼⣿⡙⣷⡄⠄⠄⠄⠃⠄⢠⣿⢸⣿⡀
 ⠄⠄⢀⣾⣿⣿⣷⣝⠿⡀⠄⠄⠄⢀⡞⢍⣼⣿⠇
 ⠄⠄⣼⣿⣿⣿⣿⣿⣷⣄⠄⠄⠠⡊⠴⠋⠹⡜⠄
⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⡆⣤⣾⣿⣿⣧⠹⠄⠄
 ⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⡇⠄⠄
 ⠄⠄⠐⡏⠉⠉⠉⠉⠉⠄⢸⠛⠿⣿⣿⡟⠄⠄⠄
 ⠄⠄⠄⠹⡖⠒⠒⠒⠒⠊⢹⠒⠤⢤⡜⠁⠄⠄⠄
 ⠄⠄⠄⠄⠱⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄""")

  app.edit_message_text(message.chat.id,message.id,""" : ⠄⠄⠄⠄ ⠄⠄⠄⠄ ⠄⠄⠄⠄
 ⠄⠄⡔⠙⠢⡀⠄⠄⠄⢀⠼⠅⠈⢂⠄⠄⠄⠄
 ⠄⠄⡌⠄⢰⠉⢙⢗⣲⡖⡋⢐⡺⡄⠈⢆⠄⠄⠄
 ⠄⡜⠄⢀⠆⢠⣿⣿⣿⣿⢡⢣⢿⡱⡀⠈⠆⠄⠄
 ⠄⠧⠤⠂⠄⣼⢧⢻⣿⣿⣞⢸⣮⠳⣕⢤⡆⠄⠄
 ⢺⣿⣿⣶⣦⡇⡌⣰⣍⠚⢿⠄⢩⣧⠉⢷⡇⠄⠄
 ⠘⣿⣿⣯⡙⣧⢎⢨⣶⣶⣶⣶⢸⣼⡻⡎⡇⠄⠄
 ⠄⠘⣿⣿⣷⡀⠎⡮⡙⠶⠟⣫⣶⠛⠧⠁⠄⠄⠄
 ⠄⠄⠘⣿⣿⣿⣦⣤⡀⢿⣿⣿⣿⣄⠄⠄⠄⠄⠄
 ⠄⠄⠄⠈⢿⣿⣿⣿⣿⣷⣯⣿⣿⣷⣾⣿⣷⡄⠄
 ⠄⠄⠄⠄⠄⢻⠏⣼⣿⣿⣿⣿⡿⣿⣿⣏⢾⠇⠄
 ⠄⠄⠄⠄⠄⠈⡼⠿⠿⢿⣿⣦⡝⣿⣿⣿⠷⢀⠄
 ⠄⠄⠄⠄⠄⠄⡇⠄⠄⠄⠈⠻⠇⠿⠋⠄⠄⢘⡆
 ⠄⠄⠄⠄⠄⠄⠱⣀⠄⠄⠄⣀⢼⡀⠄⢀⣀⡜⠄
⠄⠄⠄⠄⠄⠄⠄⢸⣉⠉⠉⠄⢀⠈⠉⢏⠁⠄⠄
 ⠄⠄⠄⠄⠄⠄⡰⠃⠄⠄⠄⠄⢸⠄⠄⢸⣧⠄⠄
 ⠄⠄⠄⠄⠄⣼⣧⠄⠄⠄⠄⠄⣼⠄⠄⡘⣿⡆⠄
 ⠄⠄⠄⢀⣼⣿⡙⣷⡄⠄⠄⠄⠃⠄⢠⣿⢸⣿⡀
 ⠄⠄⢀⣾⣿⣿⣷⣝⠿⡀⠄⠄⠄⢀⡞⢍⣼⣿⠇
 ⠄⠄⣼⣿⣿⣿⣿⣿⣷⣄⠄⠄⠠⡊⠴⠋⠹⡜⠄
⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⡆⣤⣾⣿⣿⣧⠹⠄⠄
 ⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⡇⠄⠄
 ⠄⠄⠐⡏⠉⠉⠉⠉⠉⠄⢸⠛⠿⣿⣿⡟⠄⠄⠄
 ⠄⠄⠄⠹⡖⠒⠒⠒⠒⠊⢹⠒⠤⢤⡜⠁⠄⠄⠄
 ⠄⠄⠄⠄⠱⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄""")
  app.send_message(message.chat.id,"اینم عکس ننش داش 🤤🤤" ,reply_to_message_id=message.id)
 elif message.text == "ایران":
 	app.edit_message_text(message.chat.id,message.id,f"""🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩""")
 	app.edit_message_text(message.chat.id,message.id,f"""🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️""")
 	app.edit_message_text(message.chat.id,message.id,f"""🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥""")
      
 
 elif message.text == "هک":
  app.edit_message_text(message.chat.id,message.id,f"""	 ███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█ 
████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█ 
███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█ 
████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█ 
███▓▓▓▓▓▓▓╬╬▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
████▓▓▓╬╬╬╬▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ █████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ 
█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ 
████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ 
████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██ 
█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██ 
█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███ 
██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███ 
███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████ 
███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████ 
████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████ 
█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████ 
██████████▓▓▓█▓▓▓╬▓██╬╬╬╬╬╬╬╬╬╬╬▓███████ 
███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████ 
██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████ 
███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████  """)
 elif message.text == "دایناسور":
  app.edit_message_text(message.chat.id,message.id,""" █████████""")
  app.edit_message_text(message.chat.id,message.id,"""█████████
█▄█████▄█""")
  app.edit_message_text(message.chat.id,message.id,"""█████████
█▄█████▄█
█▼▼▼▼▼""")

  app.edit_message_text(message.chat.id,message.id,"""█████████
█▄█████▄█
█▼▼▼▼▼
█ """)
  app.edit_message_text(message.chat.id, message.id,"""█████████
█▄█████▄█
█▼▼▼▼▼
█  
█▲▲▲▲▲""")
  app.edit_message_text(message.chat.id, message.id,"""█████████
█▄█████▄█
█▼▼▼▼▼
█  
█▲▲▲▲▲
█████████""")
  app.edit_message_text(message.chat.id, message.id,"""█████████
█▄█████▄█
█▼▼▼▼▼
█  
█▲▲▲▲▲
█████████
 ██ ██""")
 
 elif message.text == "هواپیما":
 	app.edit_message_text(message.chat.id, message.id,"""🛫┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈""")
 	app.edit_message_text(message.chat.id, message.id,"""┈┈┈🛫┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈""")
 	app.edit_message_text(message.chat.id, message.id,"""┈┈┈┈┈┈🛫┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈""")
 	app.edit_message_text(message.chat.id, message.id,"""┈┈┈┈┈┈┈┈┈┈┈🛫┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈""")
 	app.edit_message_text(message.chat.id, message.id,"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈🛫┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈""")
 	app.edit_message_text(message.chat.id, message.id,"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈💥BOOM💥┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈""")
 elif message.text == "بمب":
 	app.edit_message_text(message.chat.id, message.id,"💣 0")
 	time.sleep(1)
 	app.edit_message_text(message.chat.id, message.id,"💣 1")
 	time.sleep(1)
 	app.edit_message_text(message.chat.id, message.id,"💣 2")
 	time.sleep(1)
 	app.edit_message_text(message.chat.id, message.id,"💣 3")
 	app.edit_message_text(message.chat.id, message.id,"💥BOOM💥")
 elif message.text == "فاک2":
 	app.edit_message_text(message.chat.id, message.id,"""🖕🏿🖕🖕🏻🖕🏼🖕🏽""")
 	app.edit_message_text(message.chat.id, message.id,"""🖕🏿🖕🏿🖕🏻🖕🏼🖕🏽""")
 	app.edit_message_text(message.chat.id, message.id,"""🖕🏿🖕🏿🖕🏿🖕🏼🖕🏽 """)
 	app.edit_message_text(message.chat.id, message.id,"""🖕🏿🖕🏿🖕🏿🖕🏿🖕🏽""")
 	app.edit_message_text(message.chat.id, message.id,"""🖕🏿🖕🏿🖕🏿🖕🏿🖕🏿""")
 	time.sleep(2)
 	app.edit_message_text(message.chat.id, message.id,"""Fucking bro🤝""")
 	
 elif message.text == "فاک":
 	app.edit_message_text(message.chat.id, message.id,"""
 	                        /¯) 
                        /   / 
                     /    / 
             /´¯/'   '/´¯¯•¸ 
          /'/   /    /  /     /¨¯\ 
        ('(   (   (   (  ¯~/'  ' / 
         \                         / 
          \                _.•´ 
            \              ( 
              \             \.""")
 elif message.text == "مرگ بر امریکا":
  app.edit_message_text(message.chat.id,message.id,""" ⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠈⠘⠩⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿""")
  app.edit_message_text(message.chat.id,message.id,"""⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠈⠘⠩⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿
⣿⣿⣿⣿⠄⠄⣀⣤⣤⣤⣄⡀⠄⠄⠄⠄⠙⣿⣿⣿
⣿⣿⣿⣿⡀⢰⣿⣿⣿⣿⣿⢿⠄⠄⠄⠄⠄⠹⢿⣿""")
  app.edit_message_text(message.chat.id,message.id,"""⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠈⠘⠩⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿
⣿⣿⣿⣿⠄⠄⣀⣤⣤⣤⣄⡀⠄⠄⠄⠄⠙⣿⣿⣿
⣿⣿⣿⣿⡀⢰⣿⣿⣿⣿⣿⢿⠄⠄⠄⠄⠄⠹⢿⣿
⣿⣿⣿⣿⣿⡞⠻⠿⠟⠋⠉⠁⣤⡀⠄⠄⠄⠄⠄⠄
⣿⣿⣿⣿⣿⣿⣶⢼⣷⡤⣦⣿⠛⡰⢃⠄⠐⠄⠄""")

  app.edit_message_text(message.chat.id,message.id,"""⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠈⠘⠩⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿
⣿⣿⣿⣿⠄⠄⣀⣤⣤⣤⣄⡀⠄⠄⠄⠄⠙⣿⣿⣿
⣿⣿⣿⣿⡀⢰⣿⣿⣿⣿⣿⢿⠄⠄⠄⠄⠄⠹⢿⣿
⣿⣿⣿⣿⣿⡞⠻⠿⠟⠋⠉⠁⣤⡀⠄⠄⠄⠄⠄⠄
⣿⣿⣿⣿⣿⣿⣶⢼⣷⡤⣦⣿⠛⡰⢃⠄⠐⠄⠄⢸
⣿⣿⣿⣿⣿⣿⣿⡯⢍⠿⢾⡿⣸⣿⠰⠄⢀⠄⠄⡬
⣿⣿⣿⣿⣿⣿⣿⣴⣴⣅⣾⣿⣿⡧⠦⡶⠃⠄⠠⢴ """)
  app.edit_message_text(message.chat.id, message.id,"""⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠈⠘⠩⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿
⣿⣿⣿⣿⠄⠄⣀⣤⣤⣤⣄⡀⠄⠄⠄⠄⠙⣿⣿⣿
⣿⣿⣿⣿⡀⢰⣿⣿⣿⣿⣿⢿⠄⠄⠄⠄⠄⠹⢿⣿
⣿⣿⣿⣿⣿⡞⠻⠿⠟⠋⠉⠁⣤⡀⠄⠄⠄⠄⠄⠄
⣿⣿⣿⣿⣿⣿⣶⢼⣷⡤⣦⣿⠛⡰⢃⠄⠐⠄⠄⢸
⣿⣿⣿⣿⣿⣿⣿⡯⢍⠿⢾⡿⣸⣿⠰⠄⢀⠄⠄⡬
⣿⣿⣿⣿⣿⣿⣿⣴⣴⣅⣾⣿⣿⡧⠦⡶⠃⠄⠠⢴
⣿⣿⣿⣿⠿⠍⣿⣿⣿⣿⣿⣿⣿⢇⠟⠁⠄⠄⠄⠄""")
  app.edit_message_text(message.chat.id, message.id,"""⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠈⠘⠩⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿
⣿⣿⣿⣿⠄⠄⣀⣤⣤⣤⣄⡀⠄⠄⠄⠄⠙⣿⣿⣿
⣿⣿⣿⣿⡀⢰⣿⣿⣿⣿⣿⢿⠄⠄⠄⠄⠄⠹⢿⣿
⣿⣿⣿⣿⣿⡞⠻⠿⠟⠋⠉⠁⣤⡀⠄⠄⠄⠄⠄⠄
⣿⣿⣿⣿⣿⣿⣶⢼⣷⡤⣦⣿⠛⡰⢃⠄⠐⠄⠄⢸
⣿⣿⣿⣿⣿⣿⣿⡯⢍⠿⢾⡿⣸⣿⠰⠄⢀⠄⠄⡬
⣿⣿⣿⣿⣿⣿⣿⣴⣴⣅⣾⣿⣿⡧⠦⡶⠃⠄⠠⢴
⣿⣿⣿⣿⠿⠍⣿⣿⣿⣿⣿⣿⣿⢇⠟⠁⠄⠄⠄⠄
⠟⠛⠉⠄⠄⠄⡽⣿⣿⣿⣿⣿⣯⠏⠄⠄⠄⠄⠄⠄
⠄⠄⠄⢀⣾⣾⣿⣤⣯⣿⣿⡿⠃⠄⠄⠄⠄⠄⠄""")
  
 
 elif message.text.startswith("Gpt "):
   try:
    text = message.text.replace("Gpt ","")[1::]
    result = requests.get(f"https://alpha-web.ir/nexapi/?license=nexapi&text={text}").json()['result']['GPT']
    app.send_message(message.chat.id,result,reply_to_message_id=message.id,disable_web_page_preview=True)
   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")

 elif message.text == "arz":
   try:
    r = requests.get(f"https://api.pamickweb.ir/API/arz2.php").json()['result']
    app.app.edit_message_text(message.chat.id,message.id,f"<b>~ Digital Currency Price:\n\n• TRX <code>{r['TRX']}</code>\n• ADA <code>{r['ADA']}</code>\n• XRP <code>{r['XRP']}</code>\n• BTC <code>{r['BTC']}</code>\n• ETH <code>{r['ETH']}</code>\n• USDT <code>{r['USDT']}</code></b>")

   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")

 elif message.text.startswith("id "):
   try:
     user_id_get = (message.reply_to_message.from_user.id if message.reply_to_message else app.get_users(message.text.split()[1]).id)
     user = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
     count_photo = app.get_chat_photos_count(user_id_get)
     app.edit_message_text(message.chat.id,message.id,f"""<b>User Info : <code>{user.users[0].first_name if user.users[0].first_name else "خطا در دریافت"}</code>\n\n- first name : <code>{user.users[0].first_name if user.users[0].first_name else "خطا در دریافت"}</code>\n- last name : <code>{user.users[0].last_name if user.users[0].last_name else "Null"}</code>\n- user id : <code>{user.users[0].id if user.users[0].id else "Null"}</code>\n- username : <code>{f"<code>@{user.users[0].username}</code>" if user.users[0].username else "Null"}\n\n- profile picture count : <code>{count_photo}</code>\n- common chats count : <code>{user.full_user.common_chats_count if user.full_user.common_chats_count else "0"}</code>\n\n- bio : <code>{user.full_user.about if user.full_user.about else "Null"}</code>\n- scam : <code>{user.users[0].scam}</code>\n- can pin message : <code>{user.full_user.can_pin_message}</code>\n- contact : <code>{user.users[0].contact}</code>\n- bot : <code>{user.users[0].bot}</code>\n- verified : <code>{user.users[0].verified}</code>\n- deleted : <code>{user.users[0].deleted}</code>\n- phone calls available : <code>{user.full_user.phone_calls_available}</code>\n- phone calls private : <code>{user.full_user.phone_calls_private}</code>\n- video calls available : <code>{user.full_user.video_calls_available}</code>\n- access hash : <code>{user.users[0].access_hash}</code>\n- blocked : <code>{user.full_user.blocked}</code>\n\n{f"- current chat_id : <code>{message.chat.id}</code>" if message.chat.id != user.users[0].id else ""}</b>""")
   except Exception as error:
     app.edit_message_text(message.chat.id,message.id,f"**~ ERROR : **```error\n{error}```")



 elif message.text == "me":
  user = app.get_me()
  app.edit_message_text(message.chat.id,message.id,f'<b>My Account Info :\n\n- first name : <code>{user.first_name}</code>\n- last name : <code>{user.last_name if user.last_name else "Null"}</code>\n- user id : <code>{user.id}</code>\n- username : <code>{f"@{user.username}" if user.username else "Null"}\n\n- language code : <code>{user.language_code}</code>\n- premium : <code>{user.is_premium}</code>\n- scam : <code>{user.is_scam}</code>\n- verified : <code>{user.is_verified}</code></b>')

 elif message.text == "دلقک": 
  app.edit_message_text(message.chat.id,message.id,"😛")
  app.edit_message_text(message.chat.id,message.id,"😝")
  app.edit_message_text(message.chat.id,message.id,"😜")
  app.edit_message_text(message.chat.id,message.id,"🤪")
  app.edit_message_text(message.chat.id,message.id,"🥴")

 elif message.text == "جق": 
  app.edit_message_text(message.chat.id,message.id,"=✊===>")
  app.edit_message_text(message.chat.id,message.id,"==✊==>")
  app.edit_message_text(message.chat.id,message.id,"===✊=>")
  app.edit_message_text(message.chat.id,message.id,"====✊>")
  app.edit_message_text(message.chat.id,message.id,"=✊===>")
  app.edit_message_text(message.chat.id,message.id,"==✊==>💦")
  app.edit_message_text(message.chat.id,message.id,"===✊=>💦💦")
  app.edit_message_text(message.chat.id,message.id,"====✊>💦💦")
  app.edit_message_text(message.chat.id,message.id,"=✊===>💦💦💦")
  app.edit_message_text(message.chat.id,message.id,"==✊==>💦💦💦💦")
  app.edit_message_text(message.chat.id,message.id,"===✊=>💦💦💦💦💦")
  app.edit_message_text(message.chat.id,message.id,"🥴 مشتی اب هام تموم شد 💦💦💦")



 elif message.text == "قلب":
  app.edit_message_text(message.chat.id,message.id,"❤️")
  app.edit_message_text(message.chat.id,message.id,"🧡")
  app.edit_message_text(message.chat.id,message.id,"💛")
  app.edit_message_text(message.chat.id,message.id,"💚")
  app.edit_message_text(message.chat.id,message.id,"💙")
  app.edit_message_text(message.chat.id,message.id,"💜")
  app.edit_message_text(message.chat.id,message.id,"🤎")
  app.edit_message_text(message.chat.id,message.id,"🖤")
  app.edit_message_text(message.chat.id,message.id,"🤍")
  app.edit_message_text(message.chat.id,message.id,"💘")
  app.edit_message_text(message.chat.id,message.id,"💝")
  app.edit_message_text(message.chat.id,message.id,"💖")
  app.edit_message_text(message.chat.id,message.id,"💗")
  app.edit_message_text(message.chat.id,message.id,"💞")
  app.edit_message_text(message.chat.id,message.id,"💕")
  app.edit_message_text(message.chat.id,message.id,"❤️‍🩹❤️‍🔥💋")

 elif message.text == "سیگما":
  app.edit_message_text(message.chat.id,message.id,""" ⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
 ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
 ⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
 ⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
 ⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
 ⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
 ⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁""")
 elif message.text == "عشق":
   app.edit_message_text(message.chat.id,message.id,"""♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡
♡┏┓┈╭━━╮┓┏┓━━┓♡
♡┃┃┉┃╭╮┃┃┃┃┏━┛♡
♡┃┃┈┃┃┃┃┃┃┃┗━┓♡
♡┃┃┉┃┃┃┃┃┃┃┏━┛♡
♡┃┗━┓╰╯┃╰╯┃┗━┓♡
♡┗━━┛━━╯━━╯━━┛♡
♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡""")



 elif message.text == "کیر":
  app.edit_message_text(message.chat.id,message.id,"""⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⢉⢉⠉⠉⠻⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⠟⠠⡰⣕⣗⣷⣧⣀⣅⠘⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⠃⣠⣳⣟⣿⣿⣷⣿⡿⣜⠄⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⡿⠁⠄⣳⢷⣿⣿⣿⣿⡿⣝⠖⠄⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⠃⠄⢢⡹⣿⢷⣯⢿⢷⡫⣗⠍⢰⣿⣿⣿⣿⣿ 
⣿⣿⣿⡏⢀⢄⠤⣁⠋⠿⣗⣟⡯⡏⢎⠁⢸⣿⣿⣿⣿⣿ 
⣿⣿⣿⠄⢔⢕⣯⣿⣿⡲⡤⡄⡤⠄⡀⢠⣿⣿⣿⣿⣿⣿ 
⣿⣿⠇⠠⡳⣯⣿⣿⣾⢵⣫⢎⢎⠆⢀⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢨⣫⣿⣿⡿⣿⣻⢎⡗⡕⡅⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢜⢾⣾⣿⣿⣟⣗⢯⡪⡳⡀⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢸⢽⣿⣷⣿⣻⡮⡧⡳⡱⡁⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⡄⢨⣻⣽⣿⣟⣿⣞⣗⡽⡸⡐⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⡇⢀⢗⣿⣿⣿⣿⡿⣞⡵⡣⣊⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⡀⡣⣗⣿⣿⣿⣿⣯⡯⡺⣼⠎⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣧⠐⡵⣻⣟⣯⣿⣷⣟⣝⢞⡿⢹⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⡆⢘⡺⣽⢿⣻⣿⣗⡷⣹⢩⢃⢿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣷⠄⠪⣯⣟⣿⢯⣿⣻⣜⢎⢆⠜⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⡆⠄⢣⣻⣽⣿⣿⣟⣾⡮⡺⡸⠸⣿⣿⣿⣿ 
⣿⣿⡿⠛⠉⠁⠄⢕⡳⣽⡾⣿⢽⣯⡿⣮⢚⣅⠹⣿⣿⣿ 
⡿⠋⠄⠄⠄⠄⢀⠒⠝⣞⢿⡿⣿⣽⢿⡽⣧⣳⡅⠌⠻⣿""")

 elif message.text == "نه":
   app.edit_message_text(message.chat.id,message.id,"""😥┈┈┈┈😫┈┈😒😣😒
😒😒┈┈😒┈😒┈┈┈┈😲
😩┈😢┈😲┈⁣😤┈┈┈┈😠
😒┈┈😒😒┈😞┈┈┈┈😤
😭┈┈┈┈😖--😒😔😫
""")



 elif (data["strike"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<s>{message.text}</s>")
  data.update({"strike": "1", "bold": "0", "mention": "0", "spoiler": "0", "italic": "0", "underline": "0", "code": "0", "php": "0", "html": "0"})

 elif (data["bold"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<b>{message.text}</b>")

 elif (data["mention"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>")



 elif (data["spoiler"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"||{message.text}||")

 elif (data["italic"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<i>{message.text}</i>")

 elif (data["underline"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<u>{message.text}</u>")
  
 elif (data["code"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"<code>{message.text}</code>")

 elif (data["php"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"```php\n' {message.text} '\n```")

 elif (data["html"] == "1"):
  app.edit_message_text(message.chat.id, message.id, f"```html\n <- {message.text} ->\n```")
  

 	

app.start(), print("Self Bot is STARTED . . .✅"), app.send_message("me" , "سلام مشتی ❤\nسلف روی اکانتت ران شد 🔥\nحالا بنویس (پنل)یا(panel)تا دستورات سلف رو بهت بدم😘🔥\nسازندم: @La_shy"),idle(), app.stop()
