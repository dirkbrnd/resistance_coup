from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich import print

from src.handler.game_handler import ResistanceCoupGameHandler
from src.utils import RainbowHighlighter

console = Console()
# console.set_alt_screen(True)
console.clear()

rainbow = RainbowHighlighter()

if __name__ == '__main__':
    text = Text("The Resistance: Coup", justify="center")
    text.stylize("bold magenta", 16, 20)
    panel = Panel(text)
    console.print(panel)

    player_name = Prompt.ask("What is your name, player?")
    handler = ResistanceCoupGameHandler(player_name, 5)

    print()
    game_ready = Confirm.ask("Ready to start?")

    # Play the game
    while game_ready:
        handler.reset_game()

        # Take turns until we have a winner
        while True:
            handler.print_players()
            console.print(Text.assemble("Current Player: ", (str(handler.get_current_player()), "bold magenta")))

            handler.handle_turn()


        print()
        game_ready = Confirm.ask("Want to play again?")

    print(rainbow("GAME OVER"))