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

class MemberJoin(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    # WARNING: Make sure intent_member is enable
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        LOG_CHANNEL_ID = 1047035958857564170 # WARNING: Replace with your discord log channel

        embed = discord.Embed(
            title = "A new member has joined the server",
            description = (
                f"* **Username:** {member.name}\n" +\
                f"* **ID:** `{member.id}`\n" +\
                f"* **Joined at: <t:{int(datetime.datetime.now().timestamp())}>**"
            ),
            color = 0x212121,
            timestamp = datetime.datetime.now()
        )
        embed.set_thumbnail(url = member.avatar.url)

        await member.guild.get_channel(LOG_CHANNEL_ID).send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(MemberJoin(bot))