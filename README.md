# todo
Simple todo app written in Python.

Writes out the todo's to a file called tasks.cfg in the current directory that app is launched from. So your todo's can be backed up or moved to another machine (or placed on a sync/share folder like Syncplicity for other machines to access).

Requires Python to be installed.

# Syntax

h          - shows help screen

a (task)   - adds a (task) to the list

r #        - replaces the task with task ID #, and prompts for new task description

d #        - deletes task ID and it's associated task description from the list.

p          - prints current task list. First column is the task ID, second column is the task description (in red)

exit       - to exit the program


You can customize the color on line 35 by replacing bcolor.RED with whatever color you want in the bcolor class above.
