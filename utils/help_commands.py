""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""

import nextcord
from nextcord.ext import commands

from utils import helpers


class CustomHelpCommand(commands.DefaultHelpCommand):
    """
    Custom help command for our bot. we use Default help command if we didnt overwrite anything
    """

    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        # Request: Add pagination here
        fields = []
        for cog, commands_list in mapping.items():
            if not cog or not commands_list:
                continue
            fields.append({"name": cog.qualified_name,
                           "value": cog.description or "No description added",
                           "inline": False,
                           "blank_before": True})
            for command in commands_list:
                if await command.can_run(self.context):
                    fields.append({"name": command,
                                   "value": command.help or "No description added",
                                   "inline": True})

        info_board = helpers.embed(
            title=f"{self.context.bot.user.display_name}",
            colour=nextcord.Colour.blurple(),
            footer=self.context.bot.user.display_name,
            fields=fields
        )
        await self.context.send(embed=info_board)

    async def send_cog_help(self, cog):
        # Request: Create his own help i guess
        return await super(CustomHelpCommand, self).send_cog_help(cog)

    async def send_group_help(self, group):
        # Request: Create his own help i guess
        return await super().send_group_help(group)

    async def send_command_help(self, command):
        if not await command.can_run(self.context):
            raise commands.errors.CheckFailure(f"You doesnt have enough permission to access this command")

        fields = [{"name": "Usage",
                   "value": command.usage,
                   "inline": False}]

        info_board = helpers.embed(
            title=command.name,
            description=command.description,
            colour=nextcord.Colour.dark_red(),
            footer=self.context.bot.user.display_name,
            fields=fields
        )

        return await self.context.send(embed=info_board)
