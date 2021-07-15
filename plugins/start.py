from pyrogram import Client, filters

from helper.database import  insert 

@Client.on_messsage(filter.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	Hello {message.from_user.first_name }
	__I am file renamer bot, Please sent any telegram 
	**Document Or Video** and enter new filenameto rename it__
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ], 
	[InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical") ]  ]))

	
