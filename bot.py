import discord
import random
import os
from discord.commands import option

Dalti = discord.Bot()

act = discord.Game("with toys")

@Dalti.event
async def on_ready():
    print(f"Logged in as {Dalti.user}")
    try:
     await Dalti.change_presence(status=discord.Status.idle, activity=act)
     print("Successfully set bot presence.")
    except discord.InvalidArgument:
     print("Could not set presence.")

@Dalti.command()
async def ping(ctx):
    """Pings bot"""
    await ctx.respond("Pong!")

@Dalti.command()
async def say(ctx, arguments: str):
    """Return what you said as Dalti"""
    await ctx.send(arguments)
    await ctx.respond("Sent message.", ephemeral=True)

@Dalti.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite me!", description="You can get me [here](https://discord.com/api/oauth2/authorize?client_id=823941047473274960&permissions=260315671798&scope=bot%20applications.commands)")
    await ctx.respond(embed=embed, mention_author=False)


@Dalti.command()
async def pet(ctx, user: discord.Member):
    l = ["They bit you.", "Such a good boi.", "Look how they wiggle their tail!"]
    s = random.choice(l)
    await ctx.respond(content=f"You have pet {user.mention}. {s}", mention_author=False)


Dalti.run(os.environ("DISCORD_TOKEN"))