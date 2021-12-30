from discord.commands import slash_command
from discord.ext import commands
import random
import discord
import datetime

class Pet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def pet(self, ctx: commands.Context, user: discord.Member):
        """Pet a user!"""

        l = ["They bit you.", "Such a good boi.", "Look how they wiggle their tail!"]
        s = random.choice(l)

        Embed = discord.Embed(
            description=f"You have pet {user.mention}. {s}",
            timestamp=datetime.datetime.utcnow()
        )

        Embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
        
        if s == "They bit you.":
            image = "https://media2.giphy.com/media/JpSlrYUK0UZ9BOyCyh/giphy.gif"
        elif s == "Such a good boi.":
            image = "https://media0.giphy.com/media/Gx2vpQi2WPToc/giphy.gif"
        else:
            image = "https://media3.giphy.com/media/Nj0FfX9n53gf6/giphy.gif"

        Embed.set_image(url=f"{image}")
        Embed.set_footer(text="Pet Pet")
        
        await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Pet(bot))