from discord.ext import commands
from discord.commands import Option, slash_command
import discord
from config import COLORS, EMOTES
import datetime

class Spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def spotify(self, ctx: commands.Context, member: Option(discord.Member, "Select a user", required=False, default=None)):
        """Get Spotify stats of someone or yourself"""

        await ctx.defer()

        if member == None:
            id = ctx.author.id
        elif type(member) == int:
            id = member
        else:
            id = member.id

        user = ctx.guild.get_member(id)

        if user != None:
    
            if type(user.activity) == discord.Spotify:

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
                    status = EMOTES["question"]

                if user.avatar == None:
                    avatar = user.default_avatar
                else:
                    avatar = user.avatar

                Embed = discord.Embed(description=f"{user.mention} | {status}", timestamp=datetime.datetime.utcnow(), color=user.color)
                Embed.set_author(name=f"{user.name}#{user.discriminator}", icon_url=avatar)

                Embed.set_thumbnail(url=user.activity.album_cover_url)

                artists = user.activity.artists

                Embed.add_field(name="Song", value=user.activity.title, inline=True)
                Embed.add_field(name="Duration", value=user.activity.duration)
                Embed.add_field(name="Artist", value=", ".join(artists))
                Embed.add_field(name="Album", value=user.activity.album)

                Embed.set_footer(text=f"ID: {member.id}", icon_url="https://emoji.gg/assets/emoji/7370_Spotify.png")

                emoji = EMOTES["spotify"]

                View = discord.ui.View()
                view.add_item(discord.ui.Button(emoji=emoji,label='Listen on Spotify', url=user.activity.track_url, style=discord.ButtonStyle.url))

                ctx.respond(embed=Embed, view=View)

            else:
                error = EMOTES["error"]
                Embed = discord.Embed(description=f"{error} This user is not listening to Spotify", color=COLORS["error"])

        else:
            error = EMOTES["error"]
            Embed = discord.Embed(description=f"{error} Couldn't find this member", color=COLORS["error"])
            ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Spotify(bot))
