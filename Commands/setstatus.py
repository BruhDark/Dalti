from discord.commands import slash_command
from discord.ext import commands
from discord.commands import Option
from discord.commands import permissions
import discord
from config import EMOTES, COLORS, ACTIVITY

eerror = EMOTES["error"]
esuccess = EMOTES["success"]
cerror = COLORS["error"]
csuccess = COLORS["success"]
online = EMOTES["green"]
idle = EMOTES["yellow"]
dnd = EMOTES["red"]

act = discord.Game(ACTIVITY)

class SetStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(default_permission=False)
    @permissions.permission(user_id=449245847767482379, permission=True)
    async def setstatus(self, ctx, status: Option(str, "Set status", choices=["online", "idle", "dnd"])):
        """Change Dalti's status"""
        try:
            if status == "online":
                await self.bot.change_presence(status=discord.Status.online, activity=act)
                Embed = discord.Embed(description=f"{esuccess} Sucessfully changed my status to {online} `Online`.", color=csuccess)
                await ctx.respond(embed=Embed)
            
            elif status == "idle":
                await self.bot.change_presence(status=discord.Status.idle, activity=act)
                Embed = discord.Embed(description=f"{esuccess} Sucessfully changed my status to {idle} `Idle`.", color=csuccess)
                await ctx.respond(embed=Embed)

            elif status == "dnd":
                await self.bot.change_presence(status=discord.Status.dnd, activity=act)
                Embed = discord.Embed(description=f"{esuccess} Sucessfully changed my status to {dnd} `DND`.", color=csuccess)
                await ctx.respond(embed=Embed)
        
        except Exception:
            Embed = discord.Embed(description=f"{eerror} I was not able to change my status/activity.", colour=cerror)
            await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(SetStatus(bot))