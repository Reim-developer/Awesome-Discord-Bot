r"""
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


class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @app_commands.command(
            name = "serverinfo",
            description = "Get server information"
    )
    async def serverinfo(
        self,
        interaction: discord.Interaction
    ) -> None:
        if not interaction.guild:
            return
        
        await interaction.response.defer()
        embed = discord.Embed(
            title = f"Server Information: {interaction.guild.name}",
            description = (
                f"* **Server Name:** {interaction.guild.name}\n" +\
                f"* **Server ID:** `{interaction.guild.id}`\n" +\
                f"* **Created At:** `{interaction.guild.created_at.strftime('%d:%m:%Y')}`\n" +\
                f"* **Current Boosts:** `{interaction.guild.premium_subscription_count}` **boosts**\n" +\
                f"* **Server Owner:** <@{interaction.guild.owner_id}> | `{interaction.guild.owner_id}`\n" +\
                f"* **Categories:** `{len(interaction.guild.categories)}` **categories**\n" +\
                f"* **Text Channels:** `{len(interaction.guild.text_channels)}` **channels**\n" +\
                f"* **Voice Channels:** `{len(interaction.guild.voice_channels)}` **channels**\n" +\
                f"* **Emojis:** `{len(interaction.guild.emojis)}` **emojis**\n" +\
                f"* **Stickers:** `{len(interaction.guild.stickers)}` **stickers**" 
             ),
             timestamp = datetime.datetime.now(),
             color = 0x696969
        )

        if interaction.guild.icon is None:
            return await interaction.followup.send(embed = embed)

        embed.set_thumbnail(url = interaction.guild.icon.url)
        await interaction.followup.send(embed = embed)

async def setup(bot):
    await bot.add_cog(Serverinfo(bot))