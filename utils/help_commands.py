""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""

from typing import Optional, List

import nextcord
from nextcord import Embed
from nextcord.ext import commands

from utils import helpers

"""
Thanks to DenverCoder1 to create this tutorial.
You could check his repo here:  https://github.com/DenverCoder1/Tutorial-Discord-Bot
"""


class HelpDropdown(nextcord.ui.Select):
    def __init__(self, help_command: "MyHelpCommand", options: list[nextcord.SelectOption]):
        super().__init__(placeholder="Choose a category...", min_values=1, max_values=1, options=options)
        self._help_command = help_command

    async def callback(self, interaction: nextcord.Interaction):
        embed = (
            await self._help_command.cog_help_embed(self._help_command.context.bot.get_cog(self.values[0]))
            if self.values[0] != self.options[0].value
            else await self._help_command.bot_help_embed(self._help_command.get_bot_mapping())
        )
        await interaction.response.edit_message(embed=embed)


class HelpView(nextcord.ui.View):
    def __init__(self, help_command: "MyHelpCommand", options: list[nextcord.SelectOption], *,
                 timeout: Optional[float] = 120.0):
        super().__init__(timeout=timeout)
        self.add_item(HelpDropdown(help_command, options))
        self._help_command = help_command

    async def on_timeout(self):
        # remove dropdown from message on timeout
        self.clear_items()
        await self._help_command.response.edit(view=self)

    async def interaction_check(self, interaction: nextcord.Interaction) -> bool:
        return self._help_command.context.author == interaction.user


class MyHelpCommand(commands.DefaultHelpCommand):
    def __init__(self, **options):
        super().__init__(**options)
        self.response = None

    def get_command_signature(self, command):
        return f"{self.context.clean_prefix}{command.qualified_name} {command.signature}"

    async def _cog_select_options(self) -> list[nextcord.SelectOption]:
        options: list[nextcord.SelectOption] = [nextcord.SelectOption(
            label="Home",
            emoji="🏠",
            description="Go back to the main menu.",
        )]

        for cog, command_set in self.get_bot_mapping().items():
            filtered = await self.filter_commands(command_set, sort=True)
            if not filtered:
                continue
            emoji = getattr(cog, "COG_EMOJI", "⁉")
            options.append(nextcord.SelectOption(
                label=cog.qualified_name if cog else "No Category",
                emoji=emoji,
                description=cog.description if cog and cog.description else None
            ))

        return options

    async def _help_embed(
            self, title=None, description: Optional[str] = Embed.Empty, mapping: Optional[dict] = None,
            command_set: Optional[List[commands.Command]] = None, set_author: bool = True
    ) -> Embed:
        fields = [{"name": "\u200B", "value": "\u200B", "inline": False}]
        if title is None:
            title = self.context.bot.user.display_name
        if command_set:
            # show help about all commands in the set
            filtered = await self.filter_commands(command_set, sort=True)
            for command in filtered:
                fields.append({"name": self.get_command_signature(command),
                               "value": command.short_doc or "...",
                               "inline": False,
                               "blank_before": False})
        elif mapping:
            # add a short description of commands in each cog
            for cog, commands_list in mapping.items():
                if not cog or not commands_list:
                    continue
                fields.append({"name": cog.qualified_name,
                               "value": cog.description or "No description added",
                               "inline": False,
                               "blank_before": False})

                # for command in commands_list:
                #     fields.append({"name": command,
                #                    "value": command.help or "No description added",
                #                    "inline": True})

        info_board = helpers.embed(
            title=title,
            colour=nextcord.Colour.blurple(),
            description=description,
            footer=self.context.bot.user.display_name,
            set_author=set_author,
            fields=fields
        )
        return info_board

    async def bot_help_embed(self, mapping: dict) -> Embed:
        return await self._help_embed(
            title="Bot Commands",
            description=self.context.bot.description,
            mapping=mapping,
            set_author=True,
        )

    async def send_bot_help(self, mapping: dict):
        embed = await self.bot_help_embed(mapping)
        options = await self._cog_select_options()
        self.response = await self.get_destination().send(embed=embed, view=HelpView(self, options))

    async def send_command_help(self, command: commands.Command):
        # Only user with permission can see the help of the command
        await command.can_run(self.context)
        emoji = getattr(command.cog, "COG_EMOJI", "⁉")
        embed = await self._help_embed(
            title=f"{emoji} {command.qualified_name}" if emoji else command.qualified_name,
            description=command.description,
            command_set=command.commands if isinstance(command, commands.Group) else None
        )
        await self.get_destination().send(embed=embed)

    async def cog_help_embed(self, cog: Optional[commands.Cog]) -> Embed:
        if cog is None:
            return await self._help_embed(
                title=f"No category",
                command_set=self.get_bot_mapping()[None]
            )
        emoji = getattr(cog, "COG_EMOJI", "⁉")
        return await self._help_embed(
            title=f"{emoji} {cog.qualified_name}" if emoji else cog.qualified_name,
            description=cog.description,
            command_set=cog.get_commands()
        )

    async def send_cog_help(self, cog: commands.Cog):
        embed = await self.cog_help_embed(cog)
        await self.get_destination().send(embed=embed)

    # Use the same function as command help for group help
    send_group_help = send_command_help
