from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import humanize
from Translation import mr
from helper.database import  insert 
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴 𝚈𝙾𝚄𝚁 𝙽𝙾𝚃 𝙹𝙾𝙸𝙽𝙳 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻. 𝙿𝙻𝙴𝙰𝚂𝙴 𝙹𝙾𝙸𝙽 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 🙏 **",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=client.invitelink)]
           ])
       )
    
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo="https://telegra.ph/file/2e2a07e86066538ed7406.jpg",
       caption=f"""👋 Hai {message.from_user.mention} \n𝙸'𝚖 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎+𝙵𝚒𝚕𝚎 𝚃𝚘 𝚅𝚒𝚍𝚎𝚘 𝙲𝚘𝚟𝚎𝚛𝚝𝚎𝚛 𝙱𝙾𝚃 𝚆𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 & 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 𝚂𝚞𝚙𝚙𝚘𝚛𝚝!🤩 \n𝙱𝙾𝚃 𝙲𝚛𝚎𝚊𝚝𝚎𝚍 𝙱𝚢: @mr_MKN & @Mr_MKN_TG \n 🤩""",
       reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton("👨‍💻 𝙾𝚆𝙽𝙴𝚁 👨‍💻", url='https://t.me/mr_MKN')
          ],[
          InlineKeyboardButton("👼 Developers 👼", callback_data='dev')
          ],[
          InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/mkn_bots_updates'),
          InlineKeyboardButton('ℹ️ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url='https://t.me/MKN_BOTZ_DISCUSSION_GROUP')
          ],[
          InlineKeyboardButton('🛡️ 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
          InlineKeyboardButton('ℹ️ 𝙷𝙴𝙻𝙿', callback_data='help')
          ]]
          )
       )
    return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply_text(
        f"__What do you want me to do with this file?__\n**File Name** :- `{filename}`\n**File Size** :- `{filesize}`",
        reply_to_message_id = message.id,
        reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 𝚁𝙴𝙽𝙰𝙼𝙴",callback_data = "rename"),
        InlineKeyboardButton("𝙲𝙰𝙽𝙲𝙴𝙻 ✖️",callback_data = "cancel")  ]]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""👋 Hai {query.from_user.mention} \n𝙸'𝚖 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎+𝙵𝚒𝚕𝚎 𝚃𝚘 𝚅𝚒𝚍𝚎𝚘 𝙲𝚘𝚟𝚎𝚛𝚝𝚎𝚛 𝙱𝙾𝚃 𝚆𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 & 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 𝚂𝚞𝚙𝚙𝚘𝚛𝚝! \n𝙱𝙾𝚃 𝙲𝚛𝚎𝚊𝚝𝚎𝚍 𝙱𝚢: @mr_MKN & @Mr_MKN_TG \n 🤩""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("👨‍💻 𝙾𝚆𝙽𝙴𝚁 👨‍💻", url='https://t.me/mr_MKN')
                ],[
                InlineKeyboardButton("👼 Developers 👼", callback_data='dev')
                ],[
                InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/mkn_bots_updates'),
                InlineKeyboardButton('ℹ️ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url='https://t.me/MKN_BOTZ_DISCUSSION_GROUP')
                ],[
                InlineKeyboardButton('🛡️ 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
                InlineKeyboardButton('ℹ️ 𝙷𝙴𝙻𝙿', callback_data='help')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
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
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





