
from pydantic import BaseModel


class Player(BaseModel):
    def __init__(self, name):
        super().__init__()

        self.name = name
        self.coins = 2
        self.cards = []

    def __str__(self):
        return f"{self.name} (Coins: {self.coins}, Cards: {self.cards})"