from time import sleep
import asyncio

STUDY_TIME = 1500 # 25 MIN
SHORT_BREAK = 300 # 5 MIN
LONG_BREAK = 1200 # 20 MIN

async def pomodoro(msg,tasks) :
    user_mention = msg.author.mention
    message_channel = msg.channel
    await message_channel.send("**" +user_mention+ " :tomato: Pomodoro Timer on. Start studying! (25 minutes)**")
    await asyncio.sleep(STUDY_TIME) 
    await message_channel.send("**" +user_mention+ " first break: (5 minutes)**")
    await asyncio.sleep(SHORT_BREAK)

    for i in range(2) :
        await message_channel.send("**" +user_mention+ " start studying again! (25 minutes)**")
        await asyncio.sleep(STUDY_TIME) 
        await message_channel.send("**" +user_mention+ " break: (5 minutes)**")
        await asyncio.sleep(SHORT_BREAK)
    
    await message_channel.send("**" +user_mention+ " start studying again! (25 minutes)**")
    await asyncio.sleep(STUDY_TIME)
    await message_channel.send("**" +user_mention+ " last break: (20 minutes)**")
    await asyncio.sleep(LONG_BREAK)
    tasks.pop(msg.author.id)
    await message_channel.send("**" +user_mention+ " your study session is over, type $study to start again. :tomato:**")



