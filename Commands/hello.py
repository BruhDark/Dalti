from discord.commands import user_command
from discord.ext import commands
import discord

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @user_command(name="Say hello", guild_ids=[688912903385907223])
    async def hello(self, ctx, member: discord.Member):
        await ctx.respond("{ctx.author.mention} says hello to {member.mention}")

def setup(bot):
    bot.add_cog(Hello(bot))
