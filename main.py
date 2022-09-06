import os
import discord
import requests


#get crypto data
def getCryptoPrices(crypto):
    URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    r = requests.get(url=URL)
    data = r.json()
    print(data)


getCryptoPrices('bitcoin')

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
