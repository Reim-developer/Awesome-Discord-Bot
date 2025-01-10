import discord
import json
from discord.ext import commands
from dotenv import load_dotenv
import os

intents = discord.Intents.all()
intents.message_content = True

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
BOT_PREFIX = os.getenv("BOT_PREFIX")

COGS_LIST: list[str] = [
    "cogs.ulti.userinfo",
    "cogs.ulti.serverinfo",
    "cogs.ulti.add_emoji",
    "cogs.ulti.create_role",
    "cogs.logging.message.message_delete",
    "cogs.logging.message.message_edit",
    "cogs.logging.message.message_send",
    "cogs.logging.member.member_join",
    "cogs.logging.member.member_left",
    "cogs.logging.member.member_ban",
    "cogs.logging.member.member_unban",
    "cogs.moderator.purge_msg",
    "cogs.moderator.set_nick"
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