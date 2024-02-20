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
IQ = InlineKeyboardMarkup(
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
                KeyboardButton("پـایـرۆگـرام"), KeyboardButton("تـێـلـێـثـۆن")
            ],
            [KeyboardButton("دەرباری بۆت")]
        ],
        resize_keyboard=True, placeholder='دەرهێنانی کۆد 🧑🏻‍💻'
    )
    await message.reply('''**
- مرحـبـًا عـزيـزي 🙋 {},
في بوت استخـراج جلسات 
- لبـدء استخـراج الجلسة اختـر الجلسـة بالاسفل.
- إذا كنـت تريـد أن يكون حسـابك في أمـان تام فاختر بايروجـرام أمـا إذا كـان رقمك حقيقـي فاختر تيليثون .
 - ملاحظـة :
- احـذر مشاركـة الكود لأحـد لأنه يستطيـع اختراق حسـابك ⚠️ .
**'''.format(message.from_user.mention), reply_markup=reply_markup, quote=True)

@app.on_message(filters.text & filters.private)
async def generator_and_about(app, m):
    if m.text == "دەرباری بۆت":
        text = ''
        text += "**🐍 زمانی پڕۆگرامینگ - پایثۆن**"
        text += f"**\n🔥 ڤێرژنی پایرۆگرام** {v}"
        text += f"**\n🌱 ڤێرژنی تێلیثۆن** {v2}"
        text += f"**\n\n🧑🏻‍💻🖤 گەشەپێدەری بۆت :  [﮼محمد](t.me/MGIMT)**"
        text += f"**\n\n⧉• کەناڵی سەرچاوە : @MGIMT**"
        photo=f"https://telegra.ph/file/11448420ddc987f97d1de.jpg"
        await app.send_photo(m.chat.id, photo, text, reply_markup=IQ)

    if m.text == "پـایـرۆگـرام":
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
        await c.send_message('me', f'**بە سەرکەوتوویی کۆدی پـایـرۆگـرام دەرهێنرا** `{v}` **ئەمە کۆدەکەیە**\n\n`{string_session}`')
        await c.disconnect()
        await app.send_message(
            m.chat.id,
            text,
            reply_markup=IQ
        )

    if m.text == "تـێـلـێـثـۆن":
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
        await c.send_message('me', f'**بە سەرکەوتوویی کۆدی تـێـلـێـثـۆن دەرهێنرا** `{v2}` **ئەمە کۆدەکەیە**\n\n`{string_session}`')
        await c.disconnect()

        await app.send_message(
            m.chat.id,
            text,
            reply_markup=IQ
        )
          


app.start()
bot.start()
print("بۆت چالاککرا لەلایەن : @IQ7amo")
idle()
