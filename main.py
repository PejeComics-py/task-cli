import task
import json
import os

#Note: If .json does not exist, function creates it
def createFile():
    try:
        json_file = "tasks.json"
        fileSerialized= open(json_file,"x")
        current_path = os.path.dirname(os.path.abspath(__file__))
        if os.path.isfile(os.path.join(current_path,json_file)):
            print(f"WARN: File was {json_file} correctly")
        fileSerialized.close()
    except FileExistsError:
        return


#Note: Verify if .json exist and call createFile() for that, else just write objects past as *args into .json
def saveInFile(*args):
    json_file = "tasks.json"
    current_path = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(os.path.join(current_path,json_file)):
        fileSerialized = open(json_file,"w")
        for arg in args: 
            fileSerialized.write(json.dumps(arg.__dict__,indent=2,default=str))
        fileSerialized.close()
    else:
        print("Creating file...")
        createFile()
        print("writing file...")
        saveInFile(*args)

"""
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
"""
