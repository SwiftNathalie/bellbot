"""Entry point for BellBot."""

from discord.ext.commands import Context
from ext.resources.bot import Bot

from dotenv import dotenv_values

conf = dotenv_values(dotenv_path='.env')

token: str | None = conf.get('TOKEN')
prefix: str | None = conf.get('PREFIX')
guild_id: str | None = conf.get('GUILD_ID')

bot = Bot(bot_token=token, bot_prefix=prefix, guild_id=guild_id) # type: ignore

@bot.command()
async def sync(ctx: Context):
    await ctx.send('Syncing...')
    await ctx.send(ctx.guild.id)
    guild = bot.get_guild(ctx.guild)# type: ignore
    bot.tree.copy_global_to(guild=ctx.guild)
    await bot.tree.sync(guild=ctx.guild)
bot.run()
