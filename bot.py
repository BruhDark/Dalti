from discord.ext import commands
import discord
import random
import os

Dalti = commands.Bot(command_prefix=commands.when_mentioned_or("d!"))

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
    await ctx.send("Pong!")
    

@Dalti.command()
async def say(ctx, *, args):
    """Return what you said as Dalti"""
    await ctx.send((args))

@Dalti.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite me!", description="You can get me [here](https://discord.com/api/oauth2/authorize?client_id=823941047473274960&permissions=260315671798&scope=bot%20applications.commands)")
    await ctx.reply(embed=embed, mention_author=False)

@Dalti.command()
async def test(ctx):
    us = open("users.txt", "r")
    for x in us:
        await ctx.send(x)

@Dalti.command()
async def pet(ctx, arg):
    l = ["They bit you.", "Such a good boi.", "Look how they wiggle their tail!"]
    s = random.choice(l)
    await ctx.reply(content=f"You have pet {(arg)}. {s}", allowed_mentions=discord.AllowedMentions(users=False), mention_author=False)


Dalti.run("ODIzOTQxMDQ3NDczMjc0OTYw.YFoI5Q.i4me8EAEvU-3xICe5yhyQ6KXZRE")