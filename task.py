import datetime
import json

class task:
    # Apparently, self is calling the object in python
    def __init__(self,id,description):
        self.__id = id
        self.__description = description
        self.__status = "todo"
        self.__createdAt = datetime.datetime.now()
        self.__updatedAt = datetime.datetime.now()
    

    def getID(self): 
        return self.__id
    def setID(self, id):
        self.__id = id
    def getDesc(self):
        return self.__description
    #IDEA: retrieve whole description and allow user to change description partially instead of change the whole description
    #HOW: Retrieve the saved description and allow edition to replace the description inside task object
    def setDesc(self, description):
        self.__description = description
    def getStatus(self):
        return self.__id
    def setStatus(self, status):
        if status == "todo":
            print("ERROR: You can't change a task with a todo status")
            return
        self.__status = status
    def getCreatedAt(self):
        return self.__createdAt
    def setUpdatedAt(self):
        self.__updatedAt = datetime.datetime.now()

    #Like the toString() method in java, changes the representation of an object

    def __repr__(self):
        return '{\n\tid: %d,\n\tdescription: %s,\n\tstatus: %s,\n\tcreated at: %s,\n\tupdated at: %s\n}'%(self.__id,self.__description,self.__status,self.__createdAt,self.__updatedAt)
