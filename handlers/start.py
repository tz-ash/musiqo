# Lᴜᴄɪᴅᴏ™

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>[💌](https://telegra.ph/file/9ccdc6fac98c35369de95.png) Welcome {message.from_user.first_name}!
**musiqo** is a bot designed for **stream** on your group, as **simple** as possible, through the **voice chats** in your group.

**❓How to use it❓**
Press the » **COMMANDS** to view the full list of the commands of the bot!
and Join [support](https://t.me/tzkid) to know about this bot 
🔺 Use /source for bot source code and pyrstring🔻
<\b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "COMMANDS", url="https://telegra.ph/𝚖𝚞𝚜𝚒𝚚𝚘-Sᴏɴɢ-06-09",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Support Group", url="https://t.me/tzkid"
                    ),
                    InlineKeyboardButton(
                        "Updates Channel", url="https://t.me/kidbots"
                    ),
                    InlineKeyboardButton(
                        "Kid Hub", url="https://t.me/kidhub"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Add to your group", url="https://t.me/InayaMusic_bot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Know how to use",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support", url="https://t.me/kidbots"
                    ),
                    InlineKeyboardButton(
                        "Report bugs", url="https://t.me/tzkid"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "Close", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("source")
    & filters.private
    & ~ filters.edited
)
async def source(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
**Here is bot source code and pyrostring generator For help contact at support group**
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "github repo", url="https://github.com/tz-ash/musiqo"
                    ),
                    InlineKeyboardButton(
                        "string generator", url="https://replit.com/@tzkid/KidzStringSession"
                    )
                ]
            ]
        )
    )
