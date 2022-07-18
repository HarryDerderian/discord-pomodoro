from time import sleep
import asyncio

STUDY_TIME = 5 #1500 # 25 MIN
SHORT_BREAK = 5 #300 # 5 MIN
LONG_BREAK = 5 #1200 # 20 MIN

async def pomodoro(msg) :
    user_mention = msg.author.mention
    await msg.reply("**" +user_mention+ " Pomodoro Timer on. Start studying! (25 minutes)**")
    await asyncio.sleep(STUDY_TIME) 
    await msg.reply("**" +user_mention+ " first break time. (5 minutes)**")
    await asyncio.sleep(SHORT_BREAK)

    for i in range(2) :
        await msg.reply("**" +user_mention+ " start studying again! (25 minutes)**")
        await asyncio.sleep(STUDY_TIME) 
        await msg.reply("**" +user_mention+ " break time. (5 minutes)**")
        await asyncio.sleep(SHORT_BREAK)
    
    await msg.reply("**" +user_mention+ " start studying again! (25 minutes)**")
    await asyncio.sleep(STUDY_TIME)
    await msg.reply("**" +user_mention+ " last break time. (20 minutes)**")
    await asyncio.sleep(LONG_BREAK)
    await msg.reply("**" +user_mention+ " your study session is over, type $study to start again.**")



