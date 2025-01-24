import discord
from discord import app_commands
from discord.ext import commands

class Nuke(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = "nuke",
        description = "Nuke the channel"
    )
    @app_commands.describe(
        channel = "The channel to nuke"
    )
    @app_commands.default_permissions(manage_channels = True)
    async def nuke(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel = None
    ):
        if not interaction.guild:
            return

        if channel is None:
            channel = interaction.channel

            channelName = channel.name
            await interaction.response.defer()
            await channel.delete()

            targetChannel = await channel.clone(
                name = channelName, 
                reason = f"Nuked by {interaction.user.name}"
            )
            await targetChannel.send(
                f"{interaction.user.mention}",
                delete_after = 0.1
                )
            await targetChannel.send(
                f"Successfully nuked the channel `{channelName}`",
                delete_after = 2
            )
            return

        channelName = channel.name
        await interaction.response.defer()
        await interaction.followup.send(
            f"Successfully nuked the channel `{channelName}`",
            delete_after = 2
        )
        await channel.delete()

        targetChannel = await channel.clone(
            name = channelName, 
            reason = f"Nuked by {interaction.user.name}"
        )
        await targetChannel.send(
            f"{interaction.user.mention}",
            delete_after = 0.1
            )
        await targetChannel.send(
            f"Successfully nuked the channel `{channelName}`",
            delete_after = 2
        )

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Nuke(bot))