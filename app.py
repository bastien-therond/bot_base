from discord.ext import commands
import os
import json


def readConfig(attr):
    with open('data/config.json', 'r') as f:
        rep = json.load(f).get(f'{attr}')
    return rep

bot = commands.Bot(readConfig('prefix'))

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(readConfig('token'))