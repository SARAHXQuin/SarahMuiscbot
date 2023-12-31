from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from ShizukaXMusic import app

from ShizukaXMusic.core.call import Shizuka
from ShizukaXMusic.utils.database import set_loop
from ShizukaXMusic.utils.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Shizuka.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    photo_url = "https://te.legra.ph/file/5f3347d579c92e984521f.jpg"  # Replace with the URL of the photo you want to send    
    await message.reply_photo(
        photo=photo_url          
    )
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention), disable_web_page_preview=True
    )
