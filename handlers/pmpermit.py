#unitedbots #callsmusic #psychobots
from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"[✨](https://telegra.ph/file/9ccdc6fac98c35369de95.png) Heya! This is the Music Assistant of [Musiqo](https://t.me/InayaMusic_bot)")
  return                        
