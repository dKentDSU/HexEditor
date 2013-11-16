#building class

class Building:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        
    def getType(self):
        return self.type
    
    def getName(self):
        return self.name
        