import random

from rich.console import Console, JustifyMethod
from rich.highlighter import Highlighter
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table
from rich.text import Text
from rich.tree import Tree

from src.models.action import Action, ActionType, CounterAction, CounterActionType
from src.models.players.base import BasePlayer

console = Console()


class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(f"color({random.randint(16, 255)})", index, index + 1)


def print_blank():
    console.print()


def print_text(content: str, style: str = "", rainbow: bool = False, with_markup: bool = False):
    print_blank()

    text = Text(content)

    if with_markup:
        text = Text.from_markup(content)

    if style:
        text.stylize(style)

    if rainbow:
        text = RainbowHighlighter()(text)

    console.print(text)


def print_texts(*parts):
    print_blank()

    text = Text.assemble(*parts)

    console.print(text)


def print_tree(root: str, content: list[str]):
    print_blank()

    tree = Tree(root)
    for line in content:
        tree.add(line)
    console.print(tree)


def print_table(table: Table, justify: JustifyMethod = "center"):
    print_blank()

    console.print(table, justify=justify)


def print_panel(panel: Panel, justify: JustifyMethod = "center"):
    print_blank()

    console.print(panel, justify=justify)


def print_prompt(content: str) -> str:
    response = None
    while not response:
        response = Prompt.ask(content)
    return response


def print_confirm(content: str) -> bool:
    print_blank()
    return Confirm.ask(content)


def build_action_report_string(
    player: BasePlayer, action: Action, target_player: BasePlayer
) -> str:
    action_report_string = f"[bold magenta]{player}[/] chose to "
    match action.action_type:
        case ActionType.income:
            action_report_string += "take income."
        case ActionType.foreign_aid:
            action_report_string += "take foreign aid."
        case ActionType.coup:
            action_report_string += f"perform a coup against {target_player.name}."
        case ActionType.tax:
            action_report_string += "take tax because they have influence over a Duke."
        case ActionType.assassinate:
            action_report_string += f"assassinate {target_player.name}."
        case ActionType.steal:
            action_report_string += f"steal coin from {target_player.name}"
        case ActionType.exchange:
            action_report_string += (
                "perform an exchange, because they have influence over an Ambassador."
            )

    return action_report_string


def build_counter_report_string(
    target_player: BasePlayer, counter: CounterAction, countering_player: BasePlayer
) -> str:
    counter_report_string = f"{countering_player} chose to "
    match counter.counter_type:
        case CounterActionType.block_foreign_aid:
            counter_report_string += f"block {target_player}'s attempt to take foreign aid."
        case CounterActionType.block_assassination:
            counter_report_string += f"block {target_player}'s assassination attempt."
        case CounterActionType.block_steal:
            counter_report_string += f"block {target_player} from stealing."

    return counter_report_string
