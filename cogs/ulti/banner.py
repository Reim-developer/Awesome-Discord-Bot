r""""
        AWESOME DISCORD BOT
        This project is licensed under GPL-3.0 License
        https://www.gnu.org/licenses/gpl-3.0.html
        Contribution:
            - Reim-developer
"""

import discord
from discord.ext import commands
from discord import app_commands

class Banner(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = "banner",
        description = "Get the server banner"
    )
    async def banner(
        self,
        interaction: discord.Interaction
    ) -> None:
        if not interaction.guild:
            return

        if interaction.guild.banner is None:
            return await interaction.response.send_message(
                "This server has no banner",
                ephemeral = True
            )

        await interaction.response.defer()
        embed = discord.Embed(
            title = f"Banner of {interaction.guild.name}",
            description = f"[Download {interaction.guild.name}'s banner]({interaction.guild.banner.url})",
            color = 0x2f3136
        )
        embed.set_image(url = interaction.guild.banner.url)
        await interaction.followup.send(embed = embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Banner(bot))