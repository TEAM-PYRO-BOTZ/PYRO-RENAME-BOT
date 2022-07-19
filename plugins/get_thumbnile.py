from pyrogram import Client, filters 

@Client.on_message(filters.photo)
async def photoid(client, message):     
    await message.reply(
        text=f"**PHOTO ID** :- \n `{message.photo.file_id}`")
