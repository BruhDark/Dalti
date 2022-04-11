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

            thread = await message.create_thread(name="Suggestion Discussion", auto_archive_duration=None)
            msg = await thread.send(f":smile: Use this thread to discuss about the above suggestion.\nFeel free to propose changes, imrpovenets or ways to apply it to the bot on an afficent way.\n\n:wave: Have a good day.")
            await msg.pin()


def setup(bot):
    bot.add_cog(Message(bot))
