import discord
import datetime
from discord.ext import commands


class MessageSend(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    # WARNING: Make sure message_content intent is enable
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        LOG_CHANNEL_ID = 1047035958857564170 # WARNING: REPLACE WITH YOUR LOG CHANNEL ID

        if message.author.bot: # Ignore all message from bot
            return 
        
        embed = discord.Embed(
            title = "Một tin nhắn vừa được gửi đi",
            description = (
                f"* **Nội dung tin nhắn:** {message.content}\n" +\
                f"* **Gửi vào lúc:** <t:{int(datetime.datetime.now().timestamp())}>\n" +\
                f"* **Người gửi:** {message.author} | `{message.author.id}`"
            ),
            colour = 0x212121,
            timestamp = datetime.datetime.now() 
        )
        embed.set_thumbnail(url = message.author.avatar.url)

        await message.guild.get_channel(LOG_CHANNEL_ID).send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(MessageSend(bot))