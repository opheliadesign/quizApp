from quiz_pkg.main_menu import *
from quiz_pkg.print_to_term import print_error
from os.path import exists

if not exists("quiz_app.db"):
    # Check to see if there is an existing SQLite database. If not, create it
    print_error("ERROR", "The database must be initialized before running the app.\n"
                         "Please run [bold]create_db.py[/bold]")
    exit()

# Start out without a registered user
User = None
# Display the app's main menu
display_main_menu()
