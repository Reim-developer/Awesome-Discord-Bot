import discord
import datetime
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class MessageEdit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # WARNING: Make sure message_content intent is enable
    @commands.Cog.listener()
    async def on_message_edit(self, before_msg: discord.Message, after_msg: discord.Message) -> None:
        LOG_CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

        if before_msg.author.bot: # Ignore all message from bot
            return
        
        embed = discord.Embed(
            title = "Tin nhắn vừa được chỉnh sửa",
            description = (
                f"* **Nội dung ban đầu:** {before_msg.content}\n" +\
                f"* **Nội dung sau khi chỉnh sửa:** {after_msg.content}\n" +\
                f"* **Chỉnh sửa vào lúc:** <t:{int(datetime.datetime.now().timestamp())}>\n" +\
                f"* **Người gửi:** {before_msg.author} | `{before_msg.author.id}`"
            ),
            timestamp = datetime.datetime.now(),
            colour = 0x212121
        )
        embed.set_thumbnail(url = before_msg.author.avatar.url)

        await before_msg.guild.get_channel(LOG_CHANNEL_ID).send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(MessageEdit(bot))