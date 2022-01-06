import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import datetime
from config import EMOTES, COLORS
import math

class Whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def whois(self, ctx, member: Option(discord.Member, "Specify a user", required=False, default=None)):
        """Get information about a user."""

        load = EMOTES["loading"]
        Loading = discord.Embed(description=f"{load} Fetching user...", color=COLORS["info"])

        message = await ctx.respond(embed=Loading)

        u = ctx.author.user.id if member == None else member.id
        user = discord.Guild.get_member(u)

        if user == None:
            user = await self.bot.fetch_user(u)
            noMember = True

        created  = user.created_at.strftime("%x\n%X %Z")
        secondsc = math.floor(datetime.datetime.utcnow() - user.created_at)

        m, s = divmod(secondsc, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)

        days, hours, minutes, seconds = None, None, None, None

        if d:
            days = f"{d} Day(s)"
        if h:
            hours = f"{h} Hour(s)"
        if m:
            minutes = f"{m} Minute(s)"
        if s:
            seconds = f"{s} Seconds"

        createda = f"{days or ''} {hours or ''} {minutes or ''} {seconds or ''} ago".strip()


        roles = [role.mention for role in user.roles[1:]]
        
        if not noMember:
         joined = user.joined_at.strftime("%x\n%X %Z")

         secondsj = math.floor(datetime.datetime.utcnow() - user.joined_at)

         m, s = divmod(secondsj, 60)
         h, m = divmod(m, 60)
         d, h = divmod(h, 24)

         days, hours, minutes, seconds = None, None, None, None

         if d:
            days = f"{d} Day(s)"
         if h:
            hours = f"{h} Hour(s)"
         if m:
            minutes = f"{m} Minute(s)"
         if s:
            seconds = f"{s} seconds"

         joineda = f"{days or ''} {hours or ''} {minutes or ''} {seconds or ''} ago".strip()

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
            Embed.add_field(name="Status", value=status)

        Embed.add_field(name="Account Created", value=f"{created}\n{createda}", inline=True)

        if not noMember:
            Embed.add_field(name="Account Joined", value=f"{joined}\n{joineda}")
            Embed.addfield(name=f"Roles [{roles.len()}]", value="".join(roles))

        Embed.set_footer(text=f"ID: {user.id}")

        message.edit(embed=Embed)

def setup(bot):
    bot.add_cog(Whois(bot))