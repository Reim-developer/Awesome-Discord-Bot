import discord
import datetime
import requests
from discord.ext import commands


class AddEmoji(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot


    # require user has permission manage_expressions
    @commands.command()
    @commands.has_permissions(manage_expressions = True)
    async def addemo(self, ctx: commands.Context, emoji_name: str = None, url: str = None) -> None:
        if not ctx.guild: # Ignore if user DM bot for using command.
            return
        
        if len(ctx.guild.emojis) == ctx.guild.emoji_limit:
            embed = discord.Embed(
                description = f"* **Hiện server đã có tối đa `{ctx.guild.emoji_limit}` emoji, không thể thêm emoji nữa.**\n* **Hãy xóa một emoji, sau đó thử lại**",
                colour = 0x212121,
                timestamp = datetime.datetime.now()
            )
            await ctx.channel.send(embed = embed)
            return
        
        if url is None:
            embed = discord.Embed(
                description = (
                    "Vui lòng nhập URL của hình ảnh bạn muốn thêm làm emoji\n"
                ),
                colour = 0x212121,
                timestamp = datetime.datetime.now()
            )
            await ctx.channel.send(embed = embed)
            return

        if emoji_name is None:
            embed = discord.Embed(
                description = (
                    "Vui lòng nhập tên của hình ảnh bạn muốn thêm làm emoji\n"
                ),
                colour = 0x212121,
                timestamp = datetime.datetime.now()
            )
            await ctx.channel.send(embed = embed)
            return
        
        response = requests.get(url = url)

        await ctx.guild.create_custom_emoji(
            name = emoji_name,
            image = response.content,
            reason = f"Emoji được thêm bởi {ctx.author.name}"
        )
        embed = discord.Embed(
            description = (
                f"Thêm emoji {emoji_name} thành công"
            ),
            colour = 0x212121,
            timestamp = datetime.datetime.now()
        )
        await ctx.channel.send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(AddEmoji(bot))