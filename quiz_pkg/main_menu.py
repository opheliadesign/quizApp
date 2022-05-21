from rich import print
from rich.layout import Layout
from rich.panel import Panel


def make_layout() -> Layout:
    """Define the layout"""
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


class Header:
    # Maybe use a table here?
    def __rich__(self) -> Panel:
        return Panel("Choose an option from the menu below!", title="Welcome", style="white on blue")


class Body:
    def __rich__(self) -> Panel:
        return Panel("Choose from the options below", title="Main Menu")
