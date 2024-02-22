import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} has connected to Discord! \n'
        f'it has connected to {guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@bot.command(name='birthday', help='Wishes a happy birthday')
async def on_message(ctx):
        await ctx.send('Happy Birthday! 🎈🎉')


@bot.command(name='hey', help='Greets you')
async def welcome(ctx):
    response = 'Hello there!'
    await ctx.send(response)


@bot.command(name='earlevent', help='add values to participants for earl MVPs')
async def update_earl_list(ctx, name_player, number_of_points: int):
    score = number_of_points
    await ctx.send(f' {name_player} has a score of {score}')


@bot.command(name='quote', help='domme aron/joyce quote')
async def quote(ctx):
    list_of_quotes=[
        'Rotterdam',
        'Pikachu',
        'Waarom scheld je zo?',
        'Wil je een tafel?'
    ]

    response = random.choice(list_of_quotes)
    await ctx.send(response)


bot.run(TOKEN)