""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""
import nextcord
from nextcord.ext import commands

from utils import helpers


class Info(commands.Cog, description="Information about this bot"):

    COG_EMOJI = "🔍"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Show bot information", description="Get information about bot")
    async def info(self, ctx):
        """
        Get information about the bot
        :param ctx:
        :return:
        """
        fields = [{"name": "Help Commands",
                   "value": f"Type {self.bot.command_prefix}help for commands list.",
                   "inline": True,
                   "blank_before": False}]

        info_board = helpers.embed(title=self.bot.user.display_name,
                                   colour=nextcord.Colour.dark_blue(),
                                   footer=self.bot.user.display_name,
                                   fields=fields)

        await ctx.send(embed=info_board)


def setup(bot):
    bot.add_cog(Info(bot))
