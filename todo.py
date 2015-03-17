#!/usr/bin/python
#Author : Ryan Clair
#Verion : 1.2

import pickle
import os.path
import os

# Create two empty lists
todo = [] #All todo's
task = [] #Use for interpreting user input

#Set location of where task.cfg should live/lives
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

# function that commits changes to the to-do list to disk
def write_disk():
    output = open(location, 'wb')
    pickle.dump(todo, output)
    output.close()
    
# Print header + all the tasks in the todo list
def print_todo():
    print "Current Tasks"
    print "------------------"
    for i in range(len(todo)):
        print i + 1, bcolors.RED + todo[i] + bcolors.ENDC

# function that clears the terminal screen's window
def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

# function that does the default set of actions after a change
def default_action():
    write_disk()
    clear_window()
    print_todo()
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
    
    if task == "exit":
        exit = True
        clear_window()
        print "Saving tasks..."
        #If exiting, commit the todo list to disk
        write_disk() 
        
        print "Saved, exiting."
        
    elif action == "d":
        iitem = int(item) - 1
        for x in range(len(todo)):
            if x == iitem:
                todo.remove(todo[x]) #If removing, remove the task
        default_action()
    elif action == "c":
        todo.append(item) # If creating a task, add the task
        default_action()
    elif action == "p":
        clear_window()
        print_todo() # If printing, print all the tasks
    elif action == "r":
        iitem = int(item) - 1
        #If replacing a task, search for the task number as it relates to the position in the todo list
        for x in range (len(todo)):
            if x == iitem: 
                todo[x] = raw_input("Replace with: ") # Then prompt user with what to replace it with, and put it into the list
        default_action()
    elif action == "m": #If user wants to move the task, ask for the new order number for said task and shift all other tasks after it up.
        iitem = int(item) - 1
        ntask = int(raw_input("New Task Number:>")) - 1
        #Check to see if user didn't change the task number or that the number is invalid, otherwise commit changes
        if iitem == ntask or ntask < 0:
            default_action()
            continue
        else: 
            old = todo.pop(iitem) #remove the task from the array and store into memory
            todo.insert(ntask, old) #insert the task back into the array 
            default_action()
        
    elif task == "h": #If asking for help, print instructions
        print "h          - shows this screen"
        print "c (task)   - creates a (task) to the list"
        print "r #        - replaces task with number #, and prompts for new task description"
        print "d #        - deletes task number from the list. See 'p' for task number"
        print "m #        - moves task # to a new task #"
        print "p          - prints current task list. First column is the task number, second column is the task description"
        print "exit       - to exit the program"
    else:
        print "Invalid command. Type \"h\" for help" #all else, tell them to check help
    str(item)
    

