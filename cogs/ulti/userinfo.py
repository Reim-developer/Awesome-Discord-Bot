import discord
import datetime
from discord.ext import commands


class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx: commands.Context, user: discord.Member = None) -> None:
        if user is None:
            embed = discord.Embed(
            title = f"Thông tin về {ctx.author.name}",
            description = (
                f"* **Tên người dùng:** {ctx.author.name}\n" +\
                f"* **ID:** `{ctx.author.id}`\n" +\
                f"* **Ngày tạo tài khoản:** `{ctx.author.created_at.strftime('%d:%m:%Y')}`\n" +\
                f"* **Avatar:** [Tải xuống]({ctx.author.avatar.url})"
            ),
            colour = 0x696969,
            timestamp = datetime.datetime.now()
        )
            embed.set_thumbnail(url = ctx.author.avatar.url)

            await ctx.channel.send(embed = embed)
            return

        embed = discord.Embed(
            title = f"Thông tin về {user.name}",
            description = (
                f"* **Tên người dùng:** {user.name}\n" +\
                f"* **ID:** `{user.id}`\n" +\
                f"* **Ngày tạo tài khoản:** `{user.created_at.strftime('%d:%m:%Y')}`\n" +\
                f"* **Avatar:** [Tải xuống]({user.avatar.url})"
            ),
            colour = 0x696969,
            timestamp = datetime.datetime.now()
        )
        embed.set_thumbnail(url = user.avatar.url)

        await ctx.channel.send(embed = embed)


async def setup(bot):
    await bot.add_cog(Userinfo(bot))