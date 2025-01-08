import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter

class SetNick(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot


    @commands.command()
    @commands.has_permissions(moderate_members = True)
    async def setnick(self, ctx: commands.Context, user: str = None, new_name: str = None) -> None:
        if not ctx.guild:
            return
        
        if user is None:
            await ctx.channel.send("Vui lòng đề cập người bạn muốn đổi biệt danh")
            return
        
        converter = MemberConverter()

        try:
            user = await converter.convert(ctx, user)
        except commands.MemberNotFound:
            await ctx.channel.send("Không tìm thấy thành viên này. Hãy chắc chắn rằng bạn tag đúng!")
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
    
        try:
            await user.edit(nick=new_name)
            await ctx.channel.send(f"Đã đổi biệt danh của **{user.display_name}** thành **{new_name}**.")
        except discord.Forbidden:
            await ctx.channel.send("Bot không có quyền đổi biệt danh cho người này!")
        except Exception as e:
            await ctx.channel.send(f"Đã xảy ra lỗi: {e}")

async def setup(bot) -> None:
    await bot.add_cog(SetNick(bot))