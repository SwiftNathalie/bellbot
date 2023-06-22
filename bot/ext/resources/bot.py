"""Custom implementation of `discord.ext.commands.Bot`."""

from __future__ import annotations

from httpx import AsyncClient

from discord import Intents, app_commands
from discord.ext.commands import Bot as BotBase


class Bot(BotBase):
    """Custom implementation of `discord.ext.commands.Bot`."""

    def __init__(self,
                httpx_client: AsyncClient,
                bot_token: str,
                bot_prefix: str = '.',
                *args,
                **kwargs
                 ) -> None:

        self.httpx_client: AsyncClient = httpx_client
        self.bot_token: str = bot_token
        self.bot_prefix: str = bot_prefix
        
        super().__init__(command_prefix=self.bot_prefix,
                        intents=Intents.all(),
                        *args,
                        **kwargs
                         )
        
    async def _set(self,
             ) -> None:
        """Sets and checks `Bot` attributes and connections."""

        if self.httpx_client is None or not isinstance(self.httpx_client, AsyncClient):
            setattr(self, 'httpx_client', AsyncClient())

        # TODO: See about implementing a websocket connection check for the future webserver.
        
    
