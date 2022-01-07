from discord.ext import commands
import discord
import os
from discord.ext.commands.bot import when_mentioned_or
from discord.commands import slash_command
from discord.ext import tasks
from config import PREFIX, ACTIVITY, DESCRIPTION
import datetime, time
from config import COLORS, EMOTES
import math
import random
import json
import urllib

def main():
    intents = discord.Intents.all()
    Bot = commands.Bot(command_prefix=when_mentioned_or(PREFIX), 
    intents=intents)

    @Bot.event
    async def on_connect():
        print("Connected.")

        await Bot.register_commands()

        loaded = False

        if not loaded:
         global started
         started = time.time()
         loaded = True


    @Bot.event
    async def on_ready():
     print(f"Ready. Logged in as {Bot.user} - ID: {Bot.user.id}")
     print("---------")
    
    for command in os.listdir("Commands"):
        if command.endswith(".py") and not command.endswith("_"):
          Bot.load_extension(f"Commands.{command[:-3]}")
          print(f"Loaded command: {command}")

    Bot.add_cog(Stats(Bot))

    @tasks.loop(seconds=300)
    async def counter():
        users = Bot.users
        guilds = Bot.guilds
        cusers = len(users)
        cguilds = len(guilds)

        await Bot.change_presence(activity=discord.Streaming(name=f"{cguilds} and {cusers}", url="https://www.twitch.tv/oknosofficial"))

    
    @counter.before_loop
    async def beforeLoop():
        await Bot.wait_until_ready()

    Bot.run(os.environ["DISCORD_TOKEN"])

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

        request = urllib.request.urlopen("https://railway.instatus.com/summary.json")
        response = json.load(request)

        s = response["page"]
        srailway = s["status"]

        if srailway == "UP":
            srailway =  EMOTES["operational"]
        elif srailway == "HASISSUES":
            srailway = EMOTES["partialoutage"]
        elif srailway == "UNDERMAINTENANCE":
            srailway = EMOTES["maintenance"]
        else:
            srailway = EMOTES["question"]

        pycordV = discord.__version__

        embed = discord.Embed(description=DESCRIPTION, timestamp=datetime.datetime.utcnow(), color=COLORS["normal"])

        embed.set_author(name=f"{self.bot.user.name}#{self.bot.user.discriminator}", icon_url=self.bot.user.avatar.url)

        l = [":saxophone::bug:", "2.1.0-b"]
        c = random.choice(l)

        oknos = EMOTES["oknos"]

        embed.add_field(name=f"{oknos} Oknos Version", value=c, inline=True)
        embed.add_field(name=":clock1: Uptime", value=uptime, inline=True)
        
        embed.add_field(name=":snake: PyCord Version", value=f"{pycordV}", inline=False)
        embed.add_field(name="🚄 Railway Status", value=srailway, inline=True)
        embed.add_field(name=":package: Resources", value=f"[Repository](https://github.com/BruhDark/Dalti) | [Last Commit](https://github.com/BruhDark/Dalti/commit/main) | [Invite](https://discord.com/oauth2/authorize?client_id=823941047473274960&permissions=1635242211574&scope=bot%20applications.commands)")

        embed.set_footer(text="Made with ♥️")

        await ctx.respond(embed=embed)


if __name__ == "__main__":
    main()
