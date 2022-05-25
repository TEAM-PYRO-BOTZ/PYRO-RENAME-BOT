from pyrogram import Client, filters 
from helper.database import find, addcaption, delcaption 

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Give me a caption to set.\n\nExample:- `/set_caption 📕 File Name: {filename}\n\n💾 Size: {filesize}\n\n⏰ Duration: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**Your Caption successfully added ✅**")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message): 
    #caption = fint(int(message.chat.id))[1]
    #if not caption:
       #return await message.reply_text("**You dont have any custom caption**")
    delcaption(int(message.chat.id))
    await message.reply_text("**Your caption successfully deleted ✅**")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>Your Caption:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("**You dont have any custom caption**")
