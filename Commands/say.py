from discord.commands import slash_command
from discord.ext import commands
from discord.commands import permissions
from discord import Forbidden
from config import AUTHORIZED, EMOTES, COLORS
import discord

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def say(self, ctx, arguments: str):
        """Return what you said as Dalti"""

        if ctx.author.id in AUTHORIZED:

         try:
             await ctx.send(arguments)
             await ctx.respond("Sent message.", ephemeral=True)

         except Forbidden:
             ctx.respond("I was not able to send the message, I am missing permissions.", ephemeral=True)

        else:

            error = EMOTES["error"]
            Embed = discord.Embed(description=f"{error} You are not authorized to run this command.", color=COLORS["error"])
            ctx.respond()

def setup(bot):
    bot.add_cog(Say(bot))