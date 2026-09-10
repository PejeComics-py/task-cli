import datetime

class task:
    # Apparently, self is calling the object in python
    def __init__(self,id,description,status):
        self.__id = id
        self.__description = description
        self.__status = status
        self.__createdAt = datetime.datetime.now()
        self.__updatedAt = datetime.datetime.now()
    

    def getID(self): 
        return self.__id
    def setID(self, id):
        self.__id = id
