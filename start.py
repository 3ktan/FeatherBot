import constants
import discord.ext.commands
import asyncio  # learn this thing
import random

from discord.ext.commands import Bot

# figure out how implementing this will help
class ChatManager(Bot):
    pass

feather_bot = ChatManager()  # command_prefix="!")

quotes = open("quotes.txt", "w")

@feather_bot.event
async def on_ready():
    print("------------")
    print("Logged in as")
    print(feather_bot.user.name)
    print(feather_bot.user.id)
    print("------------")

# calculate command "1+1" "8%2"
@feather_bot.command()
async def hello():
    await feather_bot.say("Hello I am {0}!".format(feather_bot.user.name))

@feather_bot.command(pass_context=True)
async def me(ctx):
    await feather_bot.say("You are {0.author.name} in {0.channel.name}".format(ctx.message))

@feather_bot.command()
async def joined(member : discord.Member):
    await feather_bot.say("{0.name} joined on {0.joined_at}".format(member))

@feather_bot.command()
async def add(*nums : float):
    sumNum = 0
    for i in nums:
        sumNum += i
    await feather_bot.say("The sum of all these numbers is {0}".format(sumNum))

@feather_bot.command()
async def choose(*choice : str):
    await feather_bot.say("The best is " + random.choice(choice))

@feather_bot.command()
async def add_quote(line : str, name : str):
    pass

@feather_bot.command()
async def quote():
    pass

feather_bot.run(constants.BOT_TOKEN)
