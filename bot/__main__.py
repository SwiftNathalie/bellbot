"""Entry point for BellBot."""

from discord.ext.commands import Context
from dotenv import dotenv_values

from bot.ext.resources.bot import Bot

conf = dotenv_values(dotenv_path=".env")

token: str | None = conf.get("TOKEN")
prefix: str | None = conf.get("PREFIX")
guild_id: int | None = conf.get("GUILD_ID")  # type: ignore

bot = Bot(bot_token=token, bot_prefix=prefix, guild_id=guild_id)  # type: ignore


@bot.command(name="Syncronize", aliases=["sync"], description="Syncronize all slash commands")
async def sync(ctx: Context) -> None:
    """Syncronize all slash commands"""
    await bot.tree.copy_global_to(ctx.guild_id)  # type: ignore
    await bot.tree.sync(ctx.guild_id)  # type: ignore


bot.run()
