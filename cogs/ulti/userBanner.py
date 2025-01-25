import discord
from discord.ext import commands
from discord import app_commands


class UserBanner(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(
        name = "userbanner",
        description = "Get the banner of a user"
    )
    @app_commands.describe(user = "The user to get the banner")
    async def userbanner(
        self, 
        interaction: discord.Interaction, 
        user: discord.User) -> None:
        if not interaction.guild:
            return
            
        if user.banner is None:
            return await interaction.response.send_message(
                "This user has no banner",
                ephemeral = True
            )

        await interaction.response.defer()
        embed = discord.Embed(
            title = f"Banner of {user.name}",
            description = f"[Download {user.name}'s banner]({user.banner.url})",
            color = 0x2f3136
        )
        embed.set_image(url = user.banner.url)
        await interaction.followup.send(embed = embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UserBanner(bot))