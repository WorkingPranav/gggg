from Bot import OWNER_ID, encoder, create_ubot
from pyrogram.types import InlineKeyboardMarkup as IKM, InlineKeyboardButton as IKB
import asyncio
from aiohttp import web
from plugins import web_server

encoder.start()

app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

success = create_ubot()
if success != None:
    ubot = success
    ubot.start()

try:
    encoder.send_message(OWNER_ID, text='Bot Started', reply_markup=IKM([[IKB('ʜᴇʟᴘ', 'answer_help'), IKB('ᴅᴇᴠᴇʟᴏᴘᴇʀ', 'answer_about_dev')]]))
except:
    pass    

loop = asyncio.get_event_loop()
loop.run_forever()
