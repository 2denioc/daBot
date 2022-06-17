import discord
from discord.ext import commands
import asyncio
import os
import datetime


intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.reactions = True
activity = discord.Activity(type=discord.ActivityType.watching, name="ark")
bot = commands.Bot(intents=intents, activity=activity, command_prefix='?', status=discord.Status.idle)
@bot.event
# Initialize and load cogs
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print(bot.user.name)
    print(bot.user.id)
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

# Gif task to loop
async def marvin():
    channel_id = 931098322515689517
    await bot.wait_until_ready()
    channel = bot.get_channel(channel_id)
    await channel.send("<@245084504006328321>")
    await channel.send("https://media.discordapp.net/attachments/733661388261818408/980060791233445918/what_is_his_plan.gif")

# Looping a task for a day
async def timer():
    when = datetime.time(10, 51, 0)
    now = datetime.datetime.utcnow()
    if now.time() > when:
        seconds = (datetime.datetime.combine(now.date() + datetime.timedelta(days=1), datetime.time(0)) - now).total_seconds()
        await asyncio.sleep(seconds)
    while True:
        now = datetime.datetime.utcnow()
        target_time = datetime.datetime.combine(now.date(), when)
        seconds_until_target = (target_time - now).total_seconds()
        await asyncio.sleep(seconds_until_target)
        await marvin()
        tomorrow = datetime.datetime.combine(now.date() + datetime.timedelta(days=1), datetime.time(0))
        seconds = (tomorrow - now).total_seconds()
        await asyncio.sleep(seconds)

bot.loop.create_task(timer())
bot.run('your token here')