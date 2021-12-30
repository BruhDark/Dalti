from discord.ext import commands
import discord
import os
from discord.ext.commands.bot import when_mentioned_or
from discord.commands import slash_command
from config import PREFIX, ACTIVITY, DESCRIPTION
import datetime, time

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

        global up
        up = time.time()

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

        ctime = time.time()
        diff = ctime - up
        uptime = str(datetime.timedelta(seconds=diff))

        pycordV = discord.__version__

        embed = discord.Embed(title=f"Dalti Stats",description=DESCRIPTION, timestamp=datetime.datetime.utcnow(), color=ctx.user.color)
        embed.add_field(name="Uptime", value=uptime, inline=True)
        embed.add_field(name="PyCord Version", value=f"`{pycordV}`", inline=True)
        embed.add_field(name="Bot", value=f"Username: {self.bot.user}\nID: {self.bot.user.id}\nCreated At: {self.bot.user.created_at}")


        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text="Made with ♥️ by Dark")

        await ctx.respond(embed=embed)


if __name__ == "__main__":
    main()
