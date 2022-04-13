import datetime
import os

from nextcord import Embed
from nextcord.embeds import EmbedType


# keyword only arguments
def embed(*,
          title=Embed.Empty,
          colour=Embed.Empty,
          description=Embed.Empty,
          footer=Embed.Empty,
          fields: list[dict] = None,
          timestamp: datetime.datetime = None,
          embed_type: EmbedType = 'rich'):
    if fields is None:
        fields = []

    board = Embed(
        title=title,
        description=description or os.getenv("BOT_DESC") or "This bot made with MeGaNeKo bot template.",
        colour=colour,
        timestamp=timestamp,
        type=embed_type,
    )

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
