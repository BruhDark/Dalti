from discord.commands import slash_command
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def ping(self, ctx):
        """Measures the bot latency"""

        latency = round(self.bot.latency * 1000)

        await ctx.respond(":ping_pong: Pong! My latency: `{latency}ms`")

def setup(bot):
    bot.add_cog(Ping(bot))