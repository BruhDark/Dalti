from discord.commands import slash_command
from discord.ext import commands
from config import VERSIONS, EMOTES
import discord

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def ping(self, ctx: commands.Context):
        """Measures the bot latency"""

        latency = round(self.bot.latency * 1000)

        oknos = EMOTES[f"{self.bot.user.id}"]

        Embed = discord.Embed(description=f"{oknos} My current lantecy: `{latency}ms`", color=VERSIONS[f"{self.bot.user.id}"])
        await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Ping(bot))