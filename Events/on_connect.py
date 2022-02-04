import discord
from discord.ext import commands
from discord.commands import slash_command
from config import EMOTES, COLORS, VERSIONS, DESCRIPTION
import time
import json
import urllib
import math
import datetime

class OnConnect(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def stats(self, ctx):
        """View stats about Oknos"""

        seconds = math.floor(time.time() - started)

        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)

        days, hours, minutes, seconds = None, None, None, None

        if d:
            days = f"{d} Days"
        if h:
            hours = f"{h} Hours"
        if m:
            minutes = f"{m} Minutes"
        if s:
            seconds = f"{s} Seconds"

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

        embed = discord.Embed(description=DESCRIPTION, timestamp=datetime.datetime.utcnow(), color=VERSIONS[f"{self.bot.user.id}"])

        embed.set_author(name=f"{self.bot.user.name}#{self.bot.user.discriminator}", icon_url=self.bot.user.avatar.url)

        oknos = EMOTES[f"{self.bot.user.id}"]

        embed.add_field(name=f"{oknos} Oknos Version", value="2.2.3-b", inline=True)
        embed.add_field(name=":clock1: Uptime", value=uptime, inline=True)
        
        embed.add_field(name=":snake: PyCord Version", value=f"{pycordV}", inline=True)
        embed.add_field(name="🚄 Railway Status", value=srailway, inline=True)
        embed.add_field(name=":package: Resources", value=f"[Repository](https://github.com/BruhDark/Oknos) | [Last Commit](https://github.com/BruhDark/Oknos/commit/main) | [Invite](https://discord.com/oauth2/authorize?client_id=823941047473274960&permissions=1635242211574&scope=bot%20applications.commands)")

        await ctx.respond(embed=embed)

    
    @commands.Cog.listener()
    async def on_connect(self):

         print("Connected.")

         await self.bot.register_commands()

         if self.bot.user.id == 823941047473274960:
             await self.bot.change_presence(activity=discord.Streaming(name="Oknos Technology", url="https://www.twitch.tv/oknosofficial"))
         
         elif self.bot.user.id == 912846359789461525:
             await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="Oknos Testing"))


         loaded = False

         if not loaded:
             global started
             started = time.time()
             loaded = True


def setup(bot):
    bot.add_cog(OnConnect(bot))