import discord
import random
import os
from keep_alive import keep_alive
keep_alive()

from discord.ext import commands

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = TOKEN(TOKEN=os.environ.get('TOKEN')
PREFIX = '!artofwar'

# Load quotes from the text file
with open('art_of_war_quotes.txt', 'r', encoding='utf-8') as file:
    quotes = [line.strip() for line in file.readlines()]

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='quote', help='Get a random quote from "The Art of War"')
async def get_quote(ctx):
    quote = random.choice(quotes)
    await ctx.send(quote)

bot.run(TOKEN)

