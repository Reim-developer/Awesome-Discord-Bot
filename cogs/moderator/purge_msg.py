import discord
import json
import datetime
import os
from discord.ext import commands

class PurgeMsg(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    # require user has permission: manage_messages
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx: commands.Context, count: int = None):
        if not ctx.guild:
            return # Ignore if user try use command in DM

        config_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "config", "config.json"
        )
        with open(config_path) as configFile:
            data = json.load(configFile)
            BOT_PREFIX = data["BOT_PREFIX"]

        if count is None:
            embed = discord.Embed(
                description = (
                    "* **Vui lòng đề cập số lượng tin nhắn bạn muốn xóa!**\n" +\
                    f"`{BOT_PREFIX}purge <Số lượng tin nhắn bạn muốn xóa>`"
                ),
                colour = 0x212121,
                timestamp = datetime.datetime.now()
            )
            await ctx.channel.send(embed = embed)
            return
        
        msgDeleteCount = await ctx.channel.purge(
            limit = count,
            reason = f"Thực hiện bởi {ctx.author.name}"
        )

        embed = discord.Embed(
            description = f"* **Xóa `{len(msgDeleteCount)}` tin nhắn thành công**",
            color = 0x212121,
            timestamp = datetime.datetime.now()
        )
        await ctx.channel.send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(PurgeMsg(bot))