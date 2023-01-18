"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from helper.txt import mr
from helper.database import db
from config import START_PIC, FLOOD, ADMIN 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    txt=f"👋 Hai {user.mention} \n𝙸'𝚖 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎+𝙵𝚒𝚕𝚎 𝚃𝚘 𝚅𝚒𝚍𝚎𝚘 𝙲𝚘𝚟𝚎𝚛𝚝𝚎𝚛 𝙱𝙾𝚃 𝚆𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 & 𝙲𝚞𝚜𝚝𝚘𝚖 𝙲𝚊𝚙𝚝𝚒𝚘𝚗 𝚂𝚞𝚙𝚙𝚘𝚛𝚝!"
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton("👼 𝙳𝙴𝚅𝚂 👼", callback_data='dev')
        ],[
        InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/PYRO_BOTZ'),
        InlineKeyboardButton('🍂 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url='https://t.me/PYRO_BOTZ_CHAT')
        ],[
        InlineKeyboardButton('🍃 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
        InlineKeyboardButton('ℹ️ 𝙷𝙴𝙻𝙿', callback_data='help')
        ]])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)
   

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""👋 Hai {query.from_user.mention} \n𝙸'𝚖 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎+𝙵𝚒𝚕𝚎 𝚃𝚘 𝚅𝚒𝚍𝚎𝚘 𝙲𝚘𝚟𝚎𝚛𝚝𝚎𝚛 𝙱𝙾𝚃 𝚆𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 & 𝙲𝚞𝚜𝚝𝚘𝚖 𝙲𝚊𝚙𝚝𝚒𝚘𝚗 𝚂𝚞𝚙𝚙𝚘𝚛𝚝! """,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("👼 𝙳𝙴𝚅𝚂 👼", callback_data='dev')                
                ],[
                InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/PYRO_BOTZ'),
                InlineKeyboardButton('🍂 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url='https://t.me/PYRO_BOTZ_CHAT')
                ],[
                InlineKeyboardButton('🍃 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
                InlineKeyboardButton('ℹ️ 𝙷𝙴𝙻𝙿', callback_data='help')
                ]]
                )
            )
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ 𝚂𝙾𝚄𝚁𝙲𝙴", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("❤️‍🔥 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴  ❤️‍🔥", url='https://youtu.be/BiC66uFJsio')
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ 𝚂𝙾𝚄𝚁𝙲𝙴", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("🖥️ 𝙷𝙾𝚆 𝚃𝙾 𝙼𝙰𝙺𝙴", url="https://youtu.be/GfulqsSnTv4")
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ 𝚂𝙾𝚄𝚁𝙲𝙴", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("🖥️ 𝙷𝙾𝚆 𝚃𝙾 𝙼𝙰𝙺𝙴", url="https://youtu.be/GfulqsSnTv4")
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





