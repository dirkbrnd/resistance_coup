import random
from typing import List, Tuple, Optional

from pydantic import BaseModel

from src.models.action import ActionType
from src.models.card import Card


class Player(BaseModel):
    name: str
    coins: int = 0
    cards: List[Card] = []
    is_ai: bool = False
    is_active: bool = False

    def reset_player(self):
        self.coins = 0
        self.cards = []

    def _validate_action(self, action: ActionType, player: "Player"):
        # Need at least 7 coins to coup
        if action == ActionType.coup and self.coins < 7:
            return False

        # Need at least 3 coins to assassinate
        if action == ActionType.assassin_assassinate and self.coins < 3:
            return False

        # Can't steal from player with 0 coins
        if action == ActionType.captain_steal and player.coins == 0:
            return False

        return True

    def random_action(self, players: List["Player"]) -> Tuple[ActionType, Optional["Player"]]:
        # You must coup if you have more than 10 coins
        if self.coins >= 10:
            player = random.choice(players)
            return ActionType.coup, player

        # Pick any other random choice (might be a bluff)
        action = random.choice(list(ActionType))
        player = random.choice(players)

        # Make sure we have a valid action/player combination
        while not self._validate_action(action, player):
            action = random.choice(list(ActionType))
            player = random.choice(players)

        return action, player

    def __str__(self):
        return f"{self.name}"
