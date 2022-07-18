import discord
from discord import Client, guild
from interactions import Intents
from threading import Thread
from functions import pomodoro
import asyncio

TOKEN = ""
tasks = {}
POMODORO_INFO = "The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. \
It uses a kitchen timer to break work into intervals, typically 25 minutes in length, separated by short breaks."
COMMANDS = ["$study", "$cancel", "$pomodoro", "$help"]

bot_intents = discord.Intents.all()
bot = Client(intents=bot_intents)

@bot.event
async def on_ready():
    print("Bot has connected to discord.")

@bot.event
async def on_message(msg) :
    message_sender = msg.author
    user_id = message_sender.id
    if message_sender == bot.user : return
    message_string = msg.content
    if message_string.startswith("$study") :
            if user_id not in tasks :
                timer = asyncio.get_event_loop().create_task(pomodoro(msg,tasks))
                tasks[user_id] = timer
            else :
                await msg.reply("**" +message_sender.mention+ " Pomodoro Timer already set, type $cancel to stop your session.**")
                
    elif message_string.startswith("$clear") and (user_id == 132944593548214272 or user_id == 238819922677858304 or user_id == 291083531679956992) :
        await msg.channel.purge()
        await msg.channel.send("**Chat cleared.**")

    elif message_string.startswith("$cancel") :
        if user_id in tasks :
            tasks[user_id].cancel()
            tasks.pop(user_id)
            await msg.reply("**" +message_sender.mention+ " Pomodoro Timer stopped.**")
        else :
            await msg.reply("**You aren't currently studying, type $study to start.**")
    
    elif message_string.startswith("$pomodoro") :
        await msg.reply("**" +message_sender.mention+ " " +POMODORO_INFO+ "**")

    elif message_string.startswith("$help") :
        await msg.reply("**Current Commands: " +str(COMMANDS)+ "**")

    
bot.run(TOKEN)
