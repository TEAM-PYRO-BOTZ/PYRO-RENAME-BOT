from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

BOT_UN = os.environ.get("BOT_UN", "")

FORCE_SUB = os.environ.get("FORCE_SUB", "")           

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    print(
        """
------------------
| BOT WAS STATED |
------------------
"""
    )
    app.run()
