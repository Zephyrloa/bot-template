import asyncio
import discord
from discord.ext import commands
import glob
import json
import os

with open('data.json') as f:
    data = json.load(f)
    global TOKEN
    TOKEN = data['TOKEN']

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='h!', intents = intents)

async def main():
    async with bot:
        files = glob.glob("./Cogs/*.py")
        for file in files:
            file = os.path.splitext(os.path.basename(file))[0]
            await bot.load_extension(f"Cogs.{file}")
        await bot.start(TOKEN)


asyncio.run(main())