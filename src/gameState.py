from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TransparencyAttrib, TextNode, Vec4
from state import State
from map import Map
from tile import Tile
from button import Button
from faction import Faction
from player import Player
import time
import math
import random

COLORS = [ Vec4(1,.5,.5,.01) , Vec4(.5,.5,1,.01) ]
FACTIONS = ["data/maps/humanfaction.xml"]

class GameState(State):
    #hard code for now, pass map filename in later to pick map files
    def __init__(self,application,filename):
        self.application = application
        self.purchaseMode = False
        self.enter = False
        self.filename = filename

        players = [Player(0,100,"Human",5,10),Player(1,100,"Human",8,30)]
        
        self.initializeState(players)

    def initializeState(self,players):
        self.clicked = False
        self.selectedTile = None
        self.numPlayers = 2
        self.currentPlayer = 0
        self.turn = 1
        
        self.map = Map(self.filename)        
            
        self.highlight = loader.loadModel('data/models/highlight.egg')
        self.highlight.reparentTo(render)
        self.highlight.hide()
        
        self.highlight.setTransparency(TransparencyAttrib.MAlpha)
        self.highlight.setAlphaScale(.5)
        
        self.detatime = 0
        self.starttime = time.time()
        self.lasttime = time.time()
        
        
        
        
        
    def run(self):
        taskMgr.add(self.mainLoop,'GameLoop')
        
    def mainLoop(self,task):
        self.highlight.setAlphaScale(1.5+math.sin(time.time()))
    
        self.handleInput()

        return task.cont
        
    def handleInput(self):
        currenttime = time.time()
        self.deltatime = currenttime - self.lasttime
        self.lasttime = currenttime
    
        if (self.application.keyMap["camLeft"] != 0):
            self.application.camera.setX(self.application.camera.getX()-150*self.deltatime)
            if self.application.camera.getX() < 15:
                self.application.camera.setX(15)
        if (self.application.keyMap["camRight"] != 0):
            self.application.camera.setX(self.application.camera.getX()+150*self.deltatime)
            if self.application.camera.getX() > 525:
                self.application.camera.setX(525)
        if (self.application.keyMap["camUp"] != 0):
            self.application.camera.setY(self.application.camera.getY()+150*self.deltatime)
            if self.application.camera.getY() > -230:
                self.application.camera.setY(-230)
        if (self.application.keyMap["camDown"] != 0):
            self.application.camera.setY(self.application.camera.getY()-150*self.deltatime)
            if self.application.camera.getY() < -800:
                self.application.camera.setY(-800)
        if (self.application.keyMap["camZoomIn"] != 0):
            self.application.camera.setZ(self.application.camera.getZ()-100*self.deltatime)
            if self.application.camera.getZ() < 100:
                self.application.camera.setZ(100)
        if (self.application.keyMap["camZoomOut"] != 0):
            self.application.camera.setZ(self.application.camera.getZ()+100*self.deltatime)
            if self.application.camera.getZ() > 200:
                self.application.camera.setZ(200)
         
        if base.mouseWatcherNode.hasMouse():
            mpos = base.mouseWatcherNode.getMouse()
            mouseX = base.win.getXSize()/2+(mpos.getX()*base.win.getXSize()/2)
            mouseY = (base.win.getYSize()/2-(mpos.getY()*base.win.getYSize()/2))
            
            if mouseX >= base.win.getXSize()-20 and mouseX <= base.win.getXSize():
                self.application.camera.setX(self.application.camera.getX()+150*self.deltatime)
                if self.application.camera.getX() > 525:
                    self.application.camera.setX(525)
            if mouseX >= 0 and mouseX <= 20:
                self.application.camera.setX(self.application.camera.getX()-150*self.deltatime)
                if self.application.camera.getX() < 15:
                    self.application.camera.setX(15)
            if mouseY >= 0 and mouseY <= 20:
                self.application.camera.setY(self.application.camera.getY()+150*self.deltatime)
                if self.application.camera.getY() > -230:
                    self.application.camera.setY(-230)
            if mouseY >= base.win.getYSize()-20 and mouseY <= base.win.getYSize():
                self.application.camera.setY(self.application.camera.getY()-150*self.deltatime)
                if self.application.camera.getY() < -800:
                    self.application.camera.setY(-800)
                    
        if (self.application.keyMap["left_click"]!=0):
            if self.clicked == False:
                self.leftClick()
                self.clicked = True
        if (self.application.keyMap["left_click"]==0):
            self.clicked = False
            
            
        if (self.application.keyMap["zero"]!=0):
            self.selectedTile.node.remove()
            node = self.map.node.attachNewNode('terrain'+str(self.selectedTile.id))
            node.setTag('tile',str(self.selectedTile.id))
            y = self.selectedTile.getY()
            x = self.selectedTile.getX()
            self.selectedTile.terrainType = 0
            if y % 2 == 0:
                node.setPos(x*60,-y*17,0)
            else:
                node.setPos(x*60+30,-y*17,0)
            self.map.water.instanceTo(node)
            self.selectedTile.node = node
            
            
        if (self.application.keyMap["one"]!=0):
            self.selectedTile.node.remove()
            node = self.map.node.attachNewNode('terrain'+str(self.selectedTile.id))
            node.setTag('tile',str(self.selectedTile.id))
            self.selectedTile.terrainType = 1
            y = self.selectedTile.getY()
            x = self.selectedTile.getX()
            if y % 2 == 0:
                node.setPos(x*60,-y*17,0)
            else:
                node.setPos(x*60+30,-y*17,0)
            self.map.snow.instanceTo(node)
            self.selectedTile.node = node
            
        if (self.application.keyMap["two"]!=0):
            self.selectedTile.node.remove()
            node = self.map.node.attachNewNode('terrain'+str(self.selectedTile.id))
            node.setTag('tile',str(self.selectedTile.id))
            self.selectedTile.terrainType = 2
            y = self.selectedTile.getY()
            x = self.selectedTile.getX()
            if y % 2 == 0:
                node.setPos(x*60,-y*17,0)
            else:
                node.setPos(x*60+30,-y*17,0)
            self.map.ice.instanceTo(node)
            self.selectedTile.node = node
            
        if (self.application.keyMap["three"]!=0):
            self.selectedTile.node.remove()
            node = self.map.node.attachNewNode('terrain'+str(self.selectedTile.id))
            node.setTag('tile',str(self.selectedTile.id))
            self.selectedTile.terrainType = 3
            y = self.selectedTile.getY()
            x = self.selectedTile.getX()
            if y % 2 == 0:
                node.setPos(x*60,-y*17,0)
            else:
                node.setPos(x*60+30,-y*17,0)
            self.map.plains.instanceTo(node)
            self.selectedTile.node = node
            
        if (self.application.keyMap["four"]!=0):
            self.selectedTile.node.remove()
            node = self.map.node.attachNewNode('terrain'+str(self.selectedTile.id))
            node.setTag('tile',str(self.selectedTile.id))
            self.selectedTile.terrainType = 4
            y = self.selectedTile.getY()
            x = self.selectedTile.getX()
            if y % 2 == 0:
                node.setPos(x*60,-y*17,0)
            else:
                node.setPos(x*60+30,-y*17,0)
            self.map.forest.instanceTo(node)
            self.selectedTile.node = node
            
        if (self.application.keyMap["five"]!=0):
            self.selectedTile.node.remove()
            node = self.map.node.attachNewNode('terrain'+str(self.selectedTile.id))
            node.setTag('tile',str(self.selectedTile.id))
            self.selectedTile.terrainType = 5
            y = self.selectedTile.getY()
            x = self.selectedTile.getX()
            if y % 2 == 0:
                node.setPos(x*60,-y*17,0)
            else:
                node.setPos(x*60+30,-y*17,0)
            self.map.jaggedrocks.instanceTo(node)
            self.selectedTile.node = node
            
        if (self.application.keyMap["six"]!=0):
            self.selectedTile.node.remove()
            node = self.map.node.attachNewNode('terrain'+str(self.selectedTile.id))
            node.setTag('tile',str(self.selectedTile.id))
            self.selectedTile.terrainType = 6
            y = self.selectedTile.getY()
            x = self.selectedTile.getX()
            if y % 2 == 0:
                node.setPos(x*60,-y*17,0)
            else:
                node.setPos(x*60+30,-y*17,0)
            self.map.mountain.instanceTo(node)
            self.selectedTile.node = node
            
            
        if (self.application.keyMap["seven"]!=0):
            self.selectedTile.node.remove()
            node = self.map.node.attachNewNode('terrain'+str(self.selectedTile.id))
            node.setTag('tile',str(self.selectedTile.id))
            self.selectedTile.terrainType = 7
            y = self.selectedTile.getY()
            x = self.selectedTile.getX()
            if y % 2 == 0:
                node.setPos(x*60,-y*17,0)
            else:
                node.setPos(x*60+30,-y*17,0)
            self.map.desert.instanceTo(node)
            self.selectedTile.node = node
            
            
        if (self.application.keyMap["eight"]!=0):
            self.selectedTile.node.remove()
            node = self.map.node.attachNewNode('terrain'+str(self.selectedTile.id))
            node.setTag('tile',str(self.selectedTile.id))
            self.selectedTile.terrainType = 8
            y = self.selectedTile.getY()
            x = self.selectedTile.getX()
            if y % 2 == 0:
                node.setPos(x*60,-y*17,0)
            else:
                node.setPos(x*60+30,-y*17,0)
            self.map.hills.instanceTo(node)
            self.selectedTile.node = node
            
        if (self.application.keyMap["endTurn"]!=0):
            if self.enter == False:
                self.createFile()
                self.enter = True
                
        if (self.application.keyMap["endTurn"]==0):
            self.enter = False
    
    def leftClick(self):
        mpos = base.mouseWatcherNode.getMouse()
        self.application.clickerRay.setFromLens(base.camNode,mpos.getX(),mpos.getY())
        self.application.traverser.traverse(render)
        mouseX = base.win.getXSize()/2+(mpos.getX()*base.win.getXSize()/2)
        mouseY = (base.win.getYSize()/2-(mpos.getY()*base.win.getYSize()/2))
        
        if self.application.clickHandler.getNumEntries() > 0 and not self.purchaseMode:
            self.application.clickHandler.sortEntries()    
            selected = self.application.clickHandler.getEntry(0).getIntoNodePath()
            selected = selected.findNetTag('tile')
            if not selected.isEmpty():
                tile = self.map.tileList[eval(str(selected)[22:])]
                self.selectedTile = tile
                self.highlight.show()
                self.highlight.setPos(tile.node.getX(),tile.node.getY(),tile.node.getZ())
                
    def createFile(self):
        fout = open('data/maps/mainmap.xml','w')
        fout.write('<map>\n')
        fout.write('<height> 38 </height>\n')
        fout.write('<width> 9 </width>\n')
        fout.write('<tileList>\n')
        for tile in self.map.tileList:
            fout.write('<tile> '+str(tile.terrainType)+' </tile>\n')
        fout.write('</tileList>\n')
        for country in self.map.countries:
            fout.write('<country>\n')
            fout.write('<income> '+str(country.income)+' </income>\n')
            for tile in country.tiles:
                fout.write('<tileNum> '+str(tile.id)+' </tileNum>\n')
            fout.write('</country>\n')
        fout.write('</map>')
        print "File Saved"