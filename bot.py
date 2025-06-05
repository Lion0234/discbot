import discord
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
ROLE_ID = int(os.getenv("ROLE_ID"))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot is online as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.strip() == "!status":
    await message.channel.send("fut pe iani")
    return

    if message.channel.id == CHANNEL_ID and message.webhook_id:
        role_mention = f"<@&{ROLE_ID}>"
        await message.channel.send(f"{role_mention} New post from followed channel!")

client.run(TOKEN)
