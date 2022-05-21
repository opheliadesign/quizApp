from quiz_pkg.main_menu import *

layout = make_layout()
layout["header"].update(Header())
layout['body'].update(Body())
print(layout)
