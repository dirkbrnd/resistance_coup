import random
from typing import List

from rich.highlighter import Highlighter
from rich.table import Table
from rich.text import Text
from rich import print

from src.models.player import Player

class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(f"color({random.randint(16, 255)})", index, index + 1)


def generate_table(players: List[Player], current_player_index: int) -> Table:
    """Regenerate table"""

    table = Table("Players", "Coins", "Cards")
    for ind, player in enumerate(players):
        player_text = Text()
        if ind == current_player_index:
            player_text.append(str(player), style="bold magenta")
        else:
            player_text.append(str(player))

        coin_text = Text(str(player.coins), style="gray")

        card_text = Text()
        for card in player.cards:
            card_text.append(str(card) + " ")

        table.add_row(player_text, coin_text, card_text)

    return table