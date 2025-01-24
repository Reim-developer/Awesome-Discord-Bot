import discord
import datetime
from discord.ext import commands

class MemberUnban(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_unban(self, guild: discord.Guild, user: discord.User) -> None:
        LOG_CHANNEL_ID = 1047035958857564170

        embed = discord.Embed(
            title = "A user has been unbanned from the server",
            description = (
                f"* **Username:** {user.name}\n" +\
                f"* **ID:** `{user.id}`\n" +\
                f"* **Unbanned at:** <t:{int(datetime.datetime.now().timestamp())}>"
            ),
            color = 0x212121,
            timestamp = datetime.datetime.now()
        )
        
        await guild.get_channel(LOG_CHANNEL_ID).send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(MemberUnban(bot))