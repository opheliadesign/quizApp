from rich import print
from rich.panel import Panel

"""
    Simple utility to print stylized alerts
"""


def print_to_term(title: str, message: str, bg_color: str):
    """
    Print to Term
    Prints the final message to the terminal, stylized
    :param title: Title to print
    :param message: Message to print
    :param bg_color: background color of the panel in HEX
    :return:
    """
    print(Panel(f"{message}", title=f"[bold]{title}[/bold]", style=f"white on {bg_color}", padding=1))


def print_success(title: str, message: str):
    """
    Print Success
    :param title: title of the message, eg "Success"
    :param message: body of the message, eg "You won!"
    :return:
    """
    print_to_term(title, message, "#188535")


def print_warning(title: str, message: str):
    """
    Print Warning
    :param title: title of the message, eg "Warning!"
    :param message: body of the message, eg "Sorry, wrong answer"
    :return:
    """
    print_to_term(title, message, "#a66e07")


def print_error(title: str, message: str):
    """
    Print Error
    :param title: title of the message, eg "Quiz Failed!"
    :param message: body of the message, eg "Better luck next time"
    :return:
    """
    print_to_term(title, message, "#8a1903")


def print_info(title: str, message: str):
    """
    Print Info
    :param title: title of the message, eg "Info" 
    :param message: body of the message, eg "Please fill out these fields"
    :return:
    """
    print_to_term(title, message, "#3260a8")
