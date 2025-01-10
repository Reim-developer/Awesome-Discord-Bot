import discord
import datetime
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class MemberUnban(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_unban(self, guild: discord.Guild, user: discord.User) -> None:
        LOG_CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

        embed = discord.Embed(
            title = "Một người dùng vừa được gỡ lệnh cấm khỏi server",
            description = (
                f"* **Username:** {user.name}\n" +\
                f"* **ID:** `{user.id}`\n" +\
                f"* **Gỡ lệnh cấm vào:** <t:{int(datetime.datetime.now().timestamp())}>"
            ),
            color = 0x212121,
            timestamp = datetime.datetime.now()
        )
        
        await guild.get_channel(LOG_CHANNEL_ID).send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(MemberUnban(bot))