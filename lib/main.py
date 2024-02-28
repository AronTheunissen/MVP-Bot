import asyncio
import os
import discord
from discord.ext import commands

PREFIX = "#"
OWNER_IDS = [222071865567477760, 342948804724654082]
intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents,
    owner_ids=OWNER_IDS
)


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    with open("./bot/token.env", "r", encoding="utf-8") as token:
        TOKEN = token.read()
    await load()
    await bot.start(TOKEN)

asyncio.run(main())