class script(object):
    START_TXT = """Hey there! I'm your advanced auto filter bot 🤖\nFast and efficient at your service! ⚡️\nLet's keep this chat clean and enjoyable 🚀\nFeel free to ask for help anytime! 🙌"""
    HELP_TXT = """<b>𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌</b>:\n /start - 𝖼𝗁𝖾𝖼𝗄 𝗐𝗁𝖾𝗍𝗁𝖾𝗋 𝗂𝗆 𝗈𝗇𝗅𝗂𝗇𝖾 \n/help - 𝗀𝖾𝗍 𝗍𝗁𝗂𝗌 𝗁𝖾𝗅𝗉 𝗆𝖾𝗌𝗌𝖺𝗀𝖾\n/about - 𝖺𝖻𝗈𝗎𝗍 𝗆𝖾"""
    ABOUT_TXT = """
╔══════════════════❍
║╭━━━━━━━━━━━━━━━➣ 
║➠ 𝙼𝚈 𝙽𝙰𝙼𝙴 -  Tiger Shroff
║➠ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 - :<a href='tg://user?id=1951205538'><b>༒ᶜʳᵃᶻʸᴮᴼˢˢ卂乃卄丨丂卄乇Ҝ༒</b></a>
║➠ 𝙲𝚁𝙴𝙳𝙸𝚃𝚂 - <a href='https://t.me/Abhisheksvlog'>Everyone in this journey </a>
║➠ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 - <a href='https://docs.pyrogram.org/'>𝑷𝒚𝒕𝒉𝒐𝒏 3 </a>
║➠ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 - <a href='https://docs.pyrogram.org/'>𝑷ʏʀᴏɢʀᴀᴍ </a>
║➠ 𝙲𝙻𝙾𝙽𝙴𝙳 𝙵𝚁𝙾𝙼 - EvaMaria
║➠ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴 -  <a href='https://dashboard.heroku.com/apps'>𝑯𝒆𝒓𝒐𝒌𝒖</a>
║➠ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂 - <a href='https://t.me/TigerShroffimdbot'>𝒗8.7.2[𝑴𝒂𝒋𝒐𝒓]</a>
║➠ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴 - <a href='https://github.com/200920082007/TigerShroff'>𝑪𝒍𝒊𝒄𝒌 𝑯𝒆𝒓𝒆</a>
║╰━━━━━━━━━━━━━━━➣ ╚══════════════════❍
    
🔖 𝑸𝒖𝒐𝒕𝒆 : ആരും പേടിക്കേണ്ട എല്ലാവർക്കും കിട്ടും ™️""" 

    SOURCE_TXT = """ • <h1><u>Thanks To</u></h1>\n • Thanks To Dan For His Awesome [Library](https://github.com/pyrogram/pyrogram)\n • Thanks To Mahesh For His Awesome [Media-Search-bot](https://github.com/Mahesh0253/Media-Search-bot)\n • Thanks To [Trojanz](https://github.com/trojanzhex) for Their Awesome [Unlimited Filter Bot](https://github.com/TroJanzHEX/Unlimited-Filter-Bot) And [AutoFilterBoT](https://github.com/trojanzhex/auto-filter-bot)\n • Thanks To All Everyone In This Journey\n• Thanks To [EvamariaTG](https://raw.githubusercontent.com/EvamariaTG) for their awesome [EvaMaria Bot](https://raw.githubusercontent.com/EvamariaTG/EvaMaria)\n • Thanks To Me 😂\n• <h1><u>Main Editors</u></h1>\n
 • <a href='tg://user?id=1951205538'>༒ᶜʳᵃᶻʸᴮᴼˢˢ卂乃卄丨丂卄乇Ҝ༒</a>
 • <a href='tg://user?id=1177577143'>Jᴏᴇʟ ᠰ TɢX</a> """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/mflinkzbot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of this bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """➥ <b>ᴛᴏᴛᴀʟ ғɪʟᴇs</b>: <i>{}</i>
➥ <b>ᴛᴏᴛᴀʟ ᴜsᴇʀs</b>: <i>{}</i>
➥ <b>ᴛᴏᴛᴀʟ ᴄʜᴀᴛs</b>: <i>{}</i>
➥ <b>ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ</b>: <i>{}</i> 
➥ <b>ғʀᴇᴇ sᴛᴏʀᴀɢᴇ</b>: <i>{}</i> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
