from discord.commands import slash_command, Option
from discord.ext import commands
import requests
import discord
import datetime

class RedPanda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="red panda")
    async def redpanda(self, ctx: commands.Context, fact: Option(bool, "Add fact?", required=False, default=False)):
     """Fetches a red panda image and an optional fact"""

     response = requests.get("https://some-random-api.ml/animal/red_panda").json()

     exp = response["fact"] if fact else ""

     await ctx.respond("Looking for a red panda...")

     Embed = discord.Embed(title="Found one!",
     description=exp,
     color=discord.Color.from_rgb(156,26,4))

     Embed.set_image(url=response["image"])

     await ctx.edit_message(embed=Embed)

def setup(bot):
    bot.add_cog(RedPanda(bot))