import discord
from discord.commands import slash_command
from discord.commands.commands import option
from discord.ext import commands
import requests
import datetime
from config import COLORS, EMOTES

class Lyrics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def lyrics(self, ctx, title: option(str, "Song to search")):
        """Find a song lyrics"""

        response = requests.get(f"https://some-random-api.ml/lyrics?title={title}").json()
        
        try:
         eerror = EMOTES["error"]
         cerror = EMOTES["error"]
         error = response["error"]
         Embed = discord.Embed(description=f"{eerror} {error}", color=cerror)

         ctx.respond(embed=Embed)
            
        except KeyError:
            ti = response["title"]
            author = response["author"]
            lyrics = response["lyrics"]
            thumbnail = response["thumbnail"]
            links = response["links"]
            disclaimer = response["disclaimer"]

            Embed = discord.Embed(title=f"{ti} - By {author}", 
            url=f"{links}", 
            description=f"{lyrics}", 
            timestamp=datetime.datetime.utcnow())

            Embed.set_thumbnail(url=f"{thumbnail}")
            Embed.set_footer(text=f"{disclaimer}")

            ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Lyrics(bot))