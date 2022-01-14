# Nextcord Bot Template

This repository is a template that everyone can use for the start of their discord bot.

This template created for fast set up your new discord bot and easy to scaling. It has common feature in standard
discord bot like embedded help menu.<br>

**This also compatible with any discord.py fork.**

# Setup

Firsts of all you need to have the python3 (created with 3.9). Then run `pip install -r requirements.txt`

## .env

Here is an explanation for .env:

| Variable                  | What it is                                                            |
| ------------------------- | ----------------------------------------------------------------------|
| BOT_AUTHOR                | The bot author                                                        |
| BOT_AUTHOR_URL            | The bot author embed link. Can be empty                               |
| BOT_DESC                  | The bot description                                                   |
| BOT_INTENT                | The bot intents. either all or default. Default value is default      |
| BOT_PREFIX                | The prefix you want to use for normal commands. Default value is "?"  |
| BOT_TOKEN                 | The token of your bot                                                 |

# Future Feature

1. Pagination for help command.
2. Slash command. (waiting for nextcord support slash command).
3. Add some example for client event.

# Other Help

- [Cogs](./cogs/README.md)
- [data](./data/README.md)
- [exceptions](./exceptions/README.md)
- [utils](./utils/README.md)

# Contributing The Project

This template not finish yet. There's some feature that I like to add like pagination on help menu, You can always pull
request to this repo, if you report or fix a bug or if you add more commands to the template I'll be happy implement
them.

# License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
