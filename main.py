import rich_click as click

from handler.game_handler import ResistanceCoupGameHandler


@click.group("coup_game")
@click.pass_context
@click.argument(
    "number-of-players",)
def start_game(ctx, number_of_players: int):
    """Start a new game."""
    click.echo(f"Starting the game for {number_of_players} players")
    click.prompt("Provide a name for your user: ", confirmation_prompt=True)
    ctx.handler = ResistanceCoupGameHandler()


def main():
    start_game(prog_name="coup_game")


if __name__ == '__main__':
    main()