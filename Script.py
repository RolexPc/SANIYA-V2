class script(object):
    START_TXT = """
<b>
𝐻𝑒𝑙𝑙𝑜 👋 {}</b>


<b>I'ᴍ <a href=https://t.me/{}>{}</a> Yᴏᴜ Cᴀɴ Cᴀʟʟ Mᴇ Aꜱ Aᴜᴛᴏ Fɪʟᴛᴇʀ Bᴏᴛ V2 🫶</b>

<b>Exᴄʟᴜꜱɪᴠᴇʟʏ Mᴀᴅᴇ Tʜɪꜱ Bᴏᴛ Fᴏʀ @ARAKAL_THERAVAD_GROUP_01..!! 💫</b>

<b>📌 Sᴜᴘᴘᴏʀᴛ : @OTT_ARAKAL_THERAVAD_MOVIESS</b>

<b>🍂 Oᴡɴᴇʀ : @ARAKAL_THERAVAD_MOVIES_02_bot</b>"""
    OWNER_TXT = """<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟</b>
    
<b>• ꜰᴜʟʟ ɴᴀᴍᴇ : ARAKAL THERAVAD MOVIES</b>
<b>• Uꜱᴇʀ ɴᴀᴍᴇ : @ARAKAL_THERAVAD_MOVIES_02_bot
• Usᴇʀ ɪᴅ :</b> <code>1297128957</code>
    
<b>∂σи'т вє αfяαι∂ σf вєιиg ∂ιffєяєит, вє αfяαι∂ σf вєιиg тнє ѕαмє αѕ єνєяуσиє єℓѕє</b>
    """

    ABOUT_TXT = """<b>🤖 𝑴𝒚 𝑵𝒂𝒎𝒆 : {}
    
📝 𝑳𝒂𝒏𝒈𝒖𝒂𝒈𝒆 : <a href='https://www.python.org/download/releases/3.0/'>𝑷𝒚𝒕𝒉𝒐𝒏</a>

📚 𝑭𝒓𝒂𝒎𝒆𝒘𝒐𝒓𝒌 : <a href='https://docs.pyrogram.org/'>𝑷𝒚𝒓𝒐𝒈𝒓𝒂𝒎</a>

📡 𝑯𝒐𝒔𝒕𝒆𝒅 𝑶𝒏 : 𝑯𝑬𝑹𝑲𝑼𝑶

👨‍💻 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 : <a href='https://t.me/ARAKAL_THERAVAD_MOVIES_02_bot'>𝑵𝒂𝒛𝒓𝒊𝒚𝒂</a>

👥 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑 : <a href='https://t.me/+FAa3tYIjXYcyZDY1'>𝑨𝑻𝑴</a>

📢 𝑼𝒑𝒅𝒂𝒕𝒆 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 : <a href='https://t.me/OTT_ARAKAL_THERAVAD_MOVIESS'>𝑨𝑻𝑴 𝑶𝒇𝒇𝒊𝒄𝒊𝒂𝒍</a></b>"""
    
    HELP_TXT = """<b>Hᴇʏ {} Fʀɪᴇɴᴅ Hᴇʀᴇ Yᴏᴜʀ Bᴜᴛᴛᴏɴs 👇</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
<b>- 𝙴𝙻𝚂𝙰 𝙸𝚂 𝙾𝙿𝙴𝙽 𝚂𝙾𝚄𝚁𝙲𝙴 𝙿𝚁𝙾𝙹𝙴𝙲𝚃. 
- 𝚂𝙾𝚄𝚁𝙲𝙴 - 𝙲𝙻𝙸𝙲𝙺 𝚁𝙴𝙿𝙾 𝙱𝚄𝚃𝚃𝙾𝙽</b>
<b>DEVS:</b>
- <a href=https://t.me/ARAKAL_THERAVAD_MOVIES>ARAKAL_THERAVAD_MOVIES.𝙲𝙾𝙼</a>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

<b>- 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚆𝙴𝚁𝙴 𝚄𝚂𝙴𝚁𝚂 𝙲𝙰𝙽 𝚂𝙴𝚃 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙴𝙳 𝚁𝙴𝙿𝙻𝙸𝙴𝚂 𝙵𝙾𝚁 𝙰 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻𝙰𝚁 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙰𝙽𝙳 𝙴𝙻𝚂𝙰 𝚆𝙸𝙻𝙻 𝚁𝙴𝚂𝙿𝙾𝙽𝙳 𝚆𝙷𝙴𝙽𝙴𝚅𝙴𝚁 𝙰 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙸𝚂 𝙵𝙾𝚄𝙽𝙳 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴</b>

<b>NOTE:</b>
<b> 𝙴𝙻𝚂𝙰 𝚂𝙷𝙾𝚄𝙻𝙳 𝙷𝙰𝚅𝙴 𝙰𝙳𝙼𝙸𝙽 𝙿𝚁𝙸𝚅𝙸𝙻𝙻𝙰𝙶𝙴.
 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃.
 𝙰𝙻𝙴𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝙷𝙰𝚅𝙴 𝙰 𝙻𝙸𝙼𝙸𝚃 𝙾𝙵  𝙲𝙷𝙰𝚁𝙰𝙲𝚃𝙴𝚁𝚂.</b>

<b>Commands and Usage:</b>
 /filter - <code>add a filter in chat</code>
 /filters - <code>list all the filters of a chat</code>
 /del - <code>delete a specific filter in chat</code>
 /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

<b>𝙴𝙻𝚂𝙰 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝙾𝚃𝙷 𝚄𝚁𝙻 𝙰𝙽𝙳 𝙰𝙻𝙴𝚁𝚃 𝙸𝙽𝙻𝙸𝙽𝙴 𝙱𝚄𝚃𝚃𝙾𝙽𝚂.</b>
<b>NOTE:</b>
<b> 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙰𝙻𝙻𝙾𝚆𝚂 𝚈𝙾𝚄 𝚃𝙾 𝚂𝙴𝙽𝙳 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙰𝙽𝚈 𝙲𝙾𝙽𝚃𝙴𝙽𝚃, 𝚂𝙾 𝙲𝙾𝙽𝚃𝙴𝙽𝚃 𝙸𝚂 𝙼𝙰𝙽𝙳𝙰𝚃𝙾𝚁𝚈.
 𝙴𝙻𝚂𝙰 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷 𝙰𝙽𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙼𝙴𝙳𝙸𝙰 𝚃𝚈𝙿𝙴.
 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚂𝙷𝙾𝚄𝙻𝙳 𝙱𝙴 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈 𝙿𝙰𝚁𝚂𝙴𝙳 𝙰𝚂 𝙼𝙰𝚁𝙺𝙳𝙾𝚆𝙽 𝙵𝙾𝚁𝙼𝙰𝚃</b>
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Example...)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """<b>
 Bro Or Sis, ഈ ഒരു ബോട്ട് @ARAKAL_THERAVAD_GROUP_02 ൻ്റെ Aᴜᴛᴏ Fɪʟᴛᴇʀ Bᴏᴛ ᴠ2 ആണ്, ബോട്ട് Owner ഡെ പർമ്മിഷൻ ഇല്ലാതെ മറ്റു ഗ്രൂപ്പുകളിൽ ഒന്നും ഈ ബോട്ടിനെ യൂസ് ചെയ്യാൻ കഴിയില്ല..!!  🤗⚠

️📌 𝗔𝗻𝘆 𝗛𝗲𝗹𝗽 𝗣𝗹𝗲𝗮𝘀𝗲 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗔𝗱𝗺𝗶𝗻 : @ARAKAL_THERAVAD_MOVIES_02_bot</b>"""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
 Only admins can add a connection.
 Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
 /connect  - <code>connect a particular chat to your PM</code>
 /disconnect  - <code>disconnect from a chat</code>
 /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Elsa

<b>Commands and Usage:</b>
 /id - <code>get id of a specified user.</code>
 /info  - <code>get information about a user.</code>
 /imdb  - <code>get the film information from IMDb source.</code>
 /search  - <code>get the film information from various sources.</code>"""

    SONG_TXT = """<b>𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴</b>

<i>𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴, 𝙵𝙾𝚁 𝚃𝙷𝙾𝚂𝙴 𝚆𝙷𝙾 𝙻𝙾𝚅𝙴 𝙼𝚄𝚂𝙸𝙲. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙵𝙴𝙰𝚃𝚄𝙴 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚂𝙾𝙽𝙶 𝚆𝙸𝚃𝙷 𝚂𝚄𝙿𝙴𝚁 𝙵𝙰𝚂𝚃 𝚂𝙿𝙴𝙴𝙳.𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙾𝙽 𝙶𝚁𝙾𝚄𝙿𝚂../</i>

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂</b>

 /song 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 

<b>𝚆𝙾𝚁𝙺𝚂 𝙱𝙾𝚃𝙷 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙿𝙼</b>
@ARAKAL_THERAVAD_MOVIES"""

    VIDEO_TXT ="""𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.
 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦
𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/example...)
 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/mp4 https://youtu.be/example...</code>
<code>/video https://youtu.be/example...</code>"""

    TTS_TXT = """Help: <b> TTS  module:</b>
Translate text to speech
<b>Commands and Usage:</b>
 /tts <text> : convert text to speech"""

    GTRANS_TXT = """ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋
𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚊 𝚝𝚎𝚡𝚝 𝚝𝚘 𝖺𝗇𝗒 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝. 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙 
 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾
 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾
𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    TELE_TXT = """<b>HELP: Telegraph </b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
<b>NOTE:</b>
 This Command Is Available in goups and pms
 This Command Can be used by everyone"""

    CORONA_TXT = """ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽
𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 
 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
 /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇
𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>

 This service has been stopped"""

    ABOOK_TXT = """ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 
 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
 /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    DEPLOY_TXT= """𝙸𝙵 𝚈𝙾𝚄 𝙵𝙰𝙲𝙸𝙽𝙶 𝙰𝙽𝚈 𝙸𝚂𝚂𝚄𝙴 𝙸𝙽 𝚃𝙷𝙴 𝚁𝙴𝙿𝙾 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝙴..."""
   
    PINGS_TXT = """<b>Ping Testing:</b>
Helps you to know your ping 
<b>Commands:</b>
 /alive - To check you are alive.
 /help - To get help.

 /ping - <b>To get your ping.</b>

<b> Usage :</b>
 This commands can be used in pm and groups
 This commands can be used buy everyone in the groups and bots pm
 Share us for more features"""
 
    STICKER_TXT = """<b>𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.</b>
 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
   𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
 Reply To Any Sticker [/stickerid]"""

    FONT_TXT= """ 𝐔𝐒𝐀𝐆𝐄

𝐘𝐎𝐔 𝐂𝐀𝐍 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐌𝐎𝐃𝐔𝐋𝐄 𝐓𝐎 𝐂𝐇𝐀𝐍𝐆𝐄 𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄 

<b>COMMAND</b> : /font your text (optional)
        <b> Eg:- /font Hello</b>

 <i>This feature added by @ARAKAL_THERAVAD_MOVIES"""
    JSON_TXT = """<b>JSON:</b>
Bot returns json for all replied messages with /json or /js
<b>Features:</b>
Message Editting JSON
Pm Support
Group Support
<b>Note:</b>
<b>Everyone can use this command , if spaming happens bot will automatically ban you from the group.</b>"""

    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- <b>Give a user details</b>

/whois :-give a user full details 📑"""

    URLSHORT_TXT = """ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋
<i><b>𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 </i></b>
 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
 /short: <b>𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌</b>
𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/example...</code>"""

    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>⚡ 𝙹𝚄𝚂𝚃 𝚂𝙾𝙼𝙴 𝙺𝙸𝙽𝙳 𝙾𝙵 𝙵𝚄𝙽 𝚃𝙷𝙸𝙽𝙶'𝚂 ⚡</b>
 
 /dice - 𝚁𝙾𝙻𝙴 𝚃𝙷𝙴 𝙳𝙸𝙲𝙴 
 /Throw 𝗈𝗋 /Dart - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙳𝙰𝚁𝚃 
 /Runs - 𝚂𝙾𝙼𝙴 𝚁𝙰𝙽𝙳𝙾𝙼 𝙳𝙸𝙰𝙻𝙾𝙶𝚄𝙴𝚂 
 /Goal or /Shoot - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙰 𝙶𝙾𝙰𝙻 𝙾𝚁 𝚂𝙷𝙾𝙾𝚃
 /luck or /cownd - 𝚂𝙿𝙸𝙽 𝙰𝙽𝙳 𝚃𝚁𝚈 𝚈𝙾𝚄𝚁 𝙻𝚄𝙲𝙺"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
 /logs - <code>to get the rescent errors</code>
 /stats - <code>to get status of files in db.</code>
 /delete - <code>to delete a specific file from db.</code>
 /users - <code>to get list of my users and ids.</code>
 /chats - <code>to get list of the my chats and ids </code>
 /leave  - <code>to leave from a chat.</code>
 /disable  -  <code>do disable a chat.</code>
 /ban  - <code>to ban a user.</code>
 /unban  - <code>to unban a user.</code>
 /channel - <code>to get list of total connected channels</code>
 /broadcast - <code>to broadcast a message to all users</code>
 /grp_broadcast - <code>to broadcast a message to all groups</code>
 /gfilter - <code>To add global filter</code>
 /gfilters - <code>To view global filters</code>
 /delallg - <code>To delete all global filters from database</code>
 /delg - <code>To delete a specific global filter</code>
 /setskip - <code>Skip no of files before indexing</code>
 /send - <code>Send any message through bot to users. /send (username/userid) reply with message </code>
 /deletefiles - <code>Delete CamRip and PreDvD files delete from database </code>"""
    
    STATUS_TXT = """📂 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌     - <code>{}</code>

𒆜  𝗗𝗕 1️⃣
╭ ▸ 𝖴𝗌𝖾𝗋𝗌 : <code>{}</code>
├ ▸ 𝖢𝗁𝖺𝗍𝗌  : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

 𒆜 𝗗𝗕 2️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

 𒆜 𝗗𝗕 3️⃣ 
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

𒆜  𝗗𝗕 4️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB

𒆜 𝗗𝗕 5️⃣
╭ ▸ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
╰ ▸ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>MB"""

    CARB_TXT = """<b>Help</b> : 𝗖𝗔𝗥𝗕𝗢𝗡
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""


    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
Elsa
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
Elsa
"""
    FILE_MSG = """
<b>Hai 👋 {} </b>😍

<b>📫 Your File is Ready</b>

<b>📂 Fɪʟᴇ Nᴀᴍᴇ</b> : <b><code><b>{}</b></code></b>              
                       
<b>⚙️ Fɪʟᴇ Sɪᴢᴇ</b> : <b>{}</b>
"""
    CHANNEL_CAP = """
<b>Hai 👋 {}</b> 😍

<b><code>{}</code></b>

⚠️ <b>ഇവിടെ നിന്നും വേറെ എവിടേലും മാറ്റിയതിന് ശേഷം ഡൗൺലോഡ് ചെയ്യുക... !!!</b>

<b>കോപ്പി റൈറ്റ് ഉള്ളത് കൊണ്ട് ഈ ഒരു ഫയൽ 𝟓 മിനിറ്റ് കൊണ്ട് ഇവിടെ നിന്നും ഡിലേറ്റാവും...!!!</b>

<b>╔═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╗
♻️ 𝑱𝑶𝑰𝑵 :- <a href=https://t.me/+SAkK3icaGIJhMmY9> 𝐆𝐑𝐎𝐔𝐏 </a>
♻️ 𝑱𝑶𝑰𝑵 :- <a href=https://t.me/OTT_ARAKAL_THERAVAD_MOVIESS> 𝐎𝐓𝐓 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 </a>
♻️ 𝑱𝑶𝑰𝑵 :- <a href=https://t.me/ARAKAL_THERAVAD_GROUP_LINKS> 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 </a>
╚═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╝</b>
"""
    SUR_TXT = """
<b>
𝐻𝑒𝑙𝑙𝑜 👋 {}</b>

<b>I'ᴍ <a href=https://t.me/{}>{}</a>Yᴏᴜ Cᴀɴ Cᴀʟʟ Mᴇ Aꜱ Aᴜᴛᴏ Fɪʟᴛᴇʀ Bᴏᴛ ᴠ2 🫶</b>

<b>Exᴄʟᴜꜱɪᴠᴇʟʏ Mᴀᴅᴇ Tʜɪꜱ Bᴏᴛ Fᴏʀ @ARAKAL_THERAVAD_GROUP_01..!! 💫</b>

<b>📌 Sᴜᴘᴘᴏʀᴛ : @OTT_ARAKAL_THERAVAD_MOVIESS</b>

<b>🍂 Oᴡɴᴇʀ : @ARAKAL_THERAVAD_MOVIES_02_bot</b>"""

    IMDB_TEMPLATE_TXT = """
<b>🔖 ᴛɪᴛʟᴇ :<a href={url}>{title}</a>

🎭 ɢᴇɴʀᴇs : {genres}
🎖 ʀᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10 (ʙᴀsᴇᴅ ᴏɴ {votes} ᴜsᴇʀ ʀᴀᴛɪɴɢ.)

📆 ʏᴇᴀʀ : {release_date}
🗞 ʟᴀɴɢᴜᴀɢᴇ : {languages}
🌎 ᴄᴏᴜɴᴛʀʏ : {countries}

©{message.chat.title}</b>
"""

    CUSTOM_FILE_CAPTION = """
 <b>📂Fɪʟᴇɴᴀᴍᴇ : {file_name}</b>


<b>⚙️ Fɪʟᴇ Sɪᴢᴇ</b> : <b>{file_size}</b>

<b>╔═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╗
♻️ 𝑱𝑶𝑰𝑵 :- <a href=https://t.me/+tDgIRWerxDNhMWE1> 𝐆𝐑𝐎𝐔𝐏 </a>
♻️ 𝑱𝑶𝑰𝑵 :- <a href=https://t.me/OTT_ARAKAL_THERAVAD_MOVIESS> 𝐎𝐓𝐓 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 </a>
♻️ 𝑱𝑶𝑰𝑵 :- <a href=https://t.me/ARAKAL_THERAVAD_GROUP_LINKS> 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 </a>
╚═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╝</b>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !
📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️"""

    ALRT_TXT = """ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏʏ ꜱɪʀ"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧 """

    TOP_ALRT_MSG = """♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""

    MVE_NT_FND = """<b>➠➠ ⚠️ നിങ്ങൾ ചോദിച്ച മൂവി OTT യിൽ റിലീസ് ആയിട്ടില്ല..!!⚡</b>


<b>➠➠ 📌 OTT യിൽ മൂവി റിലീസ് അയാൽ മാത്രമെ ടെലഗ്രാമിൽ വരൂ..!!💥

╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
Cʜᴇᴄᴋ 👉 <a href=https://t.me/OTT_ARAKAL_THERAVAD_MOVIESS> 𝐎𝐓𝐓 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 </a> Kɴᴏᴡ Tʜᴇ Oᴛᴛ Uᴘᴅᴀᴛᴇꜱ..!!
╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝

 ‼ 𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ @ARAKAL_THERAVAD_MOVIES_02_bot</b> """

    NORSLTS = """ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    I_CUDNT = """<b>➠➠ ⚠️ നിങ്ങൾ ചോദിച്ച മൂവി OTT യിൽ റിലീസ് ആയിട്ടില്ല..!!⚡</b>


<b>➠➠ 📌 OTT യിൽ മൂവി റിലീസ് അയാൽ മാത്രമെ ടെലഗ്രാമിൽ വരൂ..!!💥

╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
Cʜᴇᴄᴋ 👉 <a href=https://t.me/OTT_ARAKAL_THERAVAD_MOVIESS> 𝐎𝐓𝐓 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 </a> Kɴᴏᴡ Tʜᴇ Oᴛᴛ Uᴘᴅᴀᴛᴇꜱ..!!
╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝

 ‼ 𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ @ARAKAL_THERAVAD_MOVIES_02_bot</b> """

    I_CUD_NT = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴘᴇʟʟɪɴɢ."""
    
    CUDNT_FND = """<b><i>
𝖨 𝖼𝗈𝗎𝗅𝖽𝗇'𝗍 𝖿𝗂𝗇𝖽 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝗍𝗈 𝗍𝗁𝖺𝗍
𝖣𝗂𝖽 𝗒𝗈𝗎 𝗆𝖾𝖺𝗇 𝖺𝗇𝗒 𝗈𝗇𝖾 𝗈𝖿 𝗍𝗁𝖾𝗌𝖾?</i></b>"""

    REPRT_MSG = """ Reported To Admin"""

    CON_TXT = """<b><u>ᴄᴏᴜɴᴛʀʏ ɪɴғᴏ</b></u>
<b>Tʜɪs ᴍᴏᴅᴜʟᴇ ɪs ᴛᴏ ғɪɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴄᴏᴜɴᴛʀɪᴇs</b>
 /country [𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾] 
𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :- <code>/country India</code>"""
