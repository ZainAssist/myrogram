import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn = [[InlineKeyboardButton('🇮🇳 Chatting Group', url=f'https://t.me/+-o9-tiKTRrhmY2Zl')]]
STARTER = InlineKeyboardMarkup(btn)

BOTBY = "@The_Eternity_Soul"

def forceMe(id):
    url = f"https://forcesubb-cce9cd4d4881.herokuapp.com/api/private/bots?id={id}"
    res = requests.get(url).json()
    return res


def notJoin(c,m):
    button = [[InlineKeyboardButton('🇮🇳 Chatting Group', url=f'https://t.me/+-o9-tiKTRrhmY2Zl')]]
    markup = InlineKeyboardMarkup(button)
    return c.send_message(chat_id=m.chat.id, text="""Hi Broh 👋 \n👉<i> You need to join</i> <b>@About_Zain</b> \n<i>Do /start after joining the channel</i>""", reply_markup=markup)
