from discord.commands import slash_command
from discord.ext import commands
from discord.commands import Option
from discord.commands import permissions
import discord

class SetStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(default_permission=False, guild_ids=[688912903385907223])
    @permissions.permission(user_id=449245847767482379, permission=True)
    async def setstatus(self, ctx, status: Option(str, "Set status", choices=["online", "idle", "dnd"])):
        """Change Dalti's status"""
        try:
            if status == "online":
                await self.bot.change_presence(status=discord.Status.online)
                Embed = discord.Embed(description=f"<:daltiSuccess:923699355779731476> Sucessfully changed my status to <:daltiOnline:923700141754552353> `Online`.", color=discord.Color.from_rgb(67,181,130))
                await ctx.respond(embed=Embed)
            
            elif status == "idle":
                await self.bot.change_presence(status=discord.Status.idle)
                Embed = discord.Embed(description=f"<:daltiSuccess:923699355779731476> Sucessfully changed my status to <:daltiIdle:923700173438349383> `Idle`.", color=discord.Color.from_rgb(67,181,130))
                await ctx.respond(embed=Embed)

            elif status == "dnd":
                await self.bot.change_presence(status=discord.Status.dnd)
                Embed = discord.Embed(description=f"<:daltiSuccess:923699355779731476> Sucessfully changed my status to <:daltiDND:923700213389086840> `DND`.", color=discord.Color.from_rgb(67,181,130))
                await ctx.respond(embed=Embed)
        
        except Exception:
            Embed = discord.Embed(description="<:daltiError:923699414646816768> I was not able to change my status/activity.", colour=discord.Colour.from_rgb(240,74,71))
            await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(SetStatus(bot))