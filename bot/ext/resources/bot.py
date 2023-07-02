"""Custom implementation of `discord.ext.commands.Bot`."""

from __future__ import annotations

import asyncio
import pkgutil

import discord
from discord import Guild, Intents, Object, app_commands
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Cog, Context, command
from httpx import AsyncClient


class Bot(BotBase):
    """Custom implementation of `discord.ext.commands.Bot`."""

    def __init__(
        self,
        bot_token: str,
        bot_prefix: str = ".",
        guild_id: Guild | int | None = None,
        httpx_client: AsyncClient | None = None,
        *args,
        **kwargs,
    ) -> None:
        self.bot_token = bot_token
        self.bot_prefix = bot_prefix
        self.guild = guild_id
        self.httpx_client = httpx_client

        super().__init__(
            command_prefix=self.bot_prefix, intents=Intents.all(), *args, **kwargs
        )

    async def _set(
        self,
    ) -> None:
        if self.httpx_client is None or not isinstance(self.httpx_client, AsyncClient):
            setattr(self, "httpx_client", AsyncClient())

        if self.guild is None or not isinstance(self.guild, Object):
            setattr(self, "guild", Object(id=0))

        if self.bot_token is None or not isinstance(self.bot_token, str):
            raise ValueError("Bot token must be a string.")

    async def setup_hook(self) -> None:
        await self._set()
        packages: list[pkgutil.ModuleInfo] = [
            package for package in pkgutil.iter_modules(["cogs"])
        ]

        for package in packages:
            await self.load_extension(f"cogs.{package.name}")
            print(f"Loaded {package.name} cog.")

        return await super().setup_hook()

    def run(self) -> None:
        asyncio.run(super().run(self.bot_token))  # type: ignore
