from time import sleep
import asyncio

STUDY_TIME = 1500 # 25 MIN
SHORT_BREAK = 300 # 5 MIN
LONG_BREAK = 1200 # 20 MIN

# NEEDS TO BE RENAMED TO FUNCTION FILE

async def pomodoro(user_dm) :
    for i in range(3) :
        await user_dm.send("Start studying.")
        sleep(STUDY_TIME) 
        await user_dm.send("Break time.")
        sleep(SHORT_BREAK)
    
    await user_dm.send("Start studying.")
    sleep(STUDY_TIME)
    await user_dm.send("Break time.")



