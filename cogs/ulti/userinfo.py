r""""
        AWESOME DISCORD BOT
        This project is licensed under GPL-3.0 License
        https://www.gnu.org/licenses/gpl-3.0.html
        Contribution:
            - Reim-developer
"""

import discord
import datetime
from discord.ext import commands
from discord import app_commands

class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name = "userinfo",
        description = "Get user information"
    )
    @app_commands.describe(
        user = "The user to get information"
    )
    async def userinfo(
        self, 
        interaction: discord.Interaction, 
        user: discord.User = None) -> None:
        if not interaction.guild:
            return
        
        if user is None:
            await interaction.response.defer()
            embed = discord.Embed(
                title = "User Information",
                description = (
                    f"**Mention:** {interaction.user.mention}\n" +
                    f"**Display Name:** {interaction.user.name}\n" +
                    f"**ID:** `{interaction.user.id}`\n" +
                    f"**Created At:** <t:{int(interaction.user.created_at.timestamp())}>"
                ),
                color = 0x2f3136
            )
            if interaction.user.avatar is not None:
                embed.set_thumbnail(url = interaction.user.avatar.url)

            await interaction.followup.send(embed = embed)
            return
        
        await interaction.response.defer()
        embed = discord.Embed(
            title = "User Information",
            description = (
                f"**Mention:** {user.mention}\n" +
                f"**Display Name:** {user.name}\n" +
                f"**ID:** `{user.id}`\n" +
                f"**Created At:** <t:{int(user.created_at.timestamp())}>"
            ),
            color = 0x2f3136
        )
        if user.avatar is not None:
            embed.set_thumbnail(url = user.avatar.url)

        await interaction.followup.send(embed = embed)

async def setup(bot):
    await bot.add_cog(Userinfo(bot))