import discord

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


BOT_TOKEN = 'MTAxNjUxNTY4MzE5MTg4NTg0NQ.GlwbUQ.1tt1Nd7e_pSkZIZUR5cjA5uaal7dHo-MuouH8Q'
client.run(BOT_TOKEN)
