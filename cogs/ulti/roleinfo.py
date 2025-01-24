import discord
import datetime
from discord import app_commands
from discord.ext import commands

class RoleInfo(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = "roleinfo",
        description = "Get role information"
    )
    @app_commands.describe(
        role = "The role to get information"
    )
    async def roleinfO(
        self,
        interaction: discord.Interaction,
        role: discord.Role
    ) -> None:
        if not interaction.guild:
            return

        await interaction.response.defer()
        embed = discord.Embed(
            title = f"Role Information",
            color = 0x2f3136,
            timestamp = datetime.datetime.now()
        )
        embed.add_field(
            name = "ID", value = f"`{role.id}`",
            inline = False
        )
        embed.add_field(
            name = "Colour", value = f"`{role.colour}`",
            inline = False
        )
        embed.add_field(
            name = "Mention", value = f"{role.mention}",
            inline = False
        )
        embed.add_field(
            name = "Created At", value = f"<t:{int(role.created_at.timestamp())}>",
            inline = False
        )
        embed.add_field(
            name = "Hoist", value = f"`{role.hoist}`",
            inline = False
        )
        embed.add_field(
            name = "Mentionable", value = f"`{role.mentionable}`",
            inline = False
        )
        embed.add_field(
            name = "Role member(s) count", value = f"`{len(role.members)}` member(s)",
            inline = False
        )
        await interaction.followup.send(embed = embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RoleInfo(bot))