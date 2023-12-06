import random

from rich.console import Console
from rich.highlighter import Highlighter
from rich.prompt import Confirm, Prompt
from rich.table import Table
from rich.text import Text
from rich.tree import Tree

console = Console()


class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(f"color({random.randint(16, 255)})", index, index + 1)


def print_text(content: str, style: str = "", rainbow: bool = False, with_markup: bool = False):
    text = Text(content)

    if with_markup:
        text = Text.from_markup(content)

    if style:
        text.stylize(style)

    if rainbow:
        text = RainbowHighlighter()(text)

    console.print(text)


def print_texts(*parts):
    text = Text.assemble(*parts)

    console.print(text)


def print_tree(root: str, content: list[str]):
    tree = Tree(root)
    for line in content:
        tree.add(line)
    console.print(tree)


def print_table(table: Table):
    console.print(table)


def print_prompt(content: str) -> str:
    response = None
    while not response:
        response = Prompt.ask(content)
    return response


def print_confirm(content: str) -> bool:
    return Confirm.ask(content)


def print_blank():
    console.print()
