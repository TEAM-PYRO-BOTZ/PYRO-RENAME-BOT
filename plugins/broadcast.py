import re
import os
from pyrogram.types import Message
from pyrogram import Client ,filters
from helper.database import getid

id_pattern = re.compile(r'^.\d+$')

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(client: Client, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text="weit....")
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")
