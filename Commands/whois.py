import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import datetime
import time
from config import EMOTES, COLORS, BADGES
import math

class Whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def whois(self, ctx: commands.Context, member: Option(discord.Member, "Specify a user", required=False, default=None)):
        """Get information about a user."""

        await ctx.defer()

        if member == None:
            id = ctx.author.id
        elif type(member) == int:
            id = member
        else:
            id = member.id

        user = ctx.guild.get_member(id)
        noMember = False

        if user == None:
            user = await self.bot.fetch_user(id)
            noMember = True

        created  = user.created_at.strftime("%x\n%X %Z")

        if not noMember:
         roles = [role.mention for role in user.roles[1:]]
         roles.reverse()
        
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

        Embed.add_field(name="Account Created", value=f"{created}", inline=True)

        if not noMember:
            Embed.add_field(name="Account Joined", value=f"{joined}", inline=True)
            Embed.add_field(name="Highest Role", value=user.top_role.mention)
            Embed.add_field(name=f"Roles [{len(roles)}]", value=", ".join(roles), inline=True)

        flags = []
        
        if user.public_flags.staff:
            staff = BADGES["staff"]
            flags.append(f"{staff} Discord Staff")

        if user.public_flags.partner:
            partner = BADGES["partner"]
            flags.append(f"{partner} Partnered Server Owner")

        if user.public_flags.discord_certified_moderator:
            moderator = BADGES["moderator"]
            flags.append(f"{moderator} Discord Certified Moderator")

        if user.public_flags.verified_bot_developer or user.public_flags.early_verified_bot_developer:
            botdev = BADGES["botdev"]
            flags.append(f"{botdev} Verified Bot Developer")

        if user.public_flags.bug_hunter:
            bughunter = BADGES["bughunter"]
            flags.append(f"{bughunter} Bug Hunter")

        if user.public_flags.bug_hunter_level_2:
            bughunter2 = BADGES["bughunter2"]
            flags.append(f"{bughunter2} Bug Hunter")

        if user.public_flags.early_supporter:
            early = BADGES["early"]
            flags.append(f"{early} Early Supporter")
        
        if user.public_flags.hypesquad:
            events = BADGES["events"]
            flags.append(f"{events} Hypesquad Events")

        if user.public_flags.hypesquad_bravery:
            bravery = BADGES["bravery"]
            flags.append(f"{bravery} Hypequad Bravery")

        if user.public_flags.hypesquad_brilliance:
            brilliance = BADGES["brilliance"]
            flags.append(f"{brilliance} Hypequad Brilliance")

        if user.public_flags.hypesquad_balance:
            balance = BADGES["balance"]
            flags.append(f"{balance} Hypequad Balance")

        if user.bot:
            bot = BADGES["bot"]
            flags.append(f"{bot} Bot")

        if user.public_flags.verified_bot:
            verifiedbot = BADGES["verifiedbot"]
        
            flags.append(f"{verifiedbot} Verified Bot")


        Embed.add_field(name="Profile Badges", value="\n".join(flags))

        Embed.set_footer(text=f"ID: {user.id}")

        message = await ctx.interaction.original_message()
        await message.edit(embed=Embed)

def setup(bot):
    bot.add_cog(Whois(bot))