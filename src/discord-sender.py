import discord
import os
import argparse
from dotenv import load_dotenv

#region Check for required environment variables

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    print("DISCORD_TOKEN is not set.")
    exit(1)

if('DISCORD_CHANNEL_ID' not in os.environ):
    print("DISCORD_CHANNEL_ID is not set.")
    exit(1)

if os.getenv('DISCORD_CHANNEL_ID').isdigit() == False:
    print("DISCORD_CHANNEL_ID is not a number.")
    exit(1)

#endregion

#region Parse CLI Argument

parser = argparse.ArgumentParser(description="Send a message to a Discord channel.")
parser.add_argument('--message', type=str, required=True, help='The message to send to the Discord channel.')
args = parser.parse_args()

#endregion

#region Prepare Discord client

intents = discord.Intents.default()
client = discord.Client(intents=intents)
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

#endregion

#region Send message to Discord channel on bot startup

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
    channel = client.get_channel(CHANNEL_ID)
    
    if channel is not None:
        await channel.send(args.message)
        print(f"Sent message: {args.message}")
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")
    
    await client.close()

client.run(TOKEN)

#endregion
