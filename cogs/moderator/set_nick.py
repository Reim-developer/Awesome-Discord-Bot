r"""
        AWESOME DISCORD BOT
        This project is licensed under GPL-3.0 License
        https://www.gnu.org/licenses/gpl-3.0.html
        Contribution:
            - Reim-developer
"""

import discord
from discord import app_commands, user
from discord.ext import commands


class SetNick(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = "setnick",
        description = "Change a member's nickname in the server"
    )
    @app_commands.describe(
        member = "The member to change the nickname",
        nickname = "The new nickname"
    )
    @app_commands.default_permissions(manage_nicknames = True)
    async def setnick(
        self, 
        interaction: discord.Interaction, 
        member: discord.Member, 
        nickname: str) -> None:
        if not interaction.guild:
            return

        if len(nickname) > 32:
            await interaction.response.send_message(
                "Nickname must be less than 32 characters",
                ephemeral = True
            )
            return

        if member.guild.owner_id == member.id:
            await interaction.response.send_message(
                "You cannot change the nickname of the server owner",
                ephemeral = True
            )
            return
        
        await member.edit(nick = nickname)
        await interaction.response.send_message(f"Changed {member.mention}'s nickname to {nickname}")

async def setup(bot) -> None:
    await bot.add_cog(SetNick(bot))