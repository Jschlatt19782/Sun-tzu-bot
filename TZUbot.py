import discord
import random
import os
from keep_alive import keep_alive
keep_alive()

from discord.ext import commands

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = (os.environ.get('TOKEN'))
PREFIX = '!artofwar'

with open('art_of_war_quotes.txt', 'r', encoding='utf-8') as file:
    quotes = [line.strip() for line in file.readlines()]

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith(PREFIX):
        quote = random.choice(quotes)
        await message.channel.send(quote)

    await bot.process_commands(message)

@bot.command(name='quote', help='Get a random quote from "The Art of War"')
async def get_quote(ctx):
    quote = random.choice(quotes)
    await ctx.send(quote)
 
bot.run(TOKEN)

