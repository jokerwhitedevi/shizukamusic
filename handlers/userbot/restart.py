# ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐๐ @SHAILENDRA34 
# ๐๐๐๐ซ ๐๐๐ซ๐จ ๐ฉ๐ฉ๐ฅ๐ฌ ๐๐ฅ๐ข๐ฌ๐ก ๐๐จ๐ง'๐ญ ๐ซ๐๐ฆ๐จ๐ฏ๐ ๐ญ๐ก๐ข๐ฌ ๐ฅ๐ข๐ง๐ ๐๐ซ๐จ๐ฆ ๐ก๐๐ซ๐ ๐


import os
import sys
from pyrogram.types import Message
from helpers.command import commandpro
from pyrogram import Client
from os import system, execle, environ
from helpers.decorators import errors, sudo_users_only


@Client.on_message(commandpro(["R", "!restart", ".restart", "Restart", "/restart"]))
@errors
@sudo_users_only
async def restart_bot(_, message: Message):
    msg = await message.reply("`สแดsแดแดสแดษชษดษข สแดแด...`")
    args = [sys.executable, "main.py"]
    await msg.edit("โ สแดแด สแดsแดแดสแดแดแด...\nโ ษดแดแดก สแดแด แดแดษด แดsแด แดสษชs สแดแด แดาแดแดส ๐ท แดษชษดแดแดแด ")
    execle(sys.executable, *args, environ)
    return