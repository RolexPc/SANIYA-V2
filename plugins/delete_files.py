import re
import os
from os import environ
import logging
import os, pytz, re, datetime, logging, asyncio, math, time
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, ChatAdminRequired, UsernameInvalid, UsernameNotModified
from database.ia_filterdb import Media2, Media3, Media4, Media5, unpack_new_file_id, get_readable_time
from info import id_pattern, ADMINS
logger = logging.getLogger(__name__)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp
lock = asyncio.Lock()

media_filter = filters.document | filters.video | filters.audio
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001990481849').split()]


@Client.on_message(filters.chat(DELETE_CHANNELS) & media_filter)
async def deletemultiplemedia(bot, message):
    """Delete Multiple files from the database"""
    for file_type in ("document", "video", "audio"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return

    file_id, file_ref = unpack_new_file_id(media.file_id)

    result_media1 = await Media2.collection.find_one({'_id': file_id})
    result_media2 = await Media3.collection.find_one({'_id': file_id})
    result_media3 = await Media4.collection.find_one({'_id': file_id})
    result_media4 = await Media5.collection.find_one({'_id': file_id})
    
    if result_media1:
        await Media2.collection.delete_one({'_id': file_id})
    elif result_media2:
        await Media3.collection.delete_one({'_id': file_id})
    elif result_media3:
        await Media4.collection.delete_one({'_id': file_id})
    elif result_media4:
        await Media5.collection.delete_one({'_id': file_id})
    else:
        logger.info('File not found in the database.')

@Client.on_message(filters.command("del_channel") & filters.user(ADMINS))
async def deletechannelmedia(bot, message):
    if message.reply_to_message:
        if message.reply_to_message.text:
            regex = re.compile("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")
            match = regex.match(message.text)
            if not match:
                return await message.reply('Invalid link')
            chat = match.group(4)
            lst_msg_id = int(match.group(5))
            if chat.isnumeric():
                chat  = int(("-100" + chat_id))
        elif message.reply_to_message.forward_from_chat.type == enums.ChatType.CHANNEL:
            lst_msg_id = message.reply_to_message.forward_from_message_id
            chat = message.reply_to_message.forward_from_chat.username or message.reply_to_message.forward_from_chat.id
        else:
            return 
        msg = await message.reply("processing...")
        total_files = 0
        not_fount = 0
        no_media = 0
        fst_msg_id = temp.CURRENT
        start_time = time.time()
        remaining_time_str = "N/A"
        async with lock:
            try:
                current = temp.CURRENT
                tz = pytz.timezone('Asia/Kolkata')
                today = datetime.date.today()
                now = datetime.datetime.now(tz)
                ttime = now.strftime("%I:%M:%S %p - %d %b, %Y")
                temp.CANCEL = False
                elapsed_time = 0
                remaining_index = 0
                async for message in bot.iter_messages(chat, lst_msg_id, temp.CURRENT):
                    if temp.CANCEL:
                        await msg.edit(f"<b>❌ Successfully Cancelled!!</b>\n\n<b>├ ▸ Last Updated: <i>{ttime}</i></b>\n\n<b>╭ ▸ Fetched:</b> <code>{current}</code>\n<b>├ ▸ Deleted:</b> <code>{total_files}</code>\n<b>├ ▸ Not found:</b> <code>{not_fount}</code>\n<b>╰ ▸ Non:</b> <code>{no_media}</code>\n")
                        break
                    current += 1
                    tz = pytz.timezone('Asia/Kolkata')
                    today = datetime.date.today()
                    now = datetime.datetime.now(tz)
                    ttime = now.strftime("%I:%M:%S %p - %d %b, %Y")              
                    if current % 1000 == 0:
                        can = [[InlineKeyboardButton('Cancel', callback_data='index_cancel')]]
                        reply = InlineKeyboardMarkup(can)                        
                        elapsed_time = time.time() - start_time
                        remaining_time = (lst_msg_id - current - 1) * elapsed_time / (current - fst_msg_id + 1)
                        remaining_time_str = get_readable_time(remaining_time)
                        elapsed_time_str = get_readable_time(elapsed_time)
                        remaining_index = lst_msg_id - current                       
                        await msg.edit_text(
                            text=f"<b>╭ ▸ ETC: </b>{remaining_time_str} ❙ Remaining:</b> <code>{remaining_index}</code>\n<b>├ ▸ Last Updated: <i>{ttime}</i></b>\n<b>╰ ▸ Time Taken: </b>{elapsed_time_str} <b>\n\n<b>╭ ▸ Fetched:</b> <code>{current}</code>\n<b>├ ▸ Deleted:</b> <code>{total_files}</code>\n<b>├ ▸ Not found:</b> <code>{not_fount}</code>\n<b>╰ ▸ Non:</b> <code>{no_media}</code>\n",
                            reply_markup=reply)
                    if message.empty:
                        no_media += 1
                        continue
                    elif not message.media:
                        no_media += 1
                        continue
                    elif message.media not in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.DOCUMENT]:
                        no_media += 1
                        continue
                    media = getattr(message, message.media.value, None)
                    if not media:
                        no_media += 1
                        continue
                    if media.mime_type not in ['video/mp4', 'video/x-matroska']:
                        no_media += 1
                        continue
                    file_id, file_ref = unpack_new_file_id(media.file_id)

                    result_media1 = await Media2.collection.find_one({'_id': file_id})
                    result_media2 = await Media3.collection.find_one({'_id': file_id})
                    result_media3 = await Media4.collection.find_one({'_id': file_id})
                    result_media4 = await Media5.collection.find_one({'_id': file_id})
    
                    if result_media1:
                        await Media2.collection.delete_one({'_id': file_id})
                    elif result_media2:
                        await Media3.collection.delete_one({'_id': file_id})
                    elif result_media3:
                        await Media4.collection.delete_one({'_id': file_id})
                    elif result_media4:
                        await Media5.collection.delete_one({'_id': file_id})
                    else:
                        not_fount += 1
                        continue
            except Exception as e:
                logger.exception(e)
                return await bot.send_message(msg.chat.id, f'<b>🚫 Error:</b> {e}\n\n<b>╭ ▸ ETC: </b>{remaining_time_str} ❙ Remaining:</b> <code>{remaining_index}</code>\n<b>├ ▸ Last Updated: <i>{ttime}</i></b>\n<b>\n\n<b>╭ ▸ Fetched:</b> <code>{current}</code>\n<b>├ ▸ Deleted:</b> <code>{total_files}</code>\n<b>├ ▸ Not found:</b> <code>{not_fount}</code>\n<b>╰ ▸ Non:</b> <code>{no_media}</code>\n')
            else:
                await bot.send_message(msg.chat.id, f'<b>✅ Successfully Completed!!</b>\n\n<b>╭ ▸ ETC: </b>{remaining_time_str} ❙ Remaining:</b> <code>{remaining_index}</code>\n<b>├ ▸ Last Updated: <i>{ttime}</i></b>\n<b>╰ ▸ Time Taken: </b>{elapsed_time_str} <b>\n\n<b>╭ ▸ Fetched:</b> <code>{current}</code>\n<b>├ ▸ Deleted:</b> <code>{total_files}</code>\n<b>├ ▸ Not found:</b> <code>{not_fount}</code>\n<b>╰ ▸ Non:</b> <code>{no_media}</code>\n')
            
    else:
        return
        
    
