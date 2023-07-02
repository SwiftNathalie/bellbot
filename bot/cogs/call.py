"""Cog for slash commands"""
from __future__ import annotations

import discord
from discord import app_commands
from discord.ext import commands


class test(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="test-command", description="Test command")
    async def mcommand(self, interaction: discord.Interaction) -> None:
        """/command-1"""
        await interaction.response.send_message("Test", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    """Cog setup"""
    await bot.add_cog(test(bot=bot))