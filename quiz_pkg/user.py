from rich import print
from quiz_pkg.print_to_term import print_error, print_success, print_info
from rich.prompt import Prompt
from quiz_pkg.models import User


class CurrentUser:
    def __init__(self, username: str, name: str):
        self.username = username
        self.name = name


def register():
    print_info("User Registration", "Please complete the following fields to register")
    # Prompt the user for their name
    while True:
        name = Prompt.ask(
            "[bold blue]Please enter your name.[/bold blue] My name is..").strip()
        if name == "":
            # They did not provide a name
            print_error("Name:", "Please enter your name")
            continue
        break
    # Prompt the user for their username
    while True:
        username = Prompt.ask("[bold blue]Please enter a Username.[/bold blue] Must be between 1 and 15 characters").strip()
        # Check to see if the username is already taken
        user_exists = User.select().where(User.username == username).count()
        if user_exists != 0:
            print_error("Username:", "Sorry, that username is already taken.")
            continue
        elif len(username) not in range(1, 16):
            # The username is too long or too short
            print_error("Username:", "Sorry, that username is invalid. Must be between 1 and 15 characters")
            continue
        break

    # Prompt the user for their password
    while True:
        password = Prompt.ask("[bold blue]Please enter a password.[/bold blue] Must be at least 8 characters",
                              password=True).strip()
        if len(password) < 8:
            print_error("Password:", "Sorry, the password is too short.")
            continue
        break

    # Confirm the password
    while True:
        password_confirmed = Prompt.ask("[bold blue]Please confirm your password", password=True).strip()
        if password != password_confirmed:
            print_error("Password Confirmation", "Sorry, those passwords to not match")
            continue
        break

    # TODO add the user to the database and then set Current User to instance of the model object
    return CurrentUser(username, name)
