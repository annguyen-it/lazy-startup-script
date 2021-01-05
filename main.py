from vscode import vscode_setup
from udemy import udemy_setup
from postman import postman_setup
from demo import demo_setup
from WindowMgr import move_to_desktop

move_to_desktop(0)

vscode_setup()
udemy_setup()

move_to_desktop(1)

postman_setup()
demo_setup()
