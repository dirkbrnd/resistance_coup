from typing import List

from rich.table import Table
from rich.text import Text

from src.models.players.human import BasePlayer


def generate_table(players: List[BasePlayer], current_player_index: int) -> Table:
    """Regenerate table"""

    table = Table("Players", "Coins", "Cards")
    for ind, player in enumerate(players):
        if player.is_ai:
            player_text = Text.from_markup(f":robot: {str(player)}")
        else:
            player_text = Text.from_markup(f":grimacing: {str(player)}")

        if ind == current_player_index:
            player_text.stylize("bold magenta")

        coin_text = Text(str(player.coins), style="gray")

        card_text = Text()
        if player.is_active:
            for card in player.cards:
                if player.is_ai:
                    card_text.append("<Secret...> ")
                else:
                    card_text.append(
                        str(card), style=f"{card.foreground_color} on {card.background_color}"
                    )
                    card_text.append(" ")
        else:
            card_text = Text.from_markup(":skull:")

        table.add_row(player_text, coin_text, card_text)

    return table
