import discord
from discord import Client
from discord import guild
from interactions import Intents
from threading import Thread
from functions import pomodoro
import asyncio

HARRY_TOKEN = "insert token here"

bot_intents = discord.Intents.all()
bot = Client(intents=bot_intents)

@bot.event
async def on_ready():
    print("Bot has connected to discord.")

@bot.event
async def on_message(msg) :
    message_sender = msg.author
    if message_sender == bot.user : return
    message_string = msg.content
    if message_string.startswith("$study") :
            user_dm = await message_sender.create_dm()
            asyncio.get_event_loop().create_task(pomodoro(user_dm))
            #pomodoro_thread = Thread(target=between_pomodoro, args=(user_dm,))
            #pomodoro_thread.start() # brings an error up.....
    
bot.run(HARRY_TOKEN)
