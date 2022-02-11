from discord.commands import slash_command, Option
from discord.ext import commands
import requests
import discord
from config import VERSIONS

class Redpanda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Get an image of a red panda and an optional fact"
        self.category = "Fun"

    @slash_command()
    async def redpanda(self, ctx: commands.Context, fact: Option(bool, "Add fact?", required=False, default=False)):
     """Get an image of a red panda and an optional fact"""

     response = requests.get("https://some-random-api.ml/animal/red_panda").json()

     exp = response["fact"] if fact else ""

     Embed = discord.Embed(title="Found one!",
     description=exp,
     color=VERSIONS["{self.bot.user.id}"])

     Embed.set_image(url=response["image"])

     await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Redpanda(bot))