r""""
        AWESOME DISCORD BOT
        This project is licensed under GPL-3.0 License
        https://www.gnu.org/licenses/gpl-3.0.html
        Contribution:
            - Reim-developer
"""

import discord
from discord import app_commands
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = "avatar",
        description = "Get the avatar of a user"
    )
    @app_commands.describe(
        user = "The user to get the avatar"
    )
    async def avatar(self, interaction: discord.Interaction, user: discord.User) -> None:
        if not interaction.guild:
            return

        if user.avatar is None:
            return await interaction.response.send_message(
                "This user has no avatar",
                ephemeral = True
            )

        embed = discord.Embed(
            title = f"Avatar of {user.name}",
            description = f"[Download {user.name}'s avatar]({user.avatar.url})",
            color = 0x696969
        )
        embed.set_image(url = user.avatar.url)

        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Avatar(bot))