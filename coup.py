from rich.panel import Panel
from rich.text import Text

from src.handler.game_handler import ResistanceCoupGameHandler
from src.utils.print import (
    console,
    print_blank,
    print_confirm,
    print_prompt,
    print_text,
)

console.clear()


if __name__ == "__main__":
    text = Text(
        """
        In the not too distant future, the government is run for profit by a new 'royal class' of multinational CEOs.
        
        Their greed and absolute control of the economy has reduced all but a privileged few to lives of poverty.

        Out of the oppressed masses rose The Resistance, an underground organization focused on overthrowing these
        powerful rulers.
        
        The valiant efforts of The Resistance have created discord, intrigue, and weakness in the political courts of
        the noveau royal, bringing the government to brink of collapse.
        
        But for you, a powerful government official, this is your opportunity to manipulate,
        bribe and bluff your way into absolute power.
        
        To be successful, you must destroy the influence of your rivals and drive them into exile.
    
        In these turbulent times there is only room for one to survive.
    """,
        justify="center",
    )
    panel = Panel(
        text,
        title=":sleuth_or_spy:  [grey46]The Resistance: [hot_pink3 bold]Coup",
        subtitle="[plum1]By Dirk Brand",
    )
    console.print(panel)

    console.print()
    player_name = print_prompt("What is your name, player?")
    handler = ResistanceCoupGameHandler(player_name, 5)

    console.print()
    game_ready = print_confirm("Ready to start?")

    # Play the game
    while game_ready:
        handler.reset_game()

        # Take turns until we have a winner
        end_state = False
        turn_count = 0
        while not end_state:
            turn_count += 1

            console.print()
            panel = Panel(Text(f"Turn {turn_count}", style="bold", justify="left"), expand=False)
            console.print(panel)

            handler.print_players()
            console.print(
                Text.assemble("Current Player: ", (str(handler.current_player), "bold magenta"))
            )

            end_state = handler.handle_turn()

        console.print()
        game_ready = print_confirm("Want to play again?")

    print_blank()
    print_text("GAME OVER", rainbow=True)
