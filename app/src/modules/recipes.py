import json
import random

class Recepies:
    
    def __init__(self):
        self.file_path = "app/resources/recipes.json"
     
    def getAll(self):
        with open(self.file_path,"r",encoding="utf-8",) as file:
            data = json.load(file)
        return data

    def getRandom(self):
        return random.choice(self.getAll())
