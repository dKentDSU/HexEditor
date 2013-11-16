from unit import Unit
from building import Building

#import panda node thingy

class Tile:
    def __init__(self,terrain,node,x,y,id):
        self.id = id
        self.terrainType = terrain
        self.node = node
        self.units = []
        self.building = None
        self.xPos = x
        self.yPos = y
        
    def getTerrainType(self):
        return self.terrainType
        
    def setTerrainType(self,newTerrain):
        self.terrainType = newTerrain
        
    def getUnits(self):
        return self.units
        
    def getUnitsCount(self):
        return len(self.units)
        
    def getBuilding(self):
        return self.building
    
    def addUnit(self,newUnit):
        self.units.append(newUnit)
        
    def addBuilding(self,newBuilding):
        #if exists a building don't add building, return false
        if self.building != None:
            return False
        else:
        # else no building add one return true
            self.building = newBuilding
            return True
            
    def drawTile(self):
        pass
        
    def getX(self):
        return self.xPos
        
    def getY(self):
        return self.yPos 
            
        
        
        
    