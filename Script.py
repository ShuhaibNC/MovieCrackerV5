class script(object):
    START_TXT = """<b>Hello {},

πΈ'πΌ <a href=https://t.me/{}>{}</a>, πΈ π²π°π½ πΏππΎππΈπ³π΄ π»πΎπ'π πΎπ΅ ππ°ππ΄ πΌπΎππΈπ΄π π¬ & ππ΄ππΈπ΄π πΊ , πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ π΄π½πΉπΎπ π

Maintained BY @MovieCrackerLinks β€οΈ</b>"""
    HELP_TXT = """<b>Hey {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π.</b>"""
    ABOUT_TXT = """<b>π€ Κα΄α΄ Ι΄α΄α΄α΄ : <a href=https://t.me/MovieCrackerBot>α΄α΄α΄ Ιͺα΄α΄Κα΄α΄α΄α΄Κ Κα΄α΄</a>

π¨π»βπ» α΄α΄α΄ α΄Κα΄α΄α΄Κ  : <a href=https://t.me/ShuhaibNC>sΚα΄Κα΄ΙͺΚ Ι΄ α΄</a>

π² Κα΄Ι΄Ι’α΄α΄Ι’α΄: <a href="https://www.python.org/">α΄Κα΄Κα΄Ι΄ 3</a>

π α΄α΄α΄α΄Κα΄ : <a href="https://github.com/pyrogram/pyrogram">α΄ΚΚα΄Ι’Κα΄α΄</a>

βοΈ Κα΄sα΄ sα΄Κα΄ α΄Κ : <a href=http://heroku.com/>Κα΄Κα΄α΄α΄</a>

#οΈβ£ α΄ α΄ΚsΙͺα΄Ι΄ : α΄ 3.2.1 [ Κα΄α΄α΄ ]</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- MovieCrackerBot is not a open source project.
<b>DEVS:
- @ππ·ππ·π°πΈπ±π½π²</b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. MovieCrackerBot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- MovieCrackerBot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. MovieCrackerBot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

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
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of MovieCrackerBot

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specifed user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>π α΄α΄α΄α΄Κ κ°ΙͺΚα΄s : {}

π€ α΄α΄α΄α΄Κ α΄sα΄Κs : {}

π₯ α΄α΄α΄α΄Κ α΄Κα΄α΄s : {}

βοΈ α΄sα΄α΄ sα΄α΄Κα΄Ι’α΄ : {}

π κ°Κα΄α΄ sα΄α΄Κα΄Ι’α΄ : {}</b>"""
    LOG_TEXT_G = """#NewGroup
<b>π¨βπ¦βπ¦ Ι’Κα΄α΄α΄ = {}({})
π₯ α΄α΄α΄α΄Κ α΄α΄α΄Κα΄Κκ± = {}
πΆββοΈα΄α΄α΄α΄α΄ ΚΚ - {}
</b>"""
    LOG_TEXT_P = """<b>#NewUser
π₯ Ιͺα΄ - {}
π·οΈ Ι΄α΄α΄α΄ - {}
</b>"""
