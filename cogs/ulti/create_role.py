import discord
from discord.ext import commands


class CreateRole(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def rolecreate(self, ctx: commands.Context, *, role_name: str = None, ) -> None:
        if not ctx.guild:
            return
        
        if role_name is None:
            await ctx.channel.send("Vui lòng đề cập tên role bạn muốn tạo")
            return
        
        await ctx.guild.create_role(
            name = role_name,
            reason = f"Thực hiện bởi {ctx.author.name}"
        )

        await ctx.channel.send(f"Tạo vai trò `{role_name}` thành công")

async def setup(bot) -> None:
    await bot.add_cog(CreateRole(bot))