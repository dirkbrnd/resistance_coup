import random
from rich.prompt import Prompt, Confirm
from typing import List

from rich import print
import names

from src.models.card import create_deck, Card
from src.models.player import Player
from src.utils import generate_table


class ResistanceCoupGameHandler:
    _players: List[Player] = []
    _current_player_index = 0
    _deck: List[Card] = []
    _number_of_players: int = 0

    def __init__(self, player_name: str, number_of_players: int):
        self._number_of_players = number_of_players

        # Set up players
        self._players: List[Player] = [Player(name=player_name)]

        for i in range(number_of_players - 1):
            gender = random.choice(["male", "female"])
            ai_name = names.get_first_name(gender=gender)
            self._players.append(Player(name=ai_name, is_ai=True))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def reset_game(self):
        self.deck = create_deck()
        self.shuffle_deck()

        for player in self._players:
            player.reset_player()

            # Deal 2 cards to each player
            player.cards.append(self.deck.pop())
            player.cards.append(self.deck.pop())

            # Gives each player 2 coins
            player.coins = 2

            # Includes the player in the game
            player.is_active = True

        # Random starting player
        self._current_player_index = random.randint(0, self._number_of_players-1)

    def print_players(self):
        print()
        print(generate_table(self._players, self._current_player_index))
        print()

    def draw_card(self):
        if self.deck:
            return self.deck.pop()
        else:
            print("No more cards in the deck!")

    def get_current_player(self):
        return self._players[self._current_player_index]

    def handle_turn(self):
        current_player = self.get_current_player()

        # Player chooses action
        if current_player.is_ai:
            players_without_current = self._players.copy()
            players_without_current.pop(self._current_player_index)
            action, player = current_player.random_action(players_without_current)
        else:
            prompt


        # Opportunity to counter

        # Move index to next player
        self._current_player_index = (self._current_player_index + 1) % len(self._players)

