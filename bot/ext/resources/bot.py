"""Custom implementation of `discord.ext.commands.Bot`."""

from __future__ import annotations

import pkgutil

from discord import Guild, Intents
from discord.ext.commands import Bot as BotBase
from httpx import AsyncClient

from bot.ext.utils.logger import formatter, logger


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

    async def _bootstrap(
        self,
    ) -> None:
        """Bootstraps the instance of `Bot` with external services, such as the web-server and database."""
        if self.httpx_client is None or not isinstance(self.httpx_client, AsyncClient):
            self.logger.warning(
                msg=f"{self.httpx_client} is not a valid HTTPX client, defaulting to AsyncClient."
            )
            setattr(self, "httpx_client", AsyncClient())

        if self.guild is None or not isinstance(self.guild, Guild | int):
            self.logger.warning(msg=f"{self.guild} is not a valid guild, defaulting to None.")
            setattr(self, "guild", None)

    async def setup_hook(self) -> None:
        await self._bootstrap()
        packages: list[pkgutil.ModuleInfo] = [package for package in pkgutil.iter_modules(["bot/cogs"])]
        for package in packages:
            await self.load_extension(name=f"bot.cogs.{package.name}")
            self.logger.debug(
                msg=f"Extension loaded: {package.name}",
            )

        return await super().setup_hook()

    def run(self) -> None:
        return super().run(token=self.bot_token, log_formatter=formatter)
