from quiz_pkg.main_menu import *
from quiz_pkg.print_to_term import print_error
from os.path import exists

if not exists("quiz_app.db"):
    # Check to see if there is an existing SQLite database. If not, create it
    print_error("ERROR", "The database must be initialized before running the app.\n"
                         "Please run [bold]create_db.py[/bold]")
    exit()
layout = make_layout()
layout["header"].update(Header())
layout['body'].update(Body())
print(layout)
