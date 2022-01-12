""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""
import os

import nextcord
from nextcord.ext import commands


class CustomHelpCommand(commands.DefaultHelpCommand):
    """
    Custom help command for our bot. we use Default help command if we didnt overwrite anything
    """

    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        # Request: Add pagination here
        info_board = nextcord.Embed(
            title=f"{self.context.bot.user.display_name}",
            colour=nextcord.Colour.blurple()
        )
        info_board.set_footer(text=f"{self.context.bot.user.display_name}")
        info_board.set_author(name=os.getenv("BOT_AUTHOR") or "github.com/MeGaNeKoS/Discord-Bot-Template")

        for command, obj in self.context.bot.all_commands.items():
            info_board.add_field(
                name=f"{self.context.bot.command_prefix}{command}",
                value=obj.help or "No help description",
                inline=True)

        await self.context.send(embed=info_board)

    async def send_cog_help(self, cog):
        # Request: Create his own help i guess
        return await super(CustomHelpCommand, self).send_cog_help(cog)

    async def send_group_help(self, group):
        # Request: Create his own help i guess
        return await super().send_group_help(group)

    async def send_command_help(self, command):
        info_board = nextcord.Embed(
            title=f"{command.name}",
            description=command.description,
            colour=nextcord.Colour.dark_red()
        )
        info_board.set_footer(text=f"{self.context.bot.user.display_name}")
        info_board.set_author(name=os.getenv("BOT_AUTHOR") or "github.com/MeGaNeKoS/Discord-Bot-Template")

        return await self.context.send(embed=info_board)
