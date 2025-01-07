import discord
from discord.ext import commands


class SetNick(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot


    @commands.command()
    @commands.has_permissions(moderate_members = True)
    async def setnick(self, ctx: commands.Context, user: discord.Member = None, new_name: str = None) -> None:
        if not ctx.guild:
            return
        
        if user is None:
            await ctx.channel.send("Vui lòng đề cập người bạn muốn đổi biệt danh")
            return
        
        if user.id == ctx.guild.owner.id:
            await ctx.channel.send("Không thể đổi biệt danh của chủ sở hữu server!")
            return
        
        if new_name is None:
            await ctx.channel.send(f"* Vui lòng nhập tên mới mà bạn muốn set cho người dùng {user.name}")
            return
        
        if len(new_name) > 32:
            await ctx.channel.send(f"Nicname {new_name} vượt qua giới hạn 32 kí tự của discord. Vui lòng thử lại")
            return
    
        await user.edit(nick = new_name)

        await ctx.channel.send(
            content = f"Đổi biệt danh {new_name} của {user.display_name} thành công."
        )

async def setup(bot) -> None:
    await bot.add_cog(SetNick(bot))