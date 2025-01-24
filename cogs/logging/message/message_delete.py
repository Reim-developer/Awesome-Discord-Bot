import discord
import datetime
from discord.ext import commands


class MessageDelete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # WARNING: Make sure message_content is enable
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        LOG_CHANNEL_ID = 1047035958857564170 # WARNING: REPLACE WITH YOUR LOG CHANNEL ID

        embed = discord.Embed(
            title = "A message has just been deleted",
            description = (
                f"* **Message content:** {message.content}\n" +\
                f"* **Deleted at:** <t:{int(datetime.datetime.now().timestamp())}>\n" +\
                f"* **Sender:** {message.author} | `{message.author.id}`"
            ),
            color = 0x212121,
            timestamp = datetime.datetime.now()
        )
        embed.set_thumbnail(url = message.author.avatar.url)

        # Make sure your log channel id is exists.
        await message.guild.get_channel(LOG_CHANNEL_ID).send(embed = embed)


async def setup(bot) -> None:
    await bot.add_cog(MessageDelete(bot))