import discord
import random
from smite_data import GODS
from token_data import bot_token

mages     = []
warriors  = []
guardians = []
hunters   = []
assassins = []

ROLE_TO_LIST = {
    "mage" : mages,
    "warrior" : warriors,
    "guardian" : guardians,
    "hunter" : hunters,
    "assassin" : assassins}

for god in GODS:
    ROLE_TO_LIST[GODS[god]].append(god)

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} has been activated.'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'jockiejockhouse':
        if "baytak" in user_message.lower():
            await message.channel.send(f'JAAAAAAA {username}, DAGS FÖR LITE YEKHREB BAYTAK!')
            return
    elif message.channel.name == 'bot-test' or message.channel.name == 'grg':
        if "smite" in user_message.lower():
            await message.channel.send(f'JAAAAAAAAAA SMITERAS {username}!')
            return
        
        elif "bot" in user_message.lower():
            await message.channel.send('Kalla mig inte b-ordet jao')
            return

        elif user_message.lower() == "yo":
            await message.channel.send("Yoo!")
            return
        
        elif "random" in user_message.lower():
            if "god" in user_message.lower():
                    index = random.randint(0, len(GODS.keys()) - 1)
                    gods = list(GODS.keys())
                    await message.channel.send("Your pog random god is {}".format(gods[index]))
                    return
            for role in ["mage", "guardian", "warrior", "assassin", "hunter"]:
                if role in user_message.lower():
                    index = random.randint(0, len(ROLE_TO_LIST[role]) - 1)
                    await message.channel.send('Your pog random {} is {}'.format(role, ROLE_TO_LIST[role][index]))
                    return
        return


client.run(bot_token)


