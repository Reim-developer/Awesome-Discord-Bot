r"""
        AWESOME DISCORD BOT
        This project is licensed under GPL-3.0 License
        https://www.gnu.org/licenses/gpl-3.0.html
        Contribution:
            - Reim-developer
"""

import discord
import datetime
from discord.ext import commands


class MemberBan(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user: discord.User) -> None:
        LOG_CHANNEL_ID = 1047035958857564170 # WARNING: Replace with your actual log channel

        BAN_REASON = await guild.fetch_ban(user)
        
        embed = discord.Embed(
            title = "A user has been banned from the server",
            description = (
                f"* **Username:** {user.name}\n" +\
                f"* **Banned at:** <t:{int(datetime.datetime.now().timestamp())}>\n" +\
                f"* **Ban reason:** {BAN_REASON.reason}"
            ),
            color = 0x212121
        )
        await guild.get_channel(LOG_CHANNEL_ID).send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(MemberBan(bot))