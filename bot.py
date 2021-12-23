import discord
import random
import os
from discord.commands import Option
from discord.commands import permissions
import requests

Dalti = discord.Bot()

game = "with toys"
act = discord.Game(game)

@Dalti.event
async def on_ready():
    print(f"Logged in as {Dalti.user} - ID: {Dalti.user.id}")
    print("-----------")
    try:
     await Dalti.change_presence(status=discord.Status.online, activity=act)
     print("Successfully set bot presence.")
    except discord.InvalidArgument:
     print("Could not set presence.")

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
    l = ["They bit you.", "Such a good boi.", "Look how they wiggle their tail!"]
    s = random.choice(l)
    await ctx.respond(content=f"{ctx.author.mention} has pet {user.mention}! {s}")

@Dalti.command(default_permission=False)
@permissions.permission(user_id=449245847767482379, permission=True)
async def setstatus(ctx, status: Option(str, "Set status", choices=["online", "idle", "dnd"]), activity: str = game):
    """Change Dalti's status"""
    try:
        if status == "online":
            await Dalti.change_presence(status=discord.Status.online, activity=act)
            Embed = discord.Embed(description=f"<:daltiSuccess:923699355779731476> Sucessfully changed my status to <:daltiOnline:923700141754552353> `Online` and my activity to `{activity}`.", color=discord.Colour.from_rbg(67,181,130))
            await ctx.respond(embed=Embed)
        
        elif status == "idle":
            await Dalti.change_presence(status=discord.Status.idle, activity=act)
            Embed = discord.Embed(description=f"<:daltiSuccess:923699355779731476> Sucessfully changed my status to <:daltiIdle:923700173438349383> `Idle` and my activity to `{activity}`.`", color=discord.Colour.from_rbg(67,181,130))
            await ctx.respond(embed=Embed)

        elif status == "dnd":
            await Dalti.change_presence(status=discord.Status.dnd, activity=act)
            Embed = discord.Embed(description=f"<:daltiSuccess:923699355779731476> Sucessfully changed my status to <:daltiDND:923700213389086840> `DND` and my activity to `{activity}`.", color=discord.Colour.from_rbg(67,181,130))
            await ctx.respond(embed=Embed)
    
    except Exception:
        Embed = discord.Embed(description="<:daltiError:923699414646816768> I was not able to change my status/activity.", colour=discord.Colour.from_rbg(240,74,71))
        await ctx.respond("Could not change my status.")

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