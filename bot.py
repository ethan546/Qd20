import discord
import os
from dotenv import load_dotenv
import rand_dice

load_dotenv()
intents = discord.Intents.all()
client = discord.Client(intents=intents)
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        roll = message.content[1:]
        out = rand_dice.main(roll)
        print ('out',out,'end')
        for item in out:
            await message.channel.send(item)

client.run(TOKEN)