from discord.ext import commands
import discord
import os
from discord.ext.commands.bot import when_mentioned_or
from config import PREFIX

def main():
    intents = discord.Intents.default()
    Dalti = commands.Bot(command_prefix=when_mentioned_or(PREFIX), intents=intents)

    game = "with toys"
    act = discord.Game(game)

    @Dalti.event
    async def on_connect():
        print("Connected.")

        await Dalti.register_commands()

        try:
         await Dalti.change_presence(status=discord.Status.online, activity=act)
     
        except discord.InvalidArgument:
         pass

    @Dalti.event
    async def on_ready():
     print(f"Ready. Logged in as {Dalti.user} - ID: {Dalti.user.id}")
     print("---------")
    
    for command in os.listdir("Commands"):
        if command.endswith(".py") and not command.endswith("_"):
          Dalti.load_extension(f"Commands.{command[:-3]}")
          print(f"Loaded command: {command}")
    
    Dalti.run(os.environ["DISCORD_TOKEN"])

if __name__ == "__main__":
    main()
