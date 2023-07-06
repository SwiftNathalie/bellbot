"""Custom implementation of `discord.ext.commands.Bot`."""

from __future__ import annotations

import pkgutil

from discord import Guild, Intents
from discord.ext.commands import Bot as BotBase
from httpx import AsyncClient

from bot.ext.utils.logger import logger


class Bot(BotBase):
    """Custom implementation of `discord.ext.commands.Bot`."""

    def __init__(
        self,
        bot_token: str,
        *,
        bot_prefix: str = ".",
        guild_id: Guild | int | None = None,
        httpx_client: AsyncClient | None = None,
    ) -> None:
        self.bot_token = bot_token
        self.bot_prefix = bot_prefix
        self.guild = guild_id
        self.httpx_client = httpx_client
        self.logger = logger

        super().__init__(command_prefix=self.bot_prefix, intents=Intents.all(), case_insensitive=True)

    async def _set(
        self,
    ) -> None:
        if self.httpx_client is None or not isinstance(self.httpx_client, AsyncClient):
            setattr(self, "httpx_client", AsyncClient())
            self.logger.warning(
                msg=f"{self.httpx_client} is not a valid HTTPX client, defaulting to AsyncClient."
            )

    async def setup_hook(self) -> None:
        await self._set()
        packages: list[pkgutil.ModuleInfo] = [package for package in pkgutil.iter_modules(["cogs"])]

        for package in packages:
            await self.load_extension(f"cogs.{package.name}")
            print(f"Loaded {package.name} cog.")

        return await super().setup_hook()

    def run(self) -> None:
        return super().run(token=self.bot_token)
