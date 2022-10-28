import os
import random

from discord.ext import commands
from dotenv import load_dotenv
import discord

# load the .env file from your root DIR
load_dotenv()

# gets the Bot token from the env file
TOKEN = os.getenv('DISCORD_TOKEN')

# sets the bot as a client with a prefix, and intents to check on all channels
# """
# param: command_prefix
# type: string
# description: set the command prefix for Discord messages
# param: intents
# type: event
# description: sets intents. Read more on intents here: https://discordpy.readthedocs.io/en/stable/intents.html
# """
bot = commands.Bot(command_prefix='^', intents = discord.Intents.all())

# checks for certain messages and has a 'help' response
# """
# param: name
# type: string
# description: set the message to which the bot has to look for
# param: help
# type: string
# description: if {prefix}+{help} is called, responds with whatever is in the parameter
# """
@bot.command(name='terrible', help='Responds with (=3=) turrible ...')
async def on_message(ctx):
    # list of responses, separated by a comma
    responseList = [
        '(=3=) turrible ...',
    ]

    # sends a response
    response = random.choice(responseList)
    await ctx.send(response)

# runs the program on ~py bot.py
def runBot():
    bot.run(TOKEN)
