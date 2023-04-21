import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.getenv("API_ID", "")

API_HASH = os.getenv("API_HASH", "")

BOT_TOKEN = os.getenv("BOT_TOKEN", "") 

FORCE_SUB = os.getenv("FORCE_SUB", "") 

DB_NAME = os.getenv("DB_NAME","")     

DB_URL = os.getenv("DB_URL","")
 
FLOOD = int(os.getenv("FLOOD", "10"))

START_PIC = os.getenv("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.getenv('ADMIN', '').split()]

PORT = os.getenv('PORT', '8080')

WEBHOOK = bool(os.getenv("WEBHOOK", True))
