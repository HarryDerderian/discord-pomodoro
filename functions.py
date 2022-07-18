from time import sleep

STUDY_TIME = 5 #1500 # 25 MIN
SHORT_BREAK = 5 #300 # 5 MIN
LONG_BREAK = 5 #1200 # 20 MIN

async def pomodoro(msg) :
    user_mention = msg.author.mention
    for i in range(3) :
        await msg.reply("**" +user_mention+ " start studying.**")
        sleep(STUDY_TIME) 
        await msg.reply("**" +user_mention+ " break time.**")
        sleep(SHORT_BREAK)
    
    await msg.reply("**" +user_mention+ " start studying.**")
    sleep(STUDY_TIME)
    await msg.reply("**" +user_mention+ " break time.**")



