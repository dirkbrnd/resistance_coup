from enum import Enum
from typing import List, Dict

from pydantic import BaseModel

class CardType(Enum):
    contessa = 0
    duke = 1
    assassin = 2
    captain = 3
    ambassador = 4


CARD_COLOR_MAP: Dict[CardType, str] = {
    CardType.contessa: "#6d191c",
    CardType.duke: "#632d55",
    CardType.assassin: "#0f1011",
    CardType.captain: "#104894",
    CardType.ambassador: "#a59533",
}


class Card(BaseModel):
    color: str
    type: CardType

    def __str__(self):
        return f"[{self.color}]{self.type}[/]"


def create_card(card_type: CardType):
    return Card(
        color=CARD_COLOR_MAP.get(card_type),
        type=card_type
    )


def create_deck() -> List[Card]:
    return [
        create_card(CardType.contessa),
        create_card(CardType.contessa),
        create_card(CardType.contessa),
        create_card(CardType.duke),
        create_card(CardType.duke),
        create_card(CardType.duke),
        create_card(CardType.assassin),
        create_card(CardType.assassin),
        create_card(CardType.assassin),
        create_card(CardType.ambassador),
        create_card(CardType.ambassador),
        create_card(CardType.ambassador),
        create_card(CardType.captain),
        create_card(CardType.captain),
        create_card(CardType.captain)
    ]