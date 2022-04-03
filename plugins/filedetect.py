from pyrogram import Client, filters
from pyrogram.types import (  InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram.errors import UserNotParticipant

force_channel = "mkn_bots_updates"

@Client.on_message(filters.private & filters.reply)
async def refunc(client,message):
    if force_channel:   
        try:             
            user = await _.get_chat_member(force_channel, message.from_user.id)
            if user.status == "kicked":
               await message.reply_text("Sorry, You're Banned")
               return
        except UserNotParticipant:
            await message.reply_text(
                text="**sorry bro നിങ്ങൾ ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ ചെയ്തിട്ടില്ല താഴെയുള്ള ബട്ടനിൽ ക്ലിക്ക് ചെയ്ത് join ചെയ്യൂ എന്നിട്ട് വീണ്ടും start കൊടുക്കൂ 🙏**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=f"https://t.me/{force_channel}")]
              ])
            )
            return
        else:

        if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
        	new_name = message.text
        	await message.delete()
        	media = await client.get_messages(message.chat.id,message.reply_to_message.message_id)
        	file = media.reply_to_message.document or media.reply_to_message.video or media.reply_to_message.audio
        	filename = file.file_name
        	types = file.mime_type.split("/")
        	mime = types[0]
        	mg_id = media.reply_to_message.message_id
        	try:
        		out = new_name.split(".")
        		out_name = out[1]
        		out_filename = out[0] + "."+ out_name
        		await message.reply_to_message.delete()
        		if mime == "video":
        			markup = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("📁 Documents",callback_data = "doc"), 
        			InlineKeyboardButton("🎥 Video",callback_data = "vid") ]])
        		elif mime == "audio":
        			markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📁 Documents",callback_data = "doc")
        			,InlineKeyboardButton("🎵 audio",callback_data = "aud") ]])
        		else:
        			markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📁 Documents",callback_data = "doc") ]])
        		# dont chenge this message.reply_text     			        		
        		await message.reply_text(f"**Select the output file type**\n**Output FileName** :- ```{out_filename}```",reply_to_message_id=mg_id,reply_markup = markup)
        		
        	except:
        		try:
        			out = filename.split(".")
        			out_name = out[1]
        			out_filename= new_name + "."+ out_name
        		except:
        			await message.reply_to_message.delete()
        			await message.reply_text("**Error** :  No  Extension in File, Not Supporting"
        			,reply_to_message_id=mg_id)
        			return
        		await message.reply_to_message.delete()
        		if mime == "video":
        			markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📁 Documents",callback_data = "doc")
        			,InlineKeyboardButton("🎥 Video",callback_data = "vid") ]])
        		elif mime == "audio":
        			markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📁 Documents",callback_data = "doc")
        			,InlineKeyboardButton("🎵 audio",callback_data = "aud") ]])
        		else:
        			markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📁 Documents",callback_data = "doc") ]])
        		# dont chenge this message.reply_text 
        		await message.reply_text(f"**Select the output file type**\n**Output FileName** :- ```{out_filename}```",
        		reply_to_message_id=mg_id,reply_markup = markup)
        		
