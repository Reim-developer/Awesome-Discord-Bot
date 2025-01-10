import discord
import datetime
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()


class MemberBan(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user: discord.User) -> None:
        LOG_CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

        BAN_REASON = await guild.fetch_ban(user)
        
        embed = discord.Embed(
            title = "Một người dùng vừa bị cấm khỏi server",
            description = (
                f"* **Username:** {user.name}\n" +\
                f"* **Bị cấm vào lúc:** <t:{int(datetime.datetime.now().timestamp())}>\n" +\
                f"* **Lí do cấm:** {BAN_REASON.reason}"
            ),
            color = 0x212121
        )
        await guild.get_channel(LOG_CHANNEL_ID).send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(MemberBan(bot))