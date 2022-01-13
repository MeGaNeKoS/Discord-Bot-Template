""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""
import os

import nextcord
from nextcord.ext import commands


class Info(commands.Cog, description="Information about this bot"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Show bot information", description="Get information about bot")
    async def info(self, ctx):
        """
        Get information about the bot
        :param ctx:
        :return:
        """
        info_board = nextcord.Embed(
            title=f"{self.bot.user.display_name}",
            description=os.getenv("BOT_DESC") or "This bot made with MeGaNeKo bot template.",
            colour=nextcord.Colour.dark_blue(),
            url=nextcord.Embed.Empty if os.getenv("BOT_DESC") else
            "https://github.com/MeGaNeKoS/Discord-Bot-Template"
        )
        info_board.set_footer(text=f"{self.bot.user.display_name}")
        if os.getenv("BOT_AUTHOR"):
            if url := os.getenv("BOT_AUTHOR_URL"):
                pass
            else:
                url = nextcord.Embed.Empty
        else:
            url = "https://github.com/MeGaNeKoS/Discord-Bot-Template"
        info_board.set_author(name=os.getenv("BOT_AUTHOR") or "MeGaNeKoS",
                              url=url)
        info_board.add_field(
            name="\u200B",
            value="\u200B",
            inline=False)
        info_board.add_field(name="Commands", value=f"Type {self.bot.command_prefix}help for commands list.",
                             inline=True)


def setup(bot):
    bot.add_cog(Info(bot))
