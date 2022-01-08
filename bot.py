from discord.ext import commands
import discord
import os
from config import PREFIX

def main():
    
    intents = discord.Intents.all()
    Bot = commands.Bot(command_prefix=PREFIX, 
    intents=intents)

    for event in os.listdir("Events"):
        if event.endswith(".py") and not event.endswith("_"):
            Bot.load_extension(f"Events.{event[:-3]}")
            print(f"Loaded event: {event}")
    
    for command in os.listdir("Commands"):
        if command.endswith(".py") and not command.endswith("_"):
          Bot.load_extension(f"Commands.{command[:-3]}")
          print(f"Loaded command: {command}")

    Bot.run(os.environ["DISCORD_TOKEN"])
    # os.environ["DISCORD_TOKEN"]

if __name__ == "__main__":
    main()
