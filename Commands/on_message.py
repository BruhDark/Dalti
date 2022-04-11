import re
import discord
from discord.ext import commands

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):

        if message.author == self.bot.user:
            return

        if message.channel.id == 963098061024940116:
            
            await message.add_reaction("✅")
            await message.add_reaction("❌")
            
            pattern = re.compile("\[(.+)\]")
            find = pattern.search(message.content)
            
            name = find.group()
            name = name.replace("[", "")
            name = name.replace("]", "")
            name = name.replace("**", "")

            thread = await message.create_thread(name=name, auto_archive_duration=None)
            msg = await thread.send(f":wave: Use this thread to discuss about the above suggestion.\nFeel free to propose changes, improvements or ways to apply it to the bot on an afficent way.\n\n:smile: Have a good day, and a fun discussion.")


def setup(bot):
    bot.add_cog(Message(bot))
