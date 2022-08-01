from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
       new_name = message.text 
       await message.delete() 
       msg = await client.get_messages(message.chat.id, reply_message.id)
       file = msg.reply_to_message
       media = file.media
       await reply_message.delete()
       button = [[InlineKeyboardButton("📁 𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃𝚂",callback_data = "upload_document")]]
       if str(media) in ["MessageMediaType.VIDEO", "MessageMediaType.DOCUMENT"]:
           button.append([InlineKeyboardButton("🎥 𝚅𝙸𝙳𝙴𝙾",callback_data = "upload_video")])
       elif str(media) == "MessageMediaType.AUDIO":
           button.append([InlineKeyboardButton("🎵 𝙰𝙾𝚄𝙳𝙸𝙾",callback_data = "upload_audio")])
       await message.reply_text(
          f"**Select the output file type**\n**Output FileName** :- ```{new_name}```",
          reply_to_message_id=file.id,
          reply_markup=InlineKeyboardMarkup(button))
