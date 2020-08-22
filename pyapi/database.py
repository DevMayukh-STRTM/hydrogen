import re
import os
import pickle
import sys

import http


#Exeption Start

class HydrogenDatabaseNotFound(Exception):
    pass

class HydrogenInvalidInit(Exception):
    pass

class HydrogenInvalidTable(Exception):
    pass

class HydrogenDataError(Exception):
    pass

class HydrogenDatabaseExist(Exception):
    pass

#Exeption Ends

class HydrogenDB:
    def __init__(self, attr):
        if type(attr) == type([]) and len(attr) == 2:
            self.data = attr
        else:
            raise HydrogenDataError("Invalid Database argument")
    

    def generateBase(self):
        import datetime
        return {
            "meta": {
                "name": f"{self.data[0]}",
                "date_created": f"{datetime.datetime.now()}",
                "password": f'{self.data[1]}'
            }
        }
    def createDB(self):
        if os.path.isfile(f"{self.data[0]}"):
            raise HydrogenDatabaseExist(f"Database \"{self.data[0]}\" Already exist")
        else:
            pickle.dump(self.generateBase(), open(f"{self.data[0]}.hdb", "wb"))

    