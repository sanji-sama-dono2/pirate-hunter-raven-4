#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<blockquote><b>○ 𝐎ᴡɴᴇʀ : <a href='https://t.me/DATTEBAYO56'>𝐃ᴀᴛᴛᴇʙᴀʏᴏ</a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Raven'>𝐀ɴɪᴍᴇ 𝐑ᴀᴠᴇɴ</a>\n○ 𝐎ɴɢᴏɪɴɢ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Ongoing_Anime_Raven'>𝐎ɴɢᴏɪɴɢ 𝐑ᴀᴠᴇɴ</a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀᴛ : <a href='https://t.me/Anime_Chat_Raven'>𝐀ɴɪᴍᴇ 𝐂ʜᴀᴛ 𝐑ᴀᴠᴇɴ</a></b></blockquote>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('ᴏᴡɴᴇʀ', url='https://t.me/DATTEBAYO56')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
