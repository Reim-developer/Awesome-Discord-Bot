import discord
import datetime
from discord.ext import commands


class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def serverinfo(self, ctx: commands.Context) -> None:
        embed = discord.Embed(
            title = f"Thông tin về server {ctx.guild.name}",
            description = (
                f"* **Tên server:** {ctx.guild.name}\n" +\
                f"* **ID server: ** `{ctx.guild.id}`\n" +\
                f"* **Ngày tạo server:** `{ctx.guild.created_at.strftime('%d:%m:%Y')}`\n" +\
                f"* **Số boost hiện tại:** `{ctx.guild.premium_subscription_count}` **boost**\n" +\
                f"* **Server owner:** <@{ctx.guild.owner_id}> | `{ctx.guild.owner_id}`\n" +\
                f"* **Số danh mục:** `{len(ctx.guild.categories)}` **danh mục**\n" +\
                f"* **Số kênh văn bản:** `{len(ctx.guild.text_channels)}` **kênh**\n" +\
                f"* **Số kênh voice:** `{len(ctx.guild.voice_channels)}` **kênh**\n" +\
                f"* **Số emoji:** `{len(ctx.guild.emojis)}` **emoji**\n" +\
                f"* **Số sticker:** `{len(ctx.guild.stickers)}` **sticker**" 
             ),
             timestamp = datetime.datetime.now(),
             color = 0x696969
        )
        embed.set_thumbnail(url = ctx.guild.icon)
        await ctx.channel.send(embed = embed)

async def setup(bot):
    await bot.add_cog(Serverinfo(bot))