import fileHandling
import task
from fileHandling import FileHandling
import sys

def welcome():
    """ Print welcome message """
    print("----Welcome to task-cli----")
    print("This program looks to manage your todo in your daily life")
    print("Option list: ")

def menu():
    """Display menu"""
    operate = FileHandling()
    choice = int(input("1)Add a task\n2)Delete a task\n3)Edit a task\n4)Display tasks\n5)Exit\nSelect an option: "))
    match choice: 
        case 1:
            #Add a task
            temp_desc = input("Enter description: ")
            temp_task = task.Task(temp_desc)
            operate.saveInFile(temp_task)
            print(f"Task add successfully (ID: {temp_task.getID})")
        case 2:
            #Delete a task
            pass
        case 3:
            #Edit a task
            pass
        case 4:
            #Display tasks
            pass
        case _: 
            #Exit program
            print("Exiting program...")
            sys.exit(0)
           

if __name__ == "__main__":
    welcome()
    while True:
        menu()
        
