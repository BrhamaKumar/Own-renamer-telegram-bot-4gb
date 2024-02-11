import asyncio
import os
from pyrogram import Client, idle
from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6945899533:AAHqvDra4_MtjqwoG1SufiU0PfQFRVj9TOE")
API_ID = int(os.environ.get("API_ID", "20810825"))
API_HASH = os.environ.get("API_HASH", "707e67f53b4593a3e9b6b424311f84d0")
STRING = os.environ.get("STRING", "BQC6kfsABRnt1efMPgUYcq3vlVFZ0R67wNuLydVb5rzeCO94Rr7aaOFg9UIG29a6ezHwWBWAatHm55n9ZVKzL8viVjv7BW8qv3sVQP8A04zCMMveN62BEjyyxsIL0E12sr0BJtnYg-dvB2KzMy3X9eZAJY9ktte8hKsqe3A-g8JzOTLX1VUggo2OQyFMbf2LWEBdoIFvrRrtKawjST5256-amVGnTLlwUtPgHnsGI13yfxlVSzldR0sD3P32mwxvdhQ-CvyfqwNuQ9fSeJjiC5amOVJIzfNNj1APnhX6jSyBg7AO_-sVnOVZN1WdquK-V3zYdb8Otnrdo8XJjoJ4HzpnLEjkxwAAAAF3nDc6AA")

bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           
if STRING:
    # Create instances of the Client2 and Client classes
    client = Client(STRING)
    client2 = Client2(STRING)
    client = Client("Renamer", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))

    # Start both instances
    client2.start()
    client.start()

    # Wait for both instances to finish processing messages
    idle()

    # Stop both instances
    client2.stop()
    client.stop()
else:
    # Start the Client instance
    client = Client("Renamer", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))
    client.run()
    bot.run()
