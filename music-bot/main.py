"""

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2025 Reim-developer

"""

import discord
import json
from discord.ext import commands

intents = discord.Intents.all()

with open(file = "./config/config.json", mode = "r", encoding = "utf-8") as config_file:
    data = json.load(config_file)
    BOT_PREFIX = data["BOT_PREFIX"]
    BOT_TOKEN = data["BOT_TOKEN"]

cog_list = [
    "cogs.prefix.join_voice",
    "cogs.prefix.leave_voice"
]

async def setup_cogs() -> None:
    for cog in cog_list:
        
        try:
            print(f"Load cog: {cog}")
            await bot.load_extension(cog)

        except Exception as error:
            print(f"Could not load cog {cog} with error: {error}")

bot = commands.Bot (
    intents = intents,
    command_prefix = BOT_PREFIX
)

@bot.event
async def on_ready() -> None:
    print(f"Online as: {bot.user}")
    await setup_cogs()

bot.run(BOT_TOKEN)