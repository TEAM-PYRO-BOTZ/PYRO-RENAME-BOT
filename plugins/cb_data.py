from helper.progress import progress_for_pyrogram
from pyrogram import Client, filters
from pyrogram.types import (  InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper.database import find
import os
from PIL import Image
import time

@Client.on_callback_query(filters.regex('cancel'))
async def cancel(bot,update):
	try:
		await update.message.delete()
	except:
		return
@Client.on_callback_query(filters.regex('rename'))
async def rename(bot,update):
	user_id = update.message.chat.id
	date = update.message.date
	await update.message.delete()
	await update.message.reply_text("__Please enter the new filename...__",	
	reply_to_message_id=update.message.reply_to_message.message_id,  
	reply_markup=ForceReply(True))
	
@Client.on_callback_query(filters.regex("doc"))
async def doc(bot,update):
     new_name = update.message.text
     name = new_name.split(":-")
     new_filename = name[1]
     file_path = f"downloads/{new_filename}"
     file = update.message.reply_to_message
     ms = await update.message.edit("``` Trying To Download...```")
     c_time = time.time()
     try:
     	path = await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=( "``` Trying To Download...```",  ms, c_time   ))
     except Exception as e:
     	await ms.edit(e)
     	return
     	
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     user_id = int(update.message.chat.id)
     thumb = find(user_id)
     if thumb:
     		ph_path = await bot.download_media(thumb)
     		Image.open(ph_path).convert("RGB").save(ph_path)
     		img = Image.open(ph_path)
     		img.resize((320, 320))
     		img.save(ph_path, "JPEG")
     		c_time = time.time()
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_document(update.message.chat.id,document = file_path,thumb=ph_path,caption = f"**{new_filename}**",progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     			os.remove(ph_path)
     		except Exception as e:
     			await ms.edit(e)
     			os.remove(file_path)
     			os.remove(ph_path)
     			     		     		
     else:
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_document(update.message.chat.id,document = file_path,caption = f"**{new_filename}**",progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     		except Exception as e:
     			await ms.edit(e)
     			os.remove(file_path)
     			     		   		
     		
@Client.on_callback_query(filters.regex("vid"))
async def vid(bot,update):
     new_name = update.message.text
     name = new_name.split(":-")
     new_filename = name[1]
     file_path = f"downloads/{new_filename}"
     file = update.message.reply_to_message
     ms = await update.message.edit("``` Trying To Download...```")
     c_time = time.time()
     try:
     	path = await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=( "``` Trying To Download...```",  ms, c_time   ))
     except Exception as e:
     	await ms.edit(e)
     	return
     
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     duration = 0
     metadata = extractMetadata(createParser(file_path))
     if metadata.has("duration"):
     		duration = metadata.get('duration').seconds
     user_id = int(update.message.chat.id)
     thumb = find(user_id)
     if thumb:
     		ph_path = await bot.download_media(thumb)
     		Image.open(ph_path).convert("RGB").save(ph_path)
     		img = Image.open(ph_path)
     		img.resize((320, 320))
     		img.save(ph_path, "JPEG")
     		c_time = time.time()
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_video(update.message.chat.id,video = file_path,caption = f"**{new_filename}**",thumb=ph_path,duration =duration, progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     			os.remove(ph_path)   				
     		except Exception as e:
     				await ms.edit(e)
     				os.remove(file_path)
     				os.remove(ph_path)
     				
     else:
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_video(update.message.chat.id,video = file_path,caption = f"**{new_filename}**",duration = duration, progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     		except Exception as e:
     			await ms.edit(e)
     			os.remove(file_path)
   
     			     		     		
@Client.on_callback_query(filters.regex("aud"))
async def aud(bot,update):
     new_name = update.message.text
     name = new_name.split(":-")
     new_filename = name[1]
     file_path = f"downloads/{new_filename}"
     file = update.message.reply_to_message
     ms = await update.message.edit("``` Trying To Download...```")
     c_time = time.time()
     try:
     	path = await bot.download_media(message = file , progress=progress_for_pyrogram,progress_args=( "``` Trying To Download...```",  ms, c_time   ))
     except Exception as e:
     	await ms.edit(e)
     	return
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     duration = 0
     metadata = extractMetadata(createParser(file_path))
     if metadata.has("duration"):
     	duration = metadata.get('duration').seconds
     user_id = int(update.message.chat.id)
     thumb = find(user_id)
     if thumb:
     		ph_path = await bot.download_media(thumb)
     		Image.open(ph_path).convert("RGB").save(ph_path)
     		img = Image.open(ph_path)
     		img.resize((320, 320))
     		img.save(ph_path, "JPEG")
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_audio(update.message.chat.id,audio = file_path,caption = f"**{new_filename}**",thumb=ph_path,duration =duration, progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     			os.remove(ph_path)
     		except Exception as e:
     			await ms.edit(e)
     			os.remove(file_path)
     			os.remove(ph_path)
     else:
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_audio(update.message.chat.id,audio = file_path,caption = f"**{new_filename}**",duration = duration, progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     		except Exception as e:
     			await ms.edit(e)
     			os.remove(file_path)		
