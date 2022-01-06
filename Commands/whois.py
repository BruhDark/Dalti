import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import datetime
import time
from config import EMOTES, COLORS
import math

class Whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def whois(self, ctx: commands.Context, member: Option(discord.Member, "Specify a user", required=False, default=None)):
        """Get information about a user."""

        load = EMOTES["loading"]
        Loading = discord.Embed(description=f"{load} Fetching user...", color=COLORS["info"])

        message = await ctx.respond(embed=Loading)

        u = ctx.author.user.id if member == None else member.id
        user = ctx.guild.get_member(u)

        if user == None:
            user = await self.bot.fetch_user(u)
            global noMember
            noMember = True

        created  = user.created_at.strftime("%x\n%X %Z")

        roles = [role.mention for role in user.roles[1:]]
        
        if not noMember:
         joined = user.joined_at.strftime("%x\n%X %Z")

        if not noMember:
         x = user.raw_status
         if x == "online":
             status = EMOTES["online"]

         elif x == "idle":
             status = EMOTES["idle"]

         elif x == "dnd":
             status = EMOTES["dnd"]

         elif x == "offline":
             status = EMOTES["offline"]

         else:
             status = "Unknown"

        color = user.color if not noMember else COLORS["dalti"]
        amember = "**This user is not a member of this server.**" if noMember else ""

        Embed = discord.Embed(color=color, timestamp=datetime.datetime.utcnow(), description=f"{user.mention}\n{amember}")

        Embed.set_author(name=f"{user.name}#{user.discriminator}", icon_url=user.avatar)
        Embed.set_thumbnail(url=user.avatar)

        if not noMember:
            Embed.add_field(name="Status", value=status, inline=True)

        Embed.add_field(name="Account Created", value=f"{created}\n{createda}", inline=True)

        if not noMember:
            Embed.add_field(name="Account Joined", value=f"{joined}\n{joineda}", inline=True)
            Embed.addfield(name=f"Roles [{roles.len()}]", value="".join(roles), inline=True)

        Embed.set_footer(text=f"ID: {user.id}")

        message.edit(embed=Embed)

def setup(bot):
    bot.add_cog(Whois(bot))