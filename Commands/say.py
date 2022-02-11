from discord.commands import slash_command
from discord.ext import commands
from discord.commands import permissions
from discord import Forbidden
from config import AUTHORIZED, EMOTES, COLORS
import discord

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Make oknos say something"
        self.category = "Developer"

    @slash_command()
    async def say(self, ctx, arguments: str):
        """Say something as Oknos"""

        if ctx.author.id in AUTHORIZED:

         try:
             await ctx.send(arguments)
             await ctx.respond("Sent message.", ephemeral=True)

         except Forbidden:
             error = EMOTES["error"]
             Embed = discord.Embed(description=f"{error} I was unable to send the message. I'm missing permissions.", color=COLORS["error"])
             await ctx.respond(embed=Embed, ephemeral=True)
        else:

            error = EMOTES["error"]
            Embed = discord.Embed(description=f"{error} You are not authorized to run this command.", color=COLORS["error"])
            await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Say(bot))
