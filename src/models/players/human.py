from typing import List, Optional, Tuple

from src.models.action import Action
from src.models.card import Card
from src.models.players.base import BasePlayer
from src.utils.print import (
    print_blank,
    print_confirm,
    print_prompt,
    print_text,
    print_tree, print_texts,
)


class HumanPlayer(BasePlayer):
    is_ai: bool = False

    def _choose_action(
        self, other_players: List[BasePlayer]
    ) -> Tuple[Action, Optional[BasePlayer]]:
        available_actions = self.available_actions()

        print_tree(
            "You have the following actions available:",
            [f"{ind} - {str(action)}" for ind, action in enumerate(available_actions)],
        )

        print_blank()
        target_action_ind = print_prompt("What action do you want to take? (provide the number)")
        target_action = available_actions[int(target_action_ind)]
        target_player = None

        # Only certain actions can target players
        if target_action.requires_target:
            print_blank()
            print_tree(
                "You can target any of the following players:",
                [f"{ind} - {str(player)}" for ind, player in enumerate(other_players) if player.is_active],
            )
            print_blank()
            target_player_ind = print_prompt("Which player are you targeting? (provide the number)")
            target_player = other_players[int(target_player_ind)]

        return target_action, target_player

    def choose_action(self, other_players: List[BasePlayer]) -> Tuple[Action, Optional[BasePlayer]]:
        target_action, target_player = self._choose_action(other_players)

        # Make sure we have a valid action/player combination
        while not self._validate_action(target_action, target_player):
            target_action, target_player = self._choose_action(other_players)

        return target_action, target_player

    def determine_challenge(self, player: BasePlayer) -> bool:
        print_blank()
        challenge = print_confirm(f"Do you wish to challenge {str(player)}?")
        return challenge

    def determine_counter(self, player: BasePlayer) -> bool:
        print_blank()
        challenge = print_confirm(f"Do you wish to counter {str(player)}?")
        return challenge

    def remove_card(self) -> None:
        print_text("Unfortunately you have to discard a card...")
        # You only have 1 card
        if len(self.cards) == 1:
            chosen_card_ind = 0
        else:
            print_tree(
                "You have the following cards in your hand:",
                [
                    f"{ind} - [{card.foreground_color} on {card.background_color}]{card}"
                    for ind, card in enumerate(self.cards)
                ],
            )

            print_blank()
            chosen_card_ind = print_prompt("Which card do you want to discard? (provide the number)")

        discarded_card = self.cards.pop(int(chosen_card_ind))

        print_blank()
        print_texts(
            f"{self} discarded their ", (f"{discarded_card}", discarded_card.style), " card"
        )

    def choose_exchange_cards(self, exchange_cards: list[Card]) -> Tuple[Card, Card]:
        print_text("You drew 2 cards from the deck, but you have to give 2 back...")
        self.cards += exchange_cards

        print_tree(
            "You have the following cards in your hand:",
            [
                f"{ind} - [{card.foreground_color} on {card.background_color}]{card}"
                for ind, card in enumerate(self.cards)
            ],
        )
        print_blank()
        first_card_ind = print_prompt("What is the first card you want to discard? (provide the number)")
        first_card = self.cards.pop(int(first_card_ind))

        print_tree(
            "You have the following cards in your hand:",
            [
                f"{ind} - [{card.foreground_color} on {card.background_color}]{card}"
                for ind, card in enumerate(self.cards)
            ],
        )
        second_card_ind = print_prompt("What is the second card you want to discard? (provide the number)")
        second_card = self.cards.pop(int(second_card_ind))

        return first_card, second_card
