import discord
import os
from dotenv import load_dotenv
import rand_dice


# Give input in two possible forms:
# $1d20 or $3d6p2
# the p2 option adds +2 to roll result

load_dotenv()
intents = discord.Intents.all()
client = discord.Client(intents=intents)
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #don't talk to self
    if message.author == client.user:
        return

    #not really, but it could be our code
    roll = message.content
    #$1d20
    if roll.startswith('$'):
        roll = roll[1:]
        
        out = rand_dice.main(roll)
        #print ('out',out,'end')
        for item in out:
            #change "you" to username
            if "you" in item:
                item = str(message.author.display_name) + item[3:]
            await message.channel.send(item)

    #d20
    elif roll.startswith('d'):
        if roll[1].isdigit():
            
            out = rand_dice.main(roll)
            #print ('out',out,'end')
            for item in out:
                #change "you" to username
                if "you" in item:
                    item = str(message.author.display_name) + item[3:]
                await message.channel.send(item)

    #6d8 -- WIP
    elif roll[0].isdigit():
        if roll[1] == "d":
            
            out = rand_dice.main(roll)
            #print ('out',out,'end')
            for item in out:
                #change "you" to username
                if "you" in item:
                    item = str(message.author.display_name) + item[3:]
                await message.channel.send(item)

client.run(TOKEN)