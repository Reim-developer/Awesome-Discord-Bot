"""

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2025 Reim-developer

"""
from typing import cast
from discord import Member, Embed
from datetime import datetime
from discord.ext import commands
from alias import Context, Bot

class JoinVoicePrefix(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.command()
    async def join(self, ctx: Context) -> None:
        if not ctx.guild:
            return
        
        author = cast(Member, ctx.author)
        if not author.voice:
            await ctx.channel.send(content = (
                f"{author.name} ơi, bạn cần tham gia 1 kênh thoại bất kì để sử dụng lệnh này"
            ))
            return
        
        if ctx.voice_client:
            if author.voice.channel:

                await ctx.voice_client.disconnect(force = True)

                await author.voice.channel.connect()
                embed = Embed (
                    description = f"Di chuyển tới kênh thoại: {author.voice.channel.mention}",
                    color = 0xeba595,
                    timestamp = datetime.now()
                )
                embed.set_footer(text = f"Yêu cầu bởi: {author.name}")

                await ctx.channel.send(embed = embed)
            
                return

            await ctx.channel.send(content = (
                f"Kênh thoại của {author.name} không tồn tại hoặc bot không có quyền truy cập."
            ))

            return

        if author.voice.channel:
            voice_channel = author.voice.channel
            await voice_channel.connect()

            embed = Embed (
                description = f"Kết nối tới kênh thoại: {voice_channel.mention}",
                color = 0xeba595,
                timestamp = datetime.now()
            )
            embed.set_footer(text = f"Yêu cầu bởi: {author.name}")

            await ctx.channel.send(embed = embed)

            return 
        
        await ctx.channel.send(content = (
                f"Kênh thoại của {author.name} không tồn tại hoặc bot không có quyền truy cập."
            ))

async def setup(bot: Bot) -> None:
    await bot.add_cog(JoinVoicePrefix(bot = bot))