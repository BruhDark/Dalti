import discord
from discord.commands import slash_command, Option
from discord.ext import commands
import requests
import datetime
from config import COLORS, EMOTES

class Lyrics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def lyrics(self, ctx, query: Option(str, "Type a song title, lyric or artist")):
        """Find a song lyrics"""

        response = requests.get(f"https://some-random-api.ml/lyrics?title={query}").json()
        
        try:
         eerror = EMOTES["error"]
         cerror = COLORS["error"]
         error = response["error"]
         Embed = discord.Embed(description=f"{eerror} {error}", color=cerror)

         await ctx.respond(embed=Embed)
            
        except KeyError:
            ti = response["title"]
            author = response["author"]
            lyrics = response["lyrics"]
            thumbnail = response["thumbnail"]
            thumbnail= thumbnail["genius"]
            links = response["links"]
            links = links["genius"]
            disclaimer = response["disclaimer"]

            Embed = discord.Embed(title=f"{ti} - By {author}", 
            url=f"{links}", 
            description=f"{lyrics}",
            color=COLORS["normal"],
            timestamp=datetime.datetime.utcnow())

            Embed.set_thumbnail(url=f"{thumbnail}")
            Embed.set_footer(text=f"{disclaimer}")

            await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Lyrics(bot))
