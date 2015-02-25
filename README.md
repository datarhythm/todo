# todo
Simple todo app written in Python.

Writes out the todo's to a file called tasks.cfg in the current directory that app is launched from. So your todo's can be backed up or moved to another machine (or placed on a sync/share folder like Syncplicity for other machines to access).

Requires Python to be installed.

# Syntax
<ol>
<il>h          - shows help screen</il>
<il>a (task)   - adds a (task) to the list</il>
<il>r #        - replaces the task with task ID #, and prompts for new task description</il>
<il>d #        - deletes task ID and it's associated task description from the list.</il>
<il>p          - prints current task list. First column is the task ID, second column is the task description (in red)</il>
<il>exit       - to exit the program</il>
</ol>


You can customize the color on line 35 by replacing bcolor.RED with whatever color you want in the bcolor class above.
