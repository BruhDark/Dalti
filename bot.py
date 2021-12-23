import discord
import random
import os
from discord.commands import Option
from discord.commands import permissions
import requests

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
    await ctx.respond(f"Pong! `{Dalti.latency}`")

@Dalti.command()
async def say(ctx, arguments: str):
    """Return what you said as Dalti"""
    await ctx.send(arguments)
    await ctx.respond("Sent message.", ephemeral=True)

@Dalti.command()
async def invite(ctx):
    """Invite Dalti to your server"""
    embed = discord.Embed(title="Invite me!", description="You can get me [here](https://discord.com/api/oauth2/authorize?client_id=823941047473274960&permissions=260315671798&scope=bot%20applications.commands)")
    await ctx.respond(embed=embed)


@Dalti.command()
async def pet(ctx, user: discord.Member):
    """Pet a user!"""
    l = ["They bit you.", "Such a good boi.", "Look how they wiggle their tail!"]
    s = random.choice(l)
    await ctx.respond(content=f"{ctx.author.mention} has pet {user.mention}! {s}")

@Dalti.command(default_permission=False)
@permissions.permission(user_id=449245847767482379, permission=True)
async def setstatus(ctx, status: Option(str, "Set status", choices=["online", "idle", "dnd"])):
    """Change Dalti's status"""
    try:
        if status == "online":
            await Dalti.change_presence(status=discord.Status.online, activity=act)
            await ctx.respond(f"Sucessfully changed my status to {status}")
        
        elif status == "idle":
            await Dalti.change_presence(status=discord.Status.idle, activity=act)
            await ctx.respond(f"Sucessfully changed my status to {status}")

        elif status == "dnd":
            await Dalti.change_presence(status=discord.Status.dnd, activity=act)
            await ctx.respond(f"Sucessfully changed my status to {status}")
    
    except discord.InvalidArgument:
        await ctx.respond("Could not change my status.")

@Dalti.command()
async def apod(ctx):
    """Retreive today's APOD from Nasa"""
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=2JvlKQHQlB1RffyXdtxcpb64HlBE6QzEp0yC0CSq").json()

    Embed = discord.Embed(title=response["title"], 
    description=response["explanation"],
    image=response["hdurl"], 
    color="#0b3d91",
    footer="© {} - {}".format(response["copyright"], response["date"]))

    await ctx.respond(embed=Embed)

Dalti.run(os.environ["DISCORD_TOKEN"])
