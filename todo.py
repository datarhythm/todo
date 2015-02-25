#!/usr/bin/python
#Author : Ryan Clair
#Verion : 1.0

import pickle
import os.path
import os

# Create two empty lists
todo = [] #All todo's
task = [] #Use for interpreting user input
location = './tasks.cfg'
# Class for changing text colors
class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# If existing config file exists, import it in, else it's blank
if os.path.exists(location) == True:
    tasks_file = open(location, 'rb')
    todo = pickle.load(tasks_file)
    tasks_file.close()

# Print header + all the tasks in the todo list
def print_todo():
    print "Current Tasks"
    print "------------------"
    for i in range(len(todo)):
        print i, bcolors.RED + todo[i] + bcolors.ENDC

# function that clears the terminal screen's window
def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear the window
clear_window()

# Print out current list of tasks
print_todo()
exit = False

# Run program until user types "exit"
while exit == False:
    # Prompt user for input
    task = raw_input("Input:> ")
    action = task[:1] #Set Action the first character of input
    item = task[2:] #Set task description as 'item'
    if action == "d":
        iitem = int(item)
        for x in range(len(todo)):
            if x == iitem:
                todo.remove(todo[x]) #If removing, remove the task
        clear_window()
        print_todo()
    elif action == "a":
        todo.append(item) # If adding, add the task
        clear_window()
        print_todo()
    elif action == "p":
        clear_window()
        print_todo() # If printing, print all the tasks
    elif action == "r":
        iitem = int(item)
        #If replacing a task, search for the task number as it relates to the position in the todo list
        for x in range (len(todo)):
            if x == iitem: 
                todo[x] = raw_input("Replace with: ") # Then prompt user with what to replace it with, and put it into the list
        clear_window()
        print_todo()
    elif task == "c":
        clear_window()
        print_todo()
        print "Commiting to disk..."
        output = open(location, 'wb')
        pickle.dump(todo, output)
        output.close()
        print "Committed."
        
    elif task == "exit":
        exit = True
        clear_window()
        print "Saving tasks..."
        #If exiting, commit the todo list to disk
        output = open(location, 'wb')
        pickle.dump(todo, output)
        output.close()
        
        print "Saved, exiting."
    elif task == "h": #If asking for help, print instructions
        print "h          - shows this screen"
        print "a (task)   - adds a (task) to the list"
        print "r #        - replaces task with number #, and prompts for new task description"
        print "d #        - deletes task number from the list. See 'p' for task number"
        print "p          - prints current task list. First column is the task number, second column is the task description"
        print "c          - Commits the todo list, and all it's recent changes, to tasks.cfg file"
        print "exit       - to exit the program"
    else:
        print "Invalid command. Type \"h\" for help" #all else, tell them to check help
    str(item)
    

