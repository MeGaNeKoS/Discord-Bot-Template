""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""
from nextcord.ext import commands, tasks


class Auto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @tasks.loop()
    # async def spam(self):
    #     channel = self.bot.get_guild(0).get_channel(0)
    #     await channel.send("This is spam")


def setup(bot):
    bot.add_cog(Auto(bot))
