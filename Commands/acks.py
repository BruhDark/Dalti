import discord
from discord.ext import commands
from discord.commands import slash_command
from config import EMOTES,  VERSIONS

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
            placeholder="What to do?",
            min_values=1,
            max_values=1,
            options=Options,
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(f"Option selected: {self.values[0]}")

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        
        self.add_item(Dropdown1())


class AcksCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def acks(self, ctx):

        view = DropdownView()

        await ctx.send("Make a selection", view=view)

def setup(bot):
    bot.add_cog(AcksCommand(bot))