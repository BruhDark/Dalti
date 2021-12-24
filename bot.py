import discord
import random
import os
from discord.commands import Option
from discord.commands import permissions
import requests
import datetime

Dalti = discord.Bot()

game = "with toys"
act = discord.Game(game)

@Dalti.event
async def on_connect():
    print("Connected to Discord. Not ready to receive commands.")
    print("-----------")
    try:
     await Dalti.change_presence(status=discord.Status.dnd, activity=discord.Game("Connecting..."))
     print("Connecting presence set.")
    
    except discord.InvalidArgument:
     print("Could not set connecting presence.")

@Dalti.event
async def on_ready():
    print(f"Logged in as {Dalti.user} - ID: {Dalti.user.id}")
    try:
     await Dalti.change_presence(status=discord.Status.online, activity=act)
     print("Successfully set bot presence.")
     print("----------")
    except discord.InvalidArgument:
     print("Could not set presence.")
     print("----------")

@Dalti.command()
async def ping(ctx):
    """Pings bot"""
    await ctx.respond(f"Pong! `{round(Dalti.latency * 1000)}ms`")

@Dalti.command(default_permission=False)
@permissions.permission(user_id=449245847767482379, permission=True)
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
    await ctx.defer()
    l = ["They bit you.", "Such a good boi.", "Look how they wiggle their tail!"]
    s = random.choice(l)

    Embed = discord.Embed(
        description=f"You have pet {user.mention}. {s}",
        timestamp=datetime.datetime.utcnow()
    )

    Embed.set_author(name=f"{ctx.author.user}", icon_url=f"{ctx.author.avatar_url}")
    
    if s == "They bit you.":
        image = "https://media2.giphy.com/media/JpSlrYUK0UZ9BOyCyh/giphy.gif"
    elif s == "Such a good boi.":
        image = "https://media0.giphy.com/media/Gx2vpQi2WPToc/giphy.gif"
    else:
        image = "https://media3.giphy.com/media/Nj0FfX9n53gf6/giphy.gif"

    Embed.set_image(url=f"{image}")
    Embed.set_footer(text="Pet Pet")
    await ctx.respond(embed=Embed)

@Dalti.command(default_permission=False)
@permissions.permission(user_id=449245847767482379, permission=True)
async def setstatus(ctx, status: Option(str, "Set status", choices=["online", "idle", "dnd"])):
    """Change Dalti's status"""
    try:
        if status == "online":
            await Dalti.change_presence(status=discord.Status.online)
            Embed = discord.Embed(description=f"<:daltiSuccess:923699355779731476> Sucessfully changed my status to <:daltiOnline:923700141754552353> `Online`.", color=discord.Color.from_rgb(67,181,130))
            await ctx.respond(embed=Embed)
        
        elif status == "idle":
            await Dalti.change_presence(status=discord.Status.idle)
            Embed = discord.Embed(description=f"<:daltiSuccess:923699355779731476> Sucessfully changed my status to <:daltiIdle:923700173438349383> `Idle`.", color=discord.Color.from_rgb(67,181,130))
            await ctx.respond(embed=Embed)

        elif status == "dnd":
            await Dalti.change_presence(status=discord.Status.dnd)
            Embed = discord.Embed(description=f"<:daltiSuccess:923699355779731476> Sucessfully changed my status to <:daltiDND:923700213389086840> `DND`.", color=discord.Color.from_rgb(67,181,130))
            await ctx.respond(embed=Embed)
    
    except Exception:
        Embed = discord.Embed(description="<:daltiError:923699414646816768> I was not able to change my status/activity.", colour=discord.Colour.from_rgb(240,74,71))
        await ctx.respond(embed=Embed)

@Dalti.command()
async def apod(ctx):
    """Retreive today's APOD from Nasa"""
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=2JvlKQHQlB1RffyXdtxcpb64HlBE6QzEp0yC0CSq").json()

    Embed = discord.Embed(title=response["title"],  
    color=discord.Color.from_rgb(102,106,242))

    Embed.set_image(url=response["hdurl"])
    Embed.set_footer(text="© {} - {}".format(response["copyright"], response["date"]), icon_url="https://media.discordapp.net/attachments/881968886248009821/923706098769358848/NASA_logo.png")

    await ctx.respond(embed=Embed)

Dalti.run(os.environ["DISCORD_TOKEN"])
