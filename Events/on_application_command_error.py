import discord
from discord.ext import commands
from config import EMOTES, COLORS
import datetime
import traceback

class OnApplicationCmdError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            
            x = EMOTES["error"]
            Embed = discord.Embed(description=f"{x} This command is on cooldown", color=COLORS["error"])
            await ctx.respond(embed=Embed)
        
        else:
            x = EMOTES["error"]
            Embed = discord.Embed(description=f"{x} Something went wrong\n\n```py\n{error}```", color=COLORS["error"])
            await ctx.respond(embed=Embed)

            channel = self.bot.get_channel(937864270434140200)
            
            tc = traceback.format_exc()

            Embed = discord.Embed(description=f"{x} A command has errored.\n\nError:\n```py\n{error}```\n\nTraceback:\n```py\n{tc}```", timestamp=datetime.datetime.utcnow(), color=COLORS["error"])
            Embed.add_field(name="Guild ID", value=ctx.guild.id, inline=True)
            Embed.add_field(name="Guild Name", value=ctx.guild.name, inline=True)
            Embed.add_field(name="Channel", value=f"{ctx.channel.mention} - {ctx.channel.name} ({ctx.channel.id})")

            Embed.add_field(name="Ran By", value=f"{ctx.author} ({ctx.author.id})")

            Embed.set_thumbnail(url=self.bot.user.avatar.url)
            await channel.send(embed=Embed)


def setup(bot):
    bot.add_cog(OnApplicationCmdError(bot))