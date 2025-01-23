r"""
        AWESOME DISCORD BOT
        This project is licensed under GPL-3.0 License
        https://www.gnu.org/licenses/gpl-3.0.html
        Contribution:
            - Reim-developer
"""
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Range

class PurgeMsg(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @app_commands.command(
        name = "purge",
        description = "Purge messages in the channel"
    )
    @app_commands.describe(
        count = "The number of messages to purge (2-100)"
    )
    @app_commands.default_permissions(manage_messages = True)
    async def purge(
        self, interaction: discord.Interaction, 
        count: Range[int, 2, 100]) -> None:
        if not interaction.guild:
            return

        await interaction.response.defer()
        await interaction.channel.purge(limit = count + 1)

        await interaction.channel.send(
            f"Successfully deleted `{count}` messages",
            delete_after = 2
        )

async def setup(bot) -> None:
    await bot.add_cog(PurgeMsg(bot))