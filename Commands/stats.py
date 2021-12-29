import discord
from discord.commands import commands
from discord.commands import slash_command
from bot import up
from config import DESCRIPTION
import datetime, time

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def stats(self, ctx):

        await ctx.defer()

        ctime = time.time()
        diff = ctime - up
        uptime = str(datetime.timedelta(seconds=diff))

        pycordV = discord.__version__

        embed = discord.Embed(title=f"{self.bot.name} Stats",description=DESCRIPTION, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Uptime", value=uptime, inline=True)
        embed.add_field(name="PyCord Version", value=pycordV, inline=True)

        embed.set_thumbnail(url=self.bot.avatar_url)
        embed.set_footer(text="Made with ♥️ by Dark")

        ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Stats(bot))