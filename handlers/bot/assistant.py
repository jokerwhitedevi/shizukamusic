# ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐๐ @SHAILENDRA34 |
# ๐๐๐๐ซ ๐๐๐ซ๐จ ๐ฉ๐ฉ๐ฅ๐ฌ ๐๐ฅ๐ข๐ฌ๐ก ๐๐จ๐ง'๐ญ ๐ซ๐๐ฆ๐จ๐ฏ๐ ๐ญ๐ก๐ข๐ฌ ๐ฅ๐ข๐ง๐ ๐๐ซ๐จ๐ฆ ๐ก๐๐ซ๐ ๐


import asyncio
from pyrogram.types import Message
from pyrogram import Client, filters
from helpers.filters import command, other_filters
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import authorized_users_only
from callsmusic.callsmusic import client as user

STR_ID = "CAACAgIAAx0CW9EqKAACEoZiT-Pqtg1RKtr06xxZWMwSAhye2AACghsAAiKAeEqwv4PkzvkmQiME"

@Client.on_message(
    command(["join", "joinassistant", "userbotjoin"]) & ~filters.bot
)
@authorized_users_only
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invite_link = await m.chat.export_invite_link()
        if "+" in invite_link:
            link_hash = (invite_link.replace("+", "")).split("t.me/")[1]
            await user.join_chat(f"https://t.me/joinchat/{link_hash}")
        await m.chat.promote_member(
            (await user.get_me()).id,
            can_manage_voice_chats=True
        )
        return await user.send_message(chat_id, "แดssษชsแดแดษดแด แดแดษชษดแดแด แดสษชs ษขสแดแดแด ษดแดแดก แดษดแดแดส แดแดsษชแด ๐ซ")
    except UserAlreadyParticipant:
        admin = await m.chat.get_member((await user.get_me()).id)
        if not admin.can_manage_voice_chats:
            await m.chat.promote_member(
                (await user.get_me()).id,
                can_manage_voice_chats=True
            )
            return await user.send_message(chat_id, "๐ แดssษชsแดแดษดแด ษชแดข sแดษชสส ษชษด สแดแดส แดสแดแด")
        return await user.send_message(chat_id, "๐ แดssษชsแดแดษดแด ษชแดข sแดษชสส ษชษด สแดแดส แดสแดแด")
