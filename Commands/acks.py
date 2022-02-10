import discord
from discord.ext import commands
from discord.commands import slash_command
from config import EMOTES,  VERSIONS
import pymongo

class view(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown1())

class Dropdown1(discord.ui.Select):
    def __init__(self):

        Options = [
            discord.SelectOption(
                label="Add Acknowledgement", description="Add an acknowledgement to the user", emoji=EMOTES["add"]
            ),
            discord.SelectOption(
                label="Remove Acknowledgement", description="Remove an acknowledgement from the user", emoji=EMOTES["remove"]
            ),
            discord.SelectOption(
                label="Edit Acknowledgement", description="Edit/replace the user acknowledgements", emoji=EMOTES["edit"]
            )
        ]
    
        super().__init__(
            placeholder="Select an option",
            min_values=1,
            max_values=1,
            options=Options,
            disabled = False
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(f"Option selected: {self.values}")
        self.disabled = True
        newView = discord.ui.View()
        newView.add_item(self)
        await interaction.message.edit(view=newView)


    async def on_timeout(self, interaction: discord.Interaction):
        if not self.disabled:
         self.disabled = True
         newView = discord.ui.View()
         newView.add_item(self)
         await interaction.message.edit(view=newView)

class AcksCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.database = self.bot.database

    @commands.command()
    async def acks(self, ctx):

        view = discord.ui.View()
        view.add_item(Dropdown1())

        await ctx.send("Make a selection", view=view)

    @commands.command()
    async def db(self, ctx, *, args: str):
        await ctx.send("Trying to add something on the db...")

        try:
            collection = self.database["stats"]
            test = {"username": ctx.author.name, "arguments": args}
            x =  collection.insert_one(test)

            await ctx.send(f"Created. Object ID: {x.inserted_id}")

        except Exception or discord.DiscordException as e:
            await ctx.send(f"An error ocurred: {e}")



def setup(bot):
    bot.add_cog(AcksCommand(bot))