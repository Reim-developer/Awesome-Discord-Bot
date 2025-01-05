import discord
import datetime
from discord.ext import commands


class MemberLeft(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member) -> None:
        LOG_CHANNEL_ID = 1047035958857564170

        embed = discord.Embed(
            title = "Vừa có một thành viên vừa rời khỏi server",
            description = (
                f"* **Username:** {member.name}\n" +\
                f"* **ID:** `{member.id}`\n" +\
                f"* **Rời vào lúc:** <t:{int(datetime.datetime.now().timestamp())}>"
            ),
            colour = 0x212121,
            timestamp = datetime.datetime.now() 
        )
        embed.set_thumbnail(url = member.avatar.url)

        await member.guild.get_channel(LOG_CHANNEL_ID).send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(MemberLeft(bot))