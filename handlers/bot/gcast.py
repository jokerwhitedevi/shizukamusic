# ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐๐ @SHAILENDRA34 | 
# ๐๐๐๐ซ ๐๐๐ซ๐จ ๐ฉ๐ฉ๐ฅ๐ฌ ๐๐ฅ๐ข๐ฌ๐ก ๐๐จ๐ง'๐ญ ๐ซ๐๐ฆ๐จ๐ฏ๐ ๐ญ๐ก๐ข๐ฌ ๐ฅ๐ข๐ง๐ ๐๐ซ๐จ๐ฆ ๐ก๐๐ซ๐ ๐
 
 
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from config import SUDO_USERS

HERO_IMG = "https://te.legra.ph/file/a4c16c60dd1c46bbe7385.jpg"

@Client.on_message(filters.command("gcast"))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        sas = await message.reply("`sแดแดสแดแดแด สสแดแดแดแดแดsแดษชษดษข แดกแดษชแด๐ฉโ๐ป`")
        if not message.reply_to_message:
            await sas.edit("**__ษขษชแดแดษช แดษดส แดแดssแดษขแด แดแด ษขแดแดsแด๐คทโโ๏ธ...__**")
            return
        hero = message.reply_to_message.text
        async for dialog in Client.iter_dialogs():
            try:
                await Client.send_message(dialog.chat.id, hero)
                sent = sent+1
                await hyper.edit(f"`สสแดแดแดแดแดsแดษชษดษข` \n\n**sแดแดแดแดssาแดสส ษชษด:** `{sent}` แดสแดแดs๐พ \n**แดษดsแดแดแดแดssาแดสส ษชษด:** {failed} แดสแดแดs๐๏ธ")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_photo(HERO_IMG, caption=f"sแดแดแดแดsาแดสสส แดแดษดแด๐งโโโญ \n\nsแดแดแดแดssาแดสส**:** `{sent}` แดสแดแดs \n**าแดษชสแดแด :** {failed} แดสแดแดs")
