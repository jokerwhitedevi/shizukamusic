# ðððð ðððð ðððð ððððð ððððððððð @SHAILENDRA34 |
# ðððð« ððð«ð¨ ð©ð©ð¥ð¬ ðð¥ð¢ð¬ð¡ ðð¨ð§'ð­ ð«ðð¦ð¨ð¯ð ð­ð¡ð¢ð¬ ð¥ð¢ð§ð ðð«ð¨ð¦ ð¡ðð«ð ð


from asyncio.queues import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.command import commandpro
from helpers.filters import other_filters
from callsmusic import callsmusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton,
                            ReplyKeyboardMarkup, ReplyKeyboardRemove)


PAUSED = "https://telegra.ph/file/94ee2bdfc7e81d371aae3.jpg"
RESUMED = "https://telegra.ph/file/50cf13056d78898e13ae0.jpg"
SKIPPED = "https://telegra.ph/file/116d7d9b9100c44249333.jpg"
END = "https://telegra.ph/file/6d1902d08c88f318d53c7.jpg"

BUTTON = [
    [
        InlineKeyboardButton(text="á´á´á´á´á´á´s", url=f"https://t.me/HeroOfficialBots"),
        InlineKeyboardButton(text="ðï¸Close", callback_data="close_"),
        InlineKeyboardButton(text="sá´á´á´á´Êá´", url=f"https://t.me/Yaaro_ki_yaarii"), 
    ],
]

ACTV_CALLS = []

@Client.on_message(commandpro(["/pause", "!pause", "pause"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    
    await message.reply_photo(
        photo=PAUSED,
        caption=f"sá´Êá´á´á´ á´á´á´sá´á´ ÊÊ {message.from_user.mention} ð¥\n\nâ¦ /resume :- Êá´sá´á´á´ á´á´á´sá´á´ sá´Êá´á´á´",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()


@Client.on_message(commandpro(["/resume", "!resume", "resume"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    
    await message.reply_photo(
        photo=RESUMED,
        caption=f"Êá´sá´á´á´á´ á´á´á´sá´á´ sá´Êá´á´á´ ÊÊ {message.from_user.mention} ð«.\n\nâ¦ /pause :- á´á´á´sá´ á´Êá´ÊÊá´á´á´!!",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()


@Client.on_message(commandpro(["/end", "!end", "/stop", "!stop", "stop", "end"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chut_id = message.chat.id
    if int(chut_id) not in ACTV_CALLS:
        await message.reply_text(
            "á´¡á´Ò, á´Êá´Ê á´Êá´ sá´É´É¢ ÒÉªÊsá´ ÉªÉ´ á´Êá´á´Ê á´á´ sá´Éªá´ á´Êá´á´ ð«",
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
        await message.delete()
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        await callsmusic.pytgcalls.leave_group_call(message.chat.id)
    
        await message.reply_photo(
            photo=END,
            caption=f"sá´Êá´á´á´ á´É´á´á´á´ ÊÊ {message.from_user.mention} \n É´á´á´¡ Êá´á´á´ ÉªÉ´É¢ á´ á´ ÊÊá´ ÊÊá´ ðð»",
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
        await message.delete()
    

@Client.on_message(commandpro(["/skip", "!skip", "skip"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        
        await message.reply_text(
            "á´¡á´Ò, á´Êá´Ê á´Êá´ sá´É´É¢ ÒÉªÊsá´ ÉªÉ´ á´Êá´á´Ê á´á´ sá´Éªá´ á´Êá´á´ ð",
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
        await message.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
    
    await message.reply_photo(
        photo=SKIPPED,
        caption=f"á´á´á´ á´á´ á´á´ á´Êá´ É´á´xá´ sá´É´É¢\nsá´Êá´á´á´ sá´Éªá´á´á´á´ ÊÊ {message.from_user.mention}ð¥",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()
