import discord
import datetime
from discord.ext import commands


class MessageEdit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # WARNING: Make sure message_content intent is enable
    @commands.Cog.listener()
    async def on_message_edit(self, before_msg: discord.Message, after_msg: discord.Message) -> None:
        LOG_CHANNEL_ID = 1047035958857564170 # WARNING: Replace with your log channel

        if before_msg.author.bot: # Ignore all message from bot
            return
        
        embed = discord.Embed(
            title = "Message has been edited",
            description = (
                f"* **Original content:** {before_msg.content}\n" +\
                f"* **Content after editing:** {after_msg.content}\n" +\
                f"* **Edited at:** <t:{int(datetime.datetime.now().timestamp())}>\n" +\
                f"* **Sender:** {before_msg.author} | `{before_msg.author.id}`"
            ),
            timestamp = datetime.datetime.now(),
            colour = 0x212121
        )
        embed.set_thumbnail(url = before_msg.author.avatar.url)

        await before_msg.guild.get_channel(LOG_CHANNEL_ID).send(embed = embed)

async def setup(bot) -> None:
    await bot.add_cog(MessageEdit(bot))