import task
import json
import os

# Note: Finally made this work 
def saveInFile(task):
    json_file = "tasks.json"
    current_path = os.path.dirname(os.path.abspath(__file__)) #Assign current path file to current_path variable
    if os.path.isfile(os.path.join(current_path,json_file)): #Checks if the file exists, if not, jumps to createFile() and comes back to this fucntion
        with open(json_file,"r") as stream1: 
            file_data = json.load(stream1)
            file_data["tasks"].append(task.__dict__)
            with open(json_file,"w") as stream2:
                stream2.write(json.dumps(file_data,indent=4,default=str))
    else:
        createFile() 
        saveInFile(task)

#Note: If .json does not exist, function creates it
def createFile():
    json_file = "tasks.json"
    current_path = os.path.dirname(os.path.abspath(__file__))
    count = 0
    if not os.path.isfile(os.path.join(current_path,json_file)):
        file = open(json_file,"w")
        tasks = {"tasks" : []} 
        file.write(json.dumps(tasks,indent=4,default=str)) #Default=str to cascade attributes into a str
        print(f"WARN: File was {json_file} created correctly")
        file.close()
    else: 
        count +=1 
        if count < 1:
            print(f"WARN: File {json_file} already exists")
        return

#INFO: read file or whatever, does not work yet 
def readFile():
    json_file = "tasks.json"
    current_path = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(os.path.join(current_path,json_file)):
        extracted_objs = []
        with open(json_file,'r') as file:
            for line in file:
                json_obj = json.loads(line)
                extracted_objs.append(json_obj)
        return extracted_objs
    else: 
        createFile()
        readFile()

print("----Welcome to task-cli----")
#Note: You may need to expand programs' description, currently it is too simple 
print("This program looks to manage your todo in your daily life")
print("Option list: ")
try:
    while True:
        choice = int(input("1)Add a task\n2)Delete a task\n3)Edit a task\n4)Display tasks\n5)Exit\nSelect an option: "))
        match choice: 
            case 1:
                #Add a task
                temp_desc = input("Enter description: ")
                temp_task = task.Task(temp_desc)
                saveInFile(temp_task)
                print(f"Task add successfully (ID: {temp_task.getID})")
            case 2:
                #Delete a task
                print(readFile())

                continue
            case 3:
                #Edit a task
                continue
            case 4:
                #Display tasks
                continue
            case _: 
                #Exit program
                print("Exiting program...")
                break
except KeyboardInterrupt:
    print("\nERROR: keyboard interrupt detected, exiting program...")


