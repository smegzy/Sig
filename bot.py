import discord
from discord.ext import commands
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Get sensitive data from environment variables
CREATOR_USERNAME = "smegzyo"
BOT_TOKEN = os.getenv("BOT_TOKEN")
COC_API_TOKEN = os.getenv("COC_API_TOKEN")

# Bot ready event
@bot.event
async def on_ready():
    print(f"{bot.user} is online and ready!")

# Handle messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.name == CREATOR_USERNAME:
        await message.channel.send(f"👑 Hail, my Creator {message.author.name}! What can I do for you? 😏")

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

# Ensure bot token exists before running
if BOT_TOKEN is None:
    print("❌ BOT_TOKEN is missing! Set it in your environment variables.")
else:
    bot.run(BOT_TOKEN)