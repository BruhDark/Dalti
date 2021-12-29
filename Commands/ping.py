import discord
from discord.commands import slash_command
from discord.ext import commands
from config import EMOTES, COLORS

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def ping(self, ctx):
        """Measures the bot latency"""

        latency = round(self.bot.latency * 1000)

        if latency < 100:
            emote = EMOTES["gdot"]
            color = COLORS["success"]
        elif latency < 300:
            emote = EMOTES["ydot"]
            color = COLORS["warning"]
        else:
            emote = EMOTES["rdot"]
            color = COLORS["error"]

        embed = discord.Embed(description=f"{emote} Pong! My latency: `{latency}ms`", color=discord.Colour.from_rgb(color))
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))