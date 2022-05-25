"""
quizApp Main Menu

"""
from rich import print
from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table

console = Console()


def make_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1)
    )
    layout["main"].split_row(
        Layout(name="body", ratio=2, minimum_size=60),
        Layout(name="side"),
    )
    return layout


def make_menu_options() -> Panel:
    """Some example content."""
    menu_options = Table.grid(padding=1)
    menu_options.add_column(style="green", justify="left")
    menu_options.add_column(no_wrap=True)
    menu_options.add_row(
        "1)",
        "Start a Quiz",
    )
    menu_options.add_row(
        "2)", "Review Last Quiz",
    )
    menu_options.add_row(
        "3)", "Select Category",
    )
    menu_options.add_row(
        "4)", "Logout"
    )

    message = Table.grid(padding=1)
    message.add_column()
    message.add_column(no_wrap=True)

    message_panel = Panel(
        Align.center(
            Group(Align.center(menu_options)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b cyan]Main Menu",
        border_style="bright_blue",
    )
    return message_panel


class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_row(
            "[b]quizApp[/b] Let's review!",
        )
        return Panel(grid, style="white on blue")


class Side:
    def __rich__(self) -> Panel:
        side_content = "Review recent incorrect answers"
        # TODO Make this into a table
        return Panel(Align.center(
            Group(Align.center(side_content))
        ),
            title="Review",
            border_style="red"
        )


def display_main_menu():
    layout = make_layout()
    layout["header"].update(Header())
    layout["body"].update(make_menu_options())
    layout["side"].update(Side())
    print(layout)
