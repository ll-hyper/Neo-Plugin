import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from ChampuMusic import app
from ChampuMusic.utils.database import add_served_chat, get_assistant


start_txt = """**
✪ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗖𝗵𝗮𝗺𝗽𝘂 𝗥𝗲𝗽𝗼𝘀 ✪

➲ ᴇᴀsʏ ʜᴇʀᴏᴋᴜ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ✰  
➲ ɴᴏ ʙᴀɴ ɪssᴜᴇs ✰  
➲ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰  
➲ 𝟸𝟺/𝟽 ʟᴀɢ-ғʀᴇᴇ ✰

► sᴇɴᴅ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍs!
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{app.username}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝖧𝖸𝖯𝖤𝖱", url="https://t.me/TheChampu"),
          InlineKeyboardButton("𝖥𝖤𝖤𝖫𝖨𝖭𝖦𝖲", url="https://t.me/se_feelings"),
          ],
               [
                InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/GOD_HYPER_O_P"),

],[
              InlineKeyboardButton("ᴍᴜsɪᴄ", url=f"Https://github.com/ll-hyper/neo_music"),
              InlineKeyboardButton("sᴛʀɪɴɢ", url=f"Https://github.com/ll-hyper/neo_music"),
              ],
[
              InlineKeyboardButton("sɪᴍᴘʟᴇ ᴍᴜsɪᴄ", url=f"https://t.me/se_feelings")
              ],
              [
              InlineKeyboardButton("ᴍᴀɴᴀɢᴍᴇɴᴛ", url=f"Https://github.com/ll-hyper/neo_music"),
InlineKeyboardButton("ᴄʜᴀᴛʙᴏᴛ", url=f"Https://github.com/ll-hyper/neo_music"),
]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo=config.START_IMG_URL,
        caption=start_txt,
        reply_markup=reply_markup
    )



