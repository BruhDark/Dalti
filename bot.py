from discord.ext import commands
import discord
import os
from discord.ext.commands.bot import when_mentioned_or
from discord.commands import slash_command
from config import PREFIX, ACTIVITY, DESCRIPTION
import datetime, time
from config import COLORS
import math
import random

def main():
    intents = discord.Intents.all()
    Dalti = commands.Bot(command_prefix=when_mentioned_or(PREFIX), 
    intents=intents)

    act = discord.Game(ACTIVITY)

    @Dalti.event
    async def on_connect():
        print("Connected.")

        await Dalti.register_commands()

        try:
         await Dalti.change_presence(status=discord.Status.online, activity=act)
     
        except discord.InvalidArgument:
         pass

        loaded = False

        if not loaded:
         global started
         started = time.time()
         loaded = True


    @Dalti.event
    async def on_ready():
     print(f"Ready. Logged in as {Dalti.user} - ID: {Dalti.user.id}")
     print("---------")
    
    for command in os.listdir("Commands"):
        if command.endswith(".py") and not command.endswith("_"):
          Dalti.load_extension(f"Commands.{command[:-3]}")
          print(f"Loaded command: {command}")

    Dalti.add_cog(Stats(Dalti))
    
    Dalti.run(os.environ["DISCORD_TOKEN"])

# Stats command here to avoid import up
class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def stats(self, ctx):
        """Get Dalti's stats"""

        seconds = math.floor(time.time() - started)

        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)

        days, hours, minutes, seconds = None, None, None, None

        if d:
            days = f"{d}d"
        if h:
            hours = f"{h}h"
        if m:
            minutes = f"{m}m"
        if s:
            seconds = f"{s}s"

        uptime = f"{days or ''} {hours or ''} {minutes or ''} {seconds or ''}".strip()

        pycordV = discord.__version__

        embed = discord.Embed(description=DESCRIPTION, timestamp=datetime.datetime.utcnow(), color=COLORS["dalti"])

        embed.set_author(name=f"{self.bot.user.name}#{self.bot.user.discriminator}", icon_url=self.bot.user.avatar.url)

        l = [":saxophone::bug:", "2.1.0-b"]
        c = random.choice(l)

        embed.add_field(name=":clock1: Uptime", value=uptime, inline=True)
        embed.add_field(name=":snake: PyCord Version", value=f"{pycordV}", inline=True)
        embed.add_field(name=":service_dog: Dalti Version", value=c)
        embed.add_field(name=":package: Resources", value=f"[Repository](https://gitub.com/BruhDark/Dalti) | [Last Commit](https://github.com/BruhDark/Dalti/commit/main) | [Invite](https://discord.com/oauth2/authorize?client_id=823941047473274960&permissions=1635242211574&scope=bot%20applications.commands)")

        embed.set_footer(text="Made with ♥️")

        await ctx.respond(embed=embed)


if __name__ == "__main__":
    main()
