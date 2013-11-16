#player class

class Player:
    # might need to pass in map for the has base function
    def __init__(self,id,funds,faction,baseX,baseY):
        self.id = id
        self.unitCount = 0
        self.funds = funds
        self.upgrades = []
        self.faction = faction
        self.baseX = baseX
        self.baseY = baseY
        
    def hasBase(self):
        #check to see if player is still in posession of his base
        if self.map.getCountryOwnerByTile(baseX,baseY) == self.id:
            return True
        else:
            return False
            
    def getFunds(self):
        return self.funds
		
    def getIncome(self,countries):
        amount = 0
        for country in countries:
            amount += country.getIncome()
        return amount
			
    def applyIncome(self,countries):
        #get money value from the list of countries
        for country in countries:
            self.funds += country.getIncome()
        
    def getUpgrades(self):
        return self.upgrades
        
    def getUnitCount(self):
        return self.unitCount
        
        # sets players unit count with pos or negative numbers
    def setUnitCount(self,unitNum):
        self.unitCount += unitNum
        
    def getFaction(self):
        return self.faction
        