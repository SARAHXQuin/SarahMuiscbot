from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from ShizukaXMusic import app
from ShizukaXMusic.core.call import Shizuka
from ShizukaXMusic.utils.database import is_music_playing, music_on
from ShizukaXMusic.utils.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(
    filters.command(RESUME_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"], disable_web_page_preview=True)
    await music_on(chat_id)
    await Shizuka.resume_stream(chat_id)
    photo_url = "https://te.legra.ph/file/c444d70431989b4c6cee4.jpg"  # Replace with the URL of the photo you want to send
    await message.reply_photo(
        photo=photo_url        
    )
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), disable_web_page_preview=True
    )
