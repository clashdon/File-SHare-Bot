#(©)Codexbotz
#(©)Cold_Onez

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Mᴀsᴛᴇʀ : <a href='https://t.me/mdiskmovies30'>𝕄𝕒𝕚𝕟 ℂ𝕙𝕒𝕟𝕟𝕖𝕝</a>\n○ Lᴀɴɢᴜᴀɢᴇ : <code>Python3</code>\n○ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ 𝕄𝕒𝕚𝕟 ℂ𝕙𝕒𝕟𝕟𝕖𝕝: <a href='https://t.me/mdiskmovies30'>Click Here</a>\n○ Cʜᴀɴɴᴇʟ : @likemoviesearch\n○ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ : @Berlinsupportg</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data = "close")
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
