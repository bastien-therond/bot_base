import discord
from random import randint
import json

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

'''---------config Token---------------'''
with open('config.json', 'r') as f:
    json_dict = json.load(f)
'''------------------------------------'''

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):
    if message.content == "Ping":
        phrase = randint(0, 5)
        if phrase == 0:
            await message.channel.send("Pong\nTu trouve sa marrant ?")
        elif phrase == 1:
            await message.channel.send("Pong\nMange tes morts !")
        elif phrase == 2:
            await message.channel.send("Pong\nOn se fait une partie ?")
        elif phrase == 3:
            await message.channel.send("Pong\nJ'arrive pas à DDOS google...")
        elif phrase == 4:
            await message.channel.send("Pong")

@client.event
async def on_member_join(member):
    print(f"L'utilisateur {member.display_name} a rejoint le serveur !")
    general_channel = client.get_channel(792500769668464724)
    general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")

client.run(json_dict["token"])