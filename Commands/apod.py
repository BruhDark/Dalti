from discord.commands import slash_command, Option
from discord.ext import commands
import discord
import requests

class Apod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def apod(self, ctx, explanation: Option(bool, "Add explanation?", required=False, default=False)):
     """Retreive today's APOD from Nasa"""

     response = requests.get("https://api.nasa.gov/planetary/apod?api_key=2JvlKQHQlB1RffyXdtxcpb64HlBE6QzEp0yC0CSq").json()

     exp = response["explanation"] if explanation else ""

     Embed = discord.Embed(title=response["title"],
     description=exp,
     color=discord.Color.from_rgb(102,106,242))

     Embed.set_image(url=response["hdurl"])
     Embed.set_footer(text="© NASA - {}".format(response["date"]), icon_url="https://media.discordapp.net/attachments/881968886248009821/923706098769358848/NASA_logo.png")

     await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Apod(bot))