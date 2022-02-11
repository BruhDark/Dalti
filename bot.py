from discord.ext import commands
import discord
import os
import pymongo
import jishaku
from config import PREFIX

client = pymongo.MongoClient("mongodb+srv://Oknos:bkUPoiPc1nGcxe7y@cluster0.gee6w.mongodb.net/")
# os.environ["MONGO_URI"]
database = client["oknos"]

class ClassBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=PREFIX, help_command=None, intents=discord.Intents.all())
        self.database = database

        for event in os.listdir("Events"):
         if event.endswith(".py"):
             self.load_extension(f"Events.{event[:-3]}")
             print(f"Loaded event: {event}")
    
        for command in os.listdir("Commands"):
         if command.endswith(".py"):
             self.load_extension(f"Commands.{command[:-3]}")
             print(f"Loaded command: {command}")

        try:
         self.load_extension("jishaku")
         print("Loaded extension: jishaku")
    
        except Exception as e:
         print("Could not load jishaku: {e}")


Bot = ClassBot()
Bot.run("OTEyODQ2MzU5Nzg5NDYxNTI1.YZ14bA.h6weR92IJltKwDGw3fgCh6tMOx8")
    # os.environ["DISCORD_TOKEN"]
