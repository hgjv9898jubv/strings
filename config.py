from pyrogram import Client
from asBASE import asJSON

db = asJSON("as.json")
###


SUDORS = [5541009328] # ايديات المطورين
API_ID = 9028013
API_HASH = "cc894fc40424f9c8bbcf06b7355bd69d"
TOKEN = "" # التوكن
bot = Client("control",API_ID,API_HASH,bot_token=TOKEN,in_memory=True)
bot_id = TOKEN.split(":")[0]