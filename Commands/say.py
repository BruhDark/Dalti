from discord.commands import slash_command
from discord.ext import commands
from discord.commands import permissions

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(default_permissions=False)
    @permissions.permission(user_id=449245847767482379, permission=True)
    async def say(self, ctx, arguments: str):
        """Return what you said as Dalti"""
        await ctx.send(arguments)
        await ctx.respond("Sent message.", ephemeral=True)

def setup(bot):
    bot.add_cog(Say(bot))