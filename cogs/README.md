# Cogs Folder

[Cogs](https://nextcord.readthedocs.io/en/latest/ext/commands/cogs.html) are a way to organize a collection of commands, listener, and some state into one class.<br>

In this folder, we divide cogs into 3 categories.
- commands: A group of command. You can use following format `cogs/commands/<group_name>/command.py` or `cogs/commands/<group_name>/slash_command.py`.
- events: A group of event. Such as `on_ready`, `on_member_join`, etc. You can use following format `cogs/events/<scope>`.
  - Example of scope: guilds event(guilds.py), messages event(messages.py), clients event(clients.py)).
- task: Everything that you need to run in background. You can use the following format `cogs/tasks/<group>`.   

# Other Help

- [All help](../README.md)
- [data](../data/README.md)
- [exceptions](../exceptions/README.md)
- [utils](../utils/README.md)