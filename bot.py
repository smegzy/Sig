import discord
from discord.ext import commands
import os
import requests

# Bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Your special details
CREATOR_USERNAME = "smegzyo"
BOT_TOKEN = "a49dbde24e865f80b1fcc2f8866e37d75daff1eae28a799755518deae52c05f9"  # Replace with your bot token
COC_API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM0NjBhMGRmLWZkMzUtNDAxMy1iZTg2LThlODJmNWQ3MGYyOSIsImlhdCI6MTc0MDIzMTQxMywic3ViIjoiZGV2ZWxvcGVyLzEwMWVlMTllLTJiOGMtZjc3OS02MjBiLWFkN2U3ZTRhNzlhYiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjc3LjExMS4yNDYuMTI2Il0sInR5cGUiOiJjbGllbnQifV19.Hw8S9ccsEoLbtBLObDoDW9fDH60cMYFw2naBX2zq_KsihGNGGXFQDuS_RZgLQFXQBxwAKFKjgOVDXwRmZ7jzgg"  # Replace with your Clash of Clans API Token

# Basic bot ready event
@bot.event
async def on_ready():
    print(f"{bot.user} is online and ready!")

# Special welcome for you
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.author.name == CREATOR_USERNAME:
        await message.channel.send(f"👑 Hail, my Creator {message.author.name}! What can I do for you? 😏")
    else:
        await bot.process_commands(message)

# Clash of Clans Stats Command
@bot.command()
async def coc(ctx, player_tag: str):
    headers = {"Authorization": f"Bearer {COC_API_TOKEN}"}
    url = f"https://api.clashofclans.com/v1/players/%23{player_tag.strip('#')}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        await ctx.send(f"🏆 {data['name']} | Level: {data['expLevel']} | Trophies: {data['trophies']}")
    else:
        await ctx.send("Could not fetch player stats. Make sure the tag is correct!")

# Special creator-only command
@bot.command()
async def creator(ctx):
    if ctx.author.name == CREATOR_USERNAME:
        await ctx.send("🔥 Yes, my divine Creator, what do you wish? 😈")
    else:
        await ctx.send("You dare impersonate my Creator? 😤")

# Run bot
bot.run(BOT_TOKEN)


