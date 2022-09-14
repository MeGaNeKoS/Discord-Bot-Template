""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""

import nextcord
from nextcord.ext import commands, tasks

from utils import helpers


class Client(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        The code in this even is executed when the bot is ready
        """

        for cog in self.bot.cogs.values():
            # Force all background tasks to has to be in cogs.task folder and avoid unnecessary check on other module
            if not cog.__module__.startswith("cogs.task"):
                continue
            for func in dir(cog):
                if isinstance(task := getattr(cog, func), tasks.Loop):
                    task.start()

        print("Bot is ready!")

    @commands.Cog.listener()
    async def on_message(self, message):
        # Whenever the bot is tagged, respond with its prefix
        if message.author != self.bot.user and message.content == f"<@{self.bot.user.id}>":
            embed = helpers.embed(title="Prefix",
                                  description=f"My prefix is `{self.bot.command_prefix}`",
                                  colour=nextcord.Colour.random())
            await message.channel.send(embed=embed, delete_after=15)
            await message.delete(delay=15)


def setup(bot):
    bot.add_cog(Client(bot))
