from enum import Enum
from typing import Dict, List

from pydantic import BaseModel


class CardType(str, Enum):
    contessa = "Contessa"
    duke = "Duke"
    assassin = "Assassin"
    captain = "Captain"
    ambassador = "Ambassador"


CARD_FOREGROUND_COLOR_MAP: Dict[CardType, str] = {
    CardType.contessa: "#6d191c",
    CardType.duke: "#632d55",
    CardType.assassin: "#0f1011",
    CardType.captain: "#104894",
    CardType.ambassador: "#a59533",
}

CARD_BACKGROUND_COLOR_MAP: Dict[CardType, str] = {
    CardType.contessa: "#000000",
    CardType.duke: "#000000",
    CardType.assassin: "#A9A9A9",
    CardType.captain: "#A9A9A9",
    CardType.ambassador: "#000000",
}


class Card(BaseModel):
    foreground_color: str
    background_color: str
    card_type: CardType

    @property
    def style(self) -> str:
        return f"{self.foreground_color} on {self.background_color}"

    def __str__(self):
        return f"{self.card_type.value}"


def build_deck() -> List[Card]:
    def _create_card(card_type: CardType):
        return Card(
            foreground_color=CARD_FOREGROUND_COLOR_MAP.get(card_type),
            background_color=CARD_BACKGROUND_COLOR_MAP.get(card_type),
            card_type=card_type,
        )

    return [
        _create_card(CardType.contessa),
        _create_card(CardType.contessa),
        _create_card(CardType.contessa),
        _create_card(CardType.duke),
        _create_card(CardType.duke),
        _create_card(CardType.duke),
        _create_card(CardType.assassin),
        _create_card(CardType.assassin),
        _create_card(CardType.assassin),
        _create_card(CardType.ambassador),
        _create_card(CardType.ambassador),
        _create_card(CardType.ambassador),
        _create_card(CardType.captain),
        _create_card(CardType.captain),
        _create_card(CardType.captain),
    ]
