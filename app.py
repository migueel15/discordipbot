import os

import discord
import requests
from discord.ext import commands, tasks

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot(command_prefix='~', intents=discord.Intents.all())

def get_ip():
    response = requests.get('https://api.ipify.org')
    return response.text

@tasks.loop(minutes=10)
async def change_status():
    print("Checking for IP change...")
    ip = get_ip()
    await bot.change_presence(activity=discord.Game(name=ip))

@bot.event
async def on_ready():
    print('Bot is ready')
    change_status.start()


print('Starting bot..')
if BOT_TOKEN:
    bot.run(BOT_TOKEN)
else:
    print('No bot token found')
