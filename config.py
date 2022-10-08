import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "12755929")

API_HASH = os.environ.get("API_HASH", "13c33467ca4268ede6d7b4f20aa11565")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5512601636:AAGruEJcLnCahiLGcf8o6vUPfevZfn7pxTA") 

FORCE_SUB = os.environ.get("FORCE_SUB", rai_info17) 

DB_NAME = os.environ.get("DB_NAME","rai1")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://adv:adv@cluster0.txud8.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "0"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/5553dc39f968b364d4856.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '761686219').split()]
