""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""
import logging
import os
import sys

import nextcord
from dotenv import load_dotenv
from nextcord.ext import commands
from utils import sys_logger
load_dotenv()

logger = logging.getLogger(__name__)
# this has to be the highest level than the other loggers
# just leave it as it is
# adjusted the logging level on the file handler or stream handler
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.WARNING)  # default level is WARNING

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # default level is WARNING

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

sys.stderr = sys_logger.STDERRLogger()

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
bot = commands.Bot(command_prefix=bot_prefix, intents=intents)
"""
This will automatically load all commands located in cogs folder.
"""
cogs: list = [os.path.join(path, file)[2:-3].replace("/", ".").replace("\\", ".")
              for path, directories, files in os.walk('./cogs')
              for file in files
              if file.endswith('.py')]

for cog in cogs:
    try:
        logger.info(f"Loading cog {cog}")
        bot.load_extension(cog)
        logger.info(f"Loaded cog {cog}")
    except Exception as e:
        logger.warning(f"Failed to load cog {cog}\n{type(e).__name__}: {e}")

# Run the bot with the token
if __name__ == "__main__":
    bot.run(bot_token)
