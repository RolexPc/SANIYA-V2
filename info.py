import re
import os
from os import environ
from pyrogram import enums
from Script import script 

import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '12618934'))
API_HASH = environ.get('API_HASH','49aacd0bc2f8924add29fb02e20c8a16')
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 600))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/1df94bbed99322cd41513.jpg https://telegra.ph/file/6cd75457784400d52ad01.jpg https://telegra.ph/file/6c50207808433731c39cc.jpg https://telegra.ph/file/f7140e078173bcf53757d.jpg https://telegra.ph/file/7a4e3151891b692f1636c.jpg https://telegra.ph/file/968e3f0f87e54d2de9083.jpg https://telegra.ph/file/76b765710d741a1e8fe35.jpg https://telegra.ph/file/0e71cb9c319c54186b40c.jpg https://telegra.ph/file/09d149147266d91ac5d8b.jpg https://telegra.ph/file/663734ea30797994835a1.jpg')).split()
NOR_IMG = environ.get('NOR_IMG', "https://telegra.ph/file/4a3ebfeb49bcd916851fb.jpg")
SPELL_IMG = environ.get('SPELL_IMG',"https://telegra.ph/file/0a777cb06df4f0336861b.jpg")

# Welcome area
MELCOW_IMG = environ.get('MELCOW_IMG',"https://telegra.ph/file/e54cae941b9b81f13eb71.jpg")
MELCOW_VID = environ.get('MELCOW_VID',"")



# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1297128957 1389381953').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001911016310').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://pcmovies:pcmovies@cluster0.4vv9ebl.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "pcmovies")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
MONGO_URL = os.environ.get('MONGO_URL', "")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

#url links
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shorturllink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '3a3935e37c74a2384f7a689c414f078ab6320785')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))

#Auto approve 
#In private group or channel must enable request admin approval 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '0').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour request has been approved")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
PORT = os.environ.get("PORT", "8080")
MAX_BTN = int(environ.get('MAX_BTN', "10"))
S_GROUP = environ.get('S_GROUP',"https://t.me/ARAKAL_THERAVAD_MOVIES")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/OTT_ARAKAL_THERAVAD_MOVIESS")
FILE_FORWARD = environ.get('FILE_FORWARD',"https://t.me/FILES_STORE_01")
MSG_ALRT = environ.get('MSG_ALRT', '𝑪𝑯𝑬𝑪𝑲 & 𝑻𝑹𝒀 𝑨𝑳𝑳 𝑴𝒀 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', '-1001765119767'))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002010307613'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Elsasupportgp')
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "False")), False)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

LANGUAGES = ["malayalam", "mal", "tamil", "tam", "english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
