import task
import json
import os

# Note: Finally made this work 
class FileHandling():
    def __init__(self):
        self.json_file = "tasks.json"

    def saveInFile(self,task):
        """Save task in json format"""
        #Assign current path file to current_path variable
        current_path = os.path.dirname(os.path.abspath(__file__)) 
        #Checks if the file exists, if not, jumps to createFile() and comes back to this fucntion
        if os.path.isfile(os.path.join(current_path,self.json_file)): 
            with open(self.json_file,"r") as stream1: 
                file_data = json.load(stream1)
                #Append data on dictionary
                file_data["tasks"].append(task.__dict__)
                with open(self.json_file,"w") as stream2:
                    stream2.write(json.dumps(file_data,indent=4,default=str))
        else:
            #Create the file in case is has not been created
            self.createFile() 
            self.saveInFile(task)

    #Note: If .json does not exist, function creates it
    def createFile(self):
        """Create file in current relative path"""

        current_path = os.path.dirname(os.path.abspath(__file__))
        count = 0
        try: 
            # If file exists, raise exception exception
            if os.path.isfile(os.path.join(current_path,self.json_file)):
                raise FileExistsError
            # Write file if not exists
            with open(self.json_file,"w") as file:
                tasks = {"tasks" : []} 
                file.write(json.dumps(tasks,indent=4,default=str)) #Default=str to cascade attributes into a str
                print(f"WARN: File was {self.json_file} created correctly")
                file.close()
        except FileExistsError: 
            print(f"WARN: File {self.json_file} already exists")

    def readFile(self):
        """ReadFile to extrat data"""
        #INFO: read file or whatever, does not work yet 
        current_path = os.path.dirname(os.path.abspath(__file__))
        if os.path.isfile(os.path.join(current_path,self.json_file)):
            extracted_objs = []
            with open(self.json_file,'r') as file:
                for line in file:
                    json_obj = json.loads(line)
                    extracted_objs.append(json_obj)
            return extracted_objs
        else: 
            self.createFile()
            self.readFile()
