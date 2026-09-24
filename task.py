import datetime

class Task:
    # Apparently, self is calling the object in python
    #Note: Need to asociate counter with the instances created with the tasks.json, once you close the program counter starts again, not really useful
    counter = 1
    def __init__(self,description):
        self.__id = Task.counter
        self.__description = description
        self.__status = "todo"
        self.__createdAt = datetime.datetime.now()
        self.__updatedAt = datetime.datetime.now()
        Task.counter +=1
    @property
    def getID(self): 
        return self.__id
    @property
    def getDesc(self):
        return self.__description
    #IDEA: retrieve whole description and allow user to change description partially instead of change the whole description
    #HOW: Retrieve the saved description and allow edition to replace the description inside task object
    @property
    def setDesc(self, description):
        self.__description = description
    @property
    def getStatus(self):
        return self.__status
    @property
    def setStatus(self, status):
        if status == "todo":
            print("ERROR: You can't change a task with a todo status")
            return
        self.__status = status
    @property
    def getCreatedAt(self):
        return self.__createdAt
    @property
    def setUpdatedAt(self):
        self.__updatedAt = datetime.datetime.now()

    #INFO: Like the toString() method in java, changes the representation of an object
    def __repr__(self):
        return '{\n\tid: %d,\n\tdescription: %s,\n\tstatus: %s,\n\tcreated at: %s,\n\tupdated at: %s\n}'%(self.__id,self.__description,self.__status,self.__createdAt,self.__updatedAt)
