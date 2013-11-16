from tile import Tile
#import panda node thingy

class Country:
    def __init__(self,tiles,income,owner = -1):
        self.tiles = tiles
        self.income = income
        self.owner = owner
        
    def getTiles(self):
        return self.tiles
        
    #gets a specific tile from this country
    def getSpecTile(self,x,y):
        for tile in self.tiles:
            if tile.getX() == x and tile.getY() == y:
                return tile
                
    def getOwner(self):
        return self.owner
        
    def setOwner(self,newOwner):
        self.owner = newOwner
        
    def getIncome(self):
        return self.income
        
    def drawCountry(self):
        pass
        
       