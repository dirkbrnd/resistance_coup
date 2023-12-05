from enum import Enum


class ActionType(str, Enum):
    income = "INCOME"
    foreign_aid = "FOREIGN_AID"
    coup = "COUP"
    duke_tax = "TAX"
    assassin_assassinate = "ASSASSINATE"
    captain_steal = "STEAL"
    ambassador_exchange = "EXCHANGE"


class CharacterCounterActionType(Enum):
    duke_block_foreign_aid = 0
    contessa_block_assassination = 1
    ambassador_block_stealing = 2

