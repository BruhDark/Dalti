from discord.commands import slash_command
from discord.ext import commands
from discord.commands import Option
import datetime
import discord
from config import EMOTES, COLORS, VERSIONS, AUTHORIZED

class Eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def eval(self, ctx, code: Option(str, "Type code to eval", required=True)):
        """Eval some code"""

        if ctx.author.id in AUTHORIZED:

            await ctx.defer()

            oknos = EMOTES[f"{self.bot.user.id}"]
            Embed = discord.Embed(description=f"{oknos} Succesfully excecuted code.", color=VERSIONS[f"{self.bot.user.id}"], timestamp=datetime.datetime.utcnow())

            Embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar)

            Embed.add_field(name=":inbox_tray: Input Code", value=f"```py\n{code}```")
            Embed.add_field(name=":outbox_tray: Output", value=f"```py\n{eval(code)}```")

            await ctx.respond(embed=Embed)

        else:

            error = EMOTES["error"]
            Embed = discord.Embed(description=f"{error} You are not authorized to run this command.", color=COLORS[f"{self.bot.user.id}"])
            await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Eval(bot))