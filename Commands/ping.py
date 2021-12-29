import discord
from discord.commands import slash_command
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def ping(self, ctx):
        """Measures the bot latency"""
        await ctx.respond(f"Pong! {round(self.bot.latency * 1000)}")

def setup(bot):
    bot.add_cog(Ping(bot))