"""Cog for the Stable Diffusion's API."""

from __future__ import annotations
import re

from ext.resources.bot import Bot
import discord
from discord import app_commands
import discord.ext.commands
from discord.ext.commands import Cog, Context, command


class StableDiffusion(Cog):
    """Cog for the Stable Diffusion's API."""

    def __init__(self,
                 bot: Bot
                    ) -> None:
        self.bot = bot

    
    