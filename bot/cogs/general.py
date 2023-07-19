"""Cog for slash commands"""
from __future__ import annotations

from discord.ext.commands import Cog

from bot.ext.resources.bot import Bot


class Fun(Cog):
    def __init__(
        self,
        bot: Bot,
    ) -> None:
        self.bot = bot

    async def cog_load(
        self,
    ) -> None:
        """Load the cog"""
        await self.bot.wait_until_ready()
        self.bot.logger.debug(msg=f"Loaded {self.qualified_name} cog.")

    # Too lazy to finish what I was intending to do, so I'll just leave this here.
    # I'll definitely finish this later, but I'm currently switching to a new OS.


async def setup(bot: Bot) -> None:
    await bot.add_cog(Fun(bot=bot))
