from enum import Enum
from typing import List

from pydantic import BaseModel


class CardType(Enum, str):
    contessa = "CONTESSA"
    duke = "DUKE"
    assassin = "ASSASSIN"
    captain = "CAPTAIN"
    ambassador = "AMBASSADOR"


class BaseCard(BaseModel):
    color: str


class ContessaCard(BaseCard):
    color = "#CC6677"


class DukeCard(BaseCard):
    color = "#CC6677"


class AssassinCard(BaseCard):
    color = "#CC6677"


class CaptainCard(BaseCard):
    color = "#CC6677"


class AmbassadorCard(BaseCard):
    color = "#CC6677"


def create_card(card_type: CardType):
    match card_type:
        case CardType.contessa:
            return ContessaCard()


def create_deck() -> List[BaseCard]:
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