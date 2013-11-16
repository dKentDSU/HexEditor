from building import Building
from unit import Unit


class Faction:
    def __init__(self,filename):
        self.name = ""
        self.buildings = []
        self.units = []
        self.upgrades = []
        self.createFaction(filename)
        
    def createFaction(self,filename):
        #parse out of the file name and fill the class members
        filein = open(filename,"rb")
        buildingType = 0
        buildingName = ""

        unitName = ""
        unitCost = 0
        unitType = 0
        unitADie = 0
        unitDDie = 0
        unitMove = 0
        unitHealth = 0
        
        for line in filein:
            words = line.split()
            if words[0] == "<faction>":
                pass
                #can throw an error if this isn't parsed
            elif words[0] == "<fname>":
                self.name = words[1]
            elif words[0] == "<uvalue>":
                self.upgrades.append(eval(words[1]))
            elif words[0] == "<bname>":
                for word in words:
                    if word == "<bname>":
                        pass
                    elif word == "</bname>":
                        break
                    else:
                        buildingName += word + " "
            elif words[0] == "<btype>":
                buildingType = eval(words[1])
            elif words[0] == "</building>":
                buildingName.strip()
                newBuilding = Building(buildingName,buildingType)
                self.buildings.append(newBuilding)
                buildingName = ""
                buildingType = 0
            elif words[0] == "<name>":
                for word in words:
                    if word == "<name>":
                        pass
                    elif word == "</name>":
                        break
                    else:
                        unitName += word + " "
            elif words[0] == "<cost>":
                unitCost = eval(words[1])
            elif words[0] == "<type>":
                unitType = eval(words[1])
            elif words[0] == "<attackDie>":
                unitADie = eval(words[1])
            elif words[0] == "<defenseDie>":
                unitDDie = eval(words[1])
            elif words[0] == "<move>":
                unitMove = eval(words[1])
            elif words[0] == "<health>":
                unitHealth = eval(words[1])
            elif words[0] == "</unit>":
                unitName.strip()
                #fix panda node thing
                newNode = 1
                newUnit = Unit(unitCost,unitName,unitType,self.name,unitADie,unitDDie,unitMove,unitHealth,newNode)
                self.units.append(newUnit)
                unitName = ""
                unitCost = 0
                unitType = 0
                unitADie = 0
                unitDDie = 0
                unitMove = 0
                unitHealth = 0
            else:
                pass
    def getUnits(self):
        return self.units
        
    def getUpgrades(self):
        return self.upgrades
        
    def getBuildings(self):
        return self.buildings
        
    def getFactionName(self):
        return self.name