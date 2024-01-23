import discord
import random

from discord.ext import commands

# Create a bot instance
bot = commands.Bot(command_prefix='!')

# Function to read quotes from a text file
def read_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        quotes = [line.strip() for line in file.readlines() if line.strip()]
    return quotes

# Path to the text file with quotes
quotes_file_path = 'art_of_war_quotes.txt'

# Read quotes from the text file
quotes = read_quotes(quotes_file_path)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='quote')
async def quote(ctx):
    # Get a random quote from the list
    random_quote = random.choice(quotes)
    await ctx.send(f'"{random_quote}" - Sun Tzu')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')
