from discord.commands import slash_command
from discord.ext import commands
import requests
import discord
import datetime

class Pat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def pat(self, ctx: commands.Context, user: discord.Member):
        """Pat a user"""
        
        request = requests.get("https://some-random-api.ml/animu/pat").json()
        image = request["link"]

        Embed = discord.Embed(
            description=f"{ctx.author.mention} pats {user.mention}. uwu",
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color(user.accent_color)
        )

        Embed.set_author(name=f"{user.name}", icon_url=f"{user.avatar.url}")
        Embed.set_image(url=f"{image}")

        Embed.set_footer(text=f"By {ctx.user}")
        
        await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Pat(bot))