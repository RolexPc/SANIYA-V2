from pyrogram import Client, filters
from info import CHANNELS
from database.ia_filterdb import save_file2, save_file3, save_file4, save_file5, check_file

media_filter = filters.document | filters.video | filters.audio


@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    """Media Handler"""
    for file_type in ("document", "video", "audio"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return

    media.file_type = file_type
    media.caption = message.caption
    
    if message.id % 4 == 0:
        tru = await check_file(media)
        if tru == "okda":
            await save_file2(media)
        else:
            print("skipped duplicate file from saving to db 😌")
    elif message.id % 4 == 1:
        tru = await check_file(media)
        if tru == "okda":
            await save_file3(media)
        else:
            print("skipped duplicate file from saving to db 😌")
    elif message.id % 4 == 2:
        tru = await check_file(media)
        if tru == "okda":
            await save_file4(media)
        else:
            print("skipped duplicate file from saving to db 😌")
    else:
        tru = await check_file(media)
        if tru == "okda":
            await save_file5(media)
        else:
            print("skipped duplicate file from saving to db 😌")
