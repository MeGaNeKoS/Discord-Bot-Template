""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.1
"""

import nextcord
from nextcord.ext import commands

from utils import helpers


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, message: commands.Context, error):
        if isinstance(error, commands.errors.CheckFailure):  # Permission error
            info_board = helpers.embed(
                title=error,
                colour=nextcord.Colour.red(),
                description=f"You doesnt have enough permission to use {message.command}")
        elif message.command_failed:  # Wrong command args/param
            info_board = helpers.embed(
                title=error,
                colour=nextcord.Colour.red(),
                description=message.command.description)
        else:  # Command not found
            info_board = helpers.embed(
                title=error,
                colour=nextcord.Colour.red())

        # To clean up our channel
        await message.send(embed=info_board, delete_after=60)
        await message.message.delete(delay=60)


def setup(bot):
    bot.add_cog(Errors(bot))
