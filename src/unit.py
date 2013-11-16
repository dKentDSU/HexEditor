#import panda node thingy

class Unit:
    def __init__(self,cost,name,type,faction,attackDie,defenseDie,move,health,node):
        self.owner = -1
        self.cost = cost
        self.name = name
        self.type = type
        self.faction = faction
        self.attackDie = attackDie
        self.defenseDie = defenseDie
        self.move = move
        self.health = health
        self.node = node
    
        
    def setNode(self,newNode):
        self.node = newNode
    
    def setOwner(self,ownerNum):
        self.owner = ownerNum
        
    def getUnitName(self):
        return self.name
        
    def getUnitType(self):
        return self.type
        
    def getUnitFaction(self):
        return self.faction
        
    def getAttackDie(self):
        return self.attackDie
        
    def getDefenseDie(self):
        return self.defenseDie
        
    def getMove(self):
        return self.move
        
    def getHealth(self):
        return self.health
        
    def getCost(self):
        return self.cost
        
    def setUnitAttackDie(self,dieNum):
        self.attackDie = dieNum
        
    def setUnitDefenseDie(self,dieNum):
        self.DefenseDie = dieNum
        
    def setUnitMove(self,moveNum):
        self.move = moveNum
        
    def setHealth(self,healthNum):
        self.health = healthNum