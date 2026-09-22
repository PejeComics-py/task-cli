import task

print("----Welcome to task-cli----")
print("This program looks to manage your todo in your daily life")
print("Option list: ")

while True:
    choice = int(input("1)Manage your tasks\n2)Display tasks\n3)Exit\n"))
    match choice: 
        case 1:
            #Mange your tasks lol
            print 
        case 2:
            #Display task
            print
        case 3:
            #Exit
            print("Exiting program...")
            break
