from direct.showbase.ShowBase import ShowBase
from panda3d.core import Spotlight
from panda3d.core import TransparencyAttrib
from tile import Tile
from country import Country
# import panda node thing

TERRAIN_WATER = 0
TERRAIN_SNOW = 1
TERRAIN_ICE = 2
TERRAIN_PLAINS = 3
TERRAIN_FOREST = 4
TERRAIN_JAGGEDROCKS = 5
TERRAIN_MOUNTAIN = 6
TERRAIN_DESERT = 7
TERRAIN_HILLS = 8

class Map:
    def __init__(self,filename):
        self.height = 0
        self.width = 0
        self.waterheight = 0
        self.countries = []
        self.tileList = []
        self.tileReference = {}
        self.node = render.attachNewNode('BaseMap')
        
        self.snow = loader.loadModel("data/models/snow.bam")
        self.ice = loader.loadModel("data/models/ice.bam")
        self.plains = loader.loadModel("data/models/plains.bam")
        self.forest = loader.loadModel("data/models/forest.bam")
        self.jaggedrocks = loader.loadModel("data/models/jaggedrocks.bam")
        self.mountain = loader.loadModel("data/models/mountains.bam")
        self.desert = loader.loadModel("data/models/desert.bam")
        self.hills = loader.loadModel("data/models/hills.bam")
        self.water = loader.loadModel("data/models/water.bam")
        self.water.setTransparency(TransparencyAttrib.MAlpha)

        self.watertop = loader.loadModel("data/models/watertop.bam")
        self.waterbottom = loader.loadModel("data/models/waterbottom.bam")
        
        render.setShaderAuto()
        
        self.spot = Spotlight('World spot')
        self.spot.setColor((.7,.7,.7,1))
        self.spot.getLens().setFov(180)
        self.spot.getLens().setNearFar(1,10000000)
        self.spotNode = render.attachNewNode(self.spot)
        self.spotNode.setPos(2000,2000,5000)
        self.spotNode.lookAt(self.node)
        render.setLight(self.spotNode)
        
        self.createMap(filename)
        
        self.watertop.reparentTo(self.node)
        self.watertop.setScale(9,9,9)
        self.watertop.setPos((self.width*60)/2,-(self.height*17)/2,5)
        
        self.waterbottom.reparentTo(self.node)
        self.waterbottom.setScale(9,9,9)
        self.waterbottom.setPos((self.width*60)/2,-(self.height*17)/2,1)
        
    def getCountry(self,countryNum):
        return self.countries[countryNum]
        
    def drawMap(self):
        pass
        
    def createMap(self,filename):
        filein = open(filename,"rb")
        countryCounter = 0
        tileCounter = 0
        countryTiles = []
        countryIncome = 0
        
        for line in filein:
            words = line.split()
            if len(words) > 0:
                if words[0] == "<map>":
                    pass
                elif words[0] == "<height>":
                    self.height = eval(words[1])
                elif words[0] == "<width>":
                    self.width = eval(words[1])
                elif words[0] == "<waterheight>":
                    self.waterheight = eval(words[1])
                elif words[0] == "<tile>":
                    terrainType = eval(words[1])
                    newNode = self.node.attachNewNode('terrain'+str(tileCounter))
                    newNode.setTag('tile',str(tileCounter))
                    if terrainType == TERRAIN_WATER:
                        self.water.instanceTo(newNode)
                    elif terrainType == TERRAIN_SNOW:
                        self.snow.instanceTo(newNode)
                    elif terrainType == TERRAIN_ICE:
                        self.ice.instanceTo(newNode)
                    elif terrainType == TERRAIN_PLAINS:
                        self.plains.instanceTo(newNode)
                    elif terrainType == TERRAIN_FOREST:
                        self.forest.instanceTo(newNode)
                    elif terrainType == TERRAIN_JAGGEDROCKS:
                        self.jaggedrocks.instanceTo(newNode)
                    elif terrainType == TERRAIN_MOUNTAIN:
                        self.mountain.instanceTo(newNode)
                    elif terrainType == TERRAIN_DESERT:
                        self.desert.instanceTo(newNode)
                    elif terrainType == TERRAIN_HILLS:
                        self.hills.instanceTo(newNode)
                    x = (tileCounter % self.width)
                    y = (tileCounter / self.width)
                    if y % 2 == 0:
                        newNode.setPos(x*60,-y*17,0)
                    else:
                        newNode.setPos(x*60+30,-y*17,0)
                    newTile = Tile(terrainType,newNode,x,y,tileCounter)
                    self.tileList.append(newTile)
                    tileCounter += 1
                elif words[0] == "<income>":
                    countryIncome = eval(words[1])
                elif words[0] == "<tileNum>":
                    countryTiles.append(self.tileList[eval(words[1])])
                elif words[0] == "</country>":
                    newCountry = Country(countryTiles,countryIncome)
                    self.countries.append(newCountry)
                    countryCounter += 1
                    countryTiles = []
                    countryIncome = 0
                else:
                    pass
        #end loop
        
        for country in range(len(self.countries)):
            for tile in self.countries[country].getTiles():
                x = tile.getX()
                y = tile.getY()
                self.tileReference[(x,y)]=country
        filein.close()
        #end init   
    def getTile(self,x,y):
        #get the tile from the country it is in from spectile
        return self.countries[self.tileReference[(x,y)]].getSpecTile(x,y)
        
    def getPlayerCountries(self,playerNum):
        #return the list of countries that belong to that player
        playerCountries = []
        for country in self.countries:
            if country.getOwner() == playerNum:
                playerCountries.append(country)
        return playerCountries
        
        
    
        
        