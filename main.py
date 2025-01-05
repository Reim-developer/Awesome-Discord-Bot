import discord
import json
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

with open("./config.json") as configFile:
    data = json.load(configFile)
    BOT_TOKEN = data["TOKEN"]
    BOT_PREFIX = data["BOT_PREFIX"]

COGS_LIST: list[str] = [
    "cogs.ulti.userinfo",
    "cogs.ulti.serverinfo",
    "cogs.logging.message_delete"
]

async def load_cogs() -> None:
    for cog in COGS_LIST:
        print(f"Load cog {cog}")
        await bot.load_extension(cog)

bot = commands.Bot(
    command_prefix = BOT_PREFIX,
    intents =  intents 
)

@bot.event
async def on_ready():
    await load_cogs()
    print(f"Online as {bot.user}")

bot.run(BOT_TOKEN)  