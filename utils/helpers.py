""""
MeGaNeKo 2022 - https://github.com/MeGaNeKoS/Discord-Bot-Template
Description:
This is a template to create your own discord bot in python.
Version: 1.0
"""

import datetime
import os
from typing import Literal

from nextcord import Embed

EmbedType = Literal['rich', 'image', 'video', 'gifv', 'article', 'link']


# keyword only arguments
def embed(*,
          title=Embed.Empty,
          colour=Embed.Empty,
          description=Embed.Empty,
          footer=Embed.Empty,
          fields: list[dict] = None,
          timestamp: datetime.datetime = None,
          set_author: bool = True,
          embed_type: EmbedType = 'rich'):
    if fields is None:
        fields = []

    board = Embed(
        title=title if title != Embed.Empty else Embed.Empty,
        description=(os.getenv("BOT_DESC") or (
            "[This bot made with MeGaNeKo bot template.](https://github.com/MeGaNeKoS/Discord-Bot-Template)"
        )) if description == Embed.Empty else description,
        colour=colour if colour != Embed.Empty else Embed.Empty,
        timestamp=timestamp,
        type=embed_type,
    )
    if set_author:
        # set bot author url info
        if url := os.getenv("BOT_AUTHOR_URL"):
            pass
        elif os.getenv("BOT_AUTHOR"):
            url = Embed.Empty
        else:
            url = "https://github.com/MeGaNeKoS/Discord-Bot-Template"

        board.set_author(name=os.getenv("BOT_AUTHOR") or "MeGaNeKoS Template Bot",
                         url=url)

    board.set_footer(text=footer)
    for field in fields:
        if field.get("blank_before", None):
            board.add_field(name="\u200B", value="\u200B", inline=False)
        board.add_field(name=field["name"], value=field['value'], inline=field["inline"])

    return board
