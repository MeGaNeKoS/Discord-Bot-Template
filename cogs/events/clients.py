""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""
from nextcord.ext import commands, tasks


class Client(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        The code in this even is executed when the bot is ready
        """
        for cog in self.bot.cogs:
            for func in dir((cog_class := self.bot.get_cog(cog))):
                if callable(task := getattr(cog_class, func)) and isinstance(task, tasks.Loop):
                    task.start()
        print("Bot is ready!")


def setup(bot):
    bot.add_cog(Client(bot))
