import discord
from discord.commands import slash_command, user_command
from discord.ext import commands
from discord.commands import SlashCommandGroup

class cog_name(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    test = SlashCommandGroup("test", "test related commands!", guild_ids=[688912903385907223])

    @test.command( name='test_hi_group', description='test')
    async def test_hi(self,ctx):
        name = ctx.author.name
        await ctx.respond(f"Hello {name}!")
        
    @slash_command(guild_ids=[688912903385907223], name='test_hi', description='test')
    async def test_hi_2(self,ctx):
        name = ctx.author.name
        await ctx.respond(f"Hello {name}!")

    @user_command(name="Say Hello",guild_ids=[688912903385907223])
    async def hi(self,ctx, user):
        await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

def setup(bot):
    bot.add_cog(cog_name(bot))
