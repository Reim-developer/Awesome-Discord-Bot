r"""
        AWESOME DISCORD BOT
        This project is licensed under GPL-3.0 License
        https://www.gnu.org/licenses/gpl-3.0.html
        Contribution:
            - Reim-developer
"""

import discord
import datetime
from discord.ext import commands


class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def serverinfo(self, ctx: commands.Context) -> None:
        embed = discord.Embed(
            title = f"Server Information: {ctx.guild.name}",
            description = (
                f"* **Server Name:** {ctx.guild.name}\n" +\
                f"* **Server ID:** `{ctx.guild.id}`\n" +\
                f"* **Created At:** `{ctx.guild.created_at.strftime('%d:%m:%Y')}`\n" +\
                f"* **Current Boosts:** `{ctx.guild.premium_subscription_count}` **boosts**\n" +\
                f"* **Server Owner:** <@{ctx.guild.owner_id}> | `{ctx.guild.owner_id}`\n" +\
                f"* **Categories:** `{len(ctx.guild.categories)}` **categories**\n" +\
                f"* **Text Channels:** `{len(ctx.guild.text_channels)}` **channels**\n" +\
                f"* **Voice Channels:** `{len(ctx.guild.voice_channels)}` **channels**\n" +\
                f"* **Emojis:** `{len(ctx.guild.emojis)}` **emojis**\n" +\
                f"* **Stickers:** `{len(ctx.guild.stickers)}` **stickers**" 
             ),
             timestamp = datetime.datetime.now(),
             color = 0x696969
        )
        embed.set_thumbnail(url = ctx.guild.icon)
        await ctx.channel.send(embed = embed)

async def setup(bot):
    await bot.add_cog(Serverinfo(bot))