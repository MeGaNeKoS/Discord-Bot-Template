""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""
import os

import nextcord
from dotenv import load_dotenv
from nextcord.ext import commands

from utils.help_commands import CustomHelpCommand

load_dotenv()

if not (bot_token := os.getenv("BOT_TOKEN")):
    raise Exception("Required bot token")
bot_prefix = os.getenv("BOT_PREFIX") or "?"
"""	
Setup bot intents (events restrictions)
For more information about intents, please go to the following websites:
https://nextcord.readthedocs.io/en/latest/intents.html
https://nextcord.readthedocs.io/en/latest/intents.html#privileged-intents
Default Intents:
intents = all()
intents.members = False
intents.presences = False
"""

if os.getenv("BOT_INTENT").lower() == "all":
    intents = nextcord.Intents.all()
else:
    intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix=bot_prefix, help_command=CustomHelpCommand(), intents=intents)
"""
This will automatically load all commands located in cogs folder.
"""
cogs: list = [os.path.join(path, file)[2:-3].replace("/", ".").replace("\\", ".")
              for path, directories, files in os.walk('./cogs')
              for file in files
              if file.endswith('.py')]

for cog in cogs:
    try:
        print(f"Loading cog {cog}")
        bot.load_extension(cog)
        print(f"Loaded cog {cog}")
    except Exception as e:
        print(f"Failed to load cog {cog}\n{type(e).__name__}: {e}")

# Run the bot with the token
bot.run(bot_token)
