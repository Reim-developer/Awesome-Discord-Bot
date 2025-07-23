"""

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2025 Reim-developer

"""

from typing import cast
from discord import Member, Embed
from datetime import datetime
from discord.ext import commands 
from alias import Bot, Context

class LeaveVoicePrefix(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot 

    @commands.command()
    async def leave(self, ctx: Context) -> None:
        if not ctx.guild:
            return 
        
        author = cast(Member, ctx.author)
        if not author.voice:
            await ctx.channel.send(content = (
                f"{author.name} ơi, bạn cần tham gia một kênh thoại để sử dụng lệnh này!"
            ))
            return
        
        if not ctx.voice_client:
            await ctx.channel.send(content = (
                f"{author.name} ơi, bot không ở kênh thoại nào, không cần rời nữa!"
            ))

            return
        
        await ctx.voice_client.disconnect(force = True)

        embed = Embed (
            description = (f"Rời kênh thoại {
                author.voice.channel.name
                if author.voice.channel 
                else "'không xác định'"
            }" +
            " thành công!"),
            color = 0xeba595,
            timestamp = datetime.now()
        )
        embed.set_footer(text = (
            f"Yêu cầu bởi: {author.name}"
        ))
        await ctx.channel.send(embed = embed)

async def setup(bot: Bot) -> None:
    await bot.add_cog(LeaveVoicePrefix(bot = bot))