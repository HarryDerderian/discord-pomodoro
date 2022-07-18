import discord
from discord import Client
from discord import guild
from interactions import Intents
from threading import Thread
from functions import pomodoro
import asyncio

HARRY_TOKEN = ""

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
            asyncio.get_event_loop().create_task(pomodoro(msg))
    
    elif message_string.startswith("$clear") :
        await msg.channel.purge()
        await msg.channel.send("**Chat cleared.**")

    
bot.run(HARRY_TOKEN)
