import os
import discord
import requests
from replit import db


#get crypto data
def getCryptoPrices(crypto):
    URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    r = requests.get(url=URL)
    data = r.json()

    #putting crypto and their prices in db
    for i in range(len(data)):
        db[data[i]['id']] = data[i]['current_price']

    if crypto in db.keys():
        return db[crypto]
    else:
        return None


def isCryptoSupported(crypto):
    if crypto in db.keys():
        return True
    else:
        return False


print(getCryptoPrices('bitcoin'))

#instantiate a discord client
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'You have logged in as {client}')


#called whenever there is a message in the chat
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('--help'):
        await message.channel.send('yeet')


BOT_TOKEN = os.environ['BOT_TOKEN']
client.run(BOT_TOKEN)
