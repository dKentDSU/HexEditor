from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, AntialiasAttrib
from panda3d.core import Vec4
from panda3d.core import CollisionHandlerQueue, CollisionTraverser, CollisionNode, GeomNode, CollisionRay
from panda3d.core import AmbientLight

import sys
from stateManager import StateManager

FULLSCREEN = '1'
SCREEN_X = '1600'
SCREEN_Y = '900'


class Application(ShowBase):
    def __init__(self,filename):
        self.filename = filename
        self.keyMap = {}

        self.initialConfiguration()
        self.keyBindings()
        self.setupClickCollision()
        
        self.createCamera()
        self.initialLighting()
        
        self.stateManager = StateManager(self,filename)
        self.stateManager.runState()
        
    def initialLighting(self):
        alight = render.attachNewNode(AmbientLight("Ambient"))
        alight.node().setColor(Vec4(.5,.5,.5,1))
        render.setLight(alight) 
        
    def createCamera(self):
        base.disableMouse() 
        self.cameratarget = self.render.attachNewNode('Camera Target')
        self.camera.setPos(200,-400,200)
        self.cameratarget.setPos(200,-200,0)
        self.camera.lookAt(self.cameratarget)
        
    def setupClickCollision(self):
        self.clickHandler = CollisionHandlerQueue()
        self.traverser = CollisionTraverser('ClickTraverser')
        base.cTrave = self.traverser
        self.clickerNode = CollisionNode('mouseClick')
        self.clickerNodePoint = self.camera.attachNewNode(self.clickerNode)
        self.clickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.clickerRay = CollisionRay()
        self.clickerNode.addSolid(self.clickerRay)
        self.traverser.addCollider(self.clickerNodePoint,self.clickHandler)
        #self.traverser.showCollisions(render)                                                                           # Uncomment to view Collisions
        
    def initialConfiguration(self):
        loadPrcFileData('', 'fullscreen '+FULLSCREEN)
        loadPrcFileData('', 'win-size '+SCREEN_X+" "+SCREEN_Y)
        loadPrcFileData('', 'framebuffer-multisample 1')
        loadPrcFileData('', 'multisamples 2')
        loadPrcFileData('', 'compressed-textures 1')
        ShowBase.__init__(self)
        render.setAntialias(AntialiasAttrib.MAuto)
        base.win.setClearColor(Vec4(0,0,0,1))
        
    def keyBindings(self):
        self.keyMap = {
            'camUp':0,
            'camDown':0,
            'camLeft':0,
            'camRight':0,
            'camRotateLeft':0,
            'camRotateRight':0,
            'camZoomIn':0,
            'camZoomOut':0,
            'endTurn':0,
            'focusTile':0,
            'focusBase':0,
            'left_click':0,
            'zero':0,
            'one':0,
            'two':0,
            'three':0,
            'four':0,
            'five':0,
            'six':0,
            'seven':0,
            'eight':0,
        }
        
        #self.accept('button',self.setKey,['key',value])
        self.accept('escape',sys.exit)
        self.accept('w',self.setKey,['camUp',1])
        self.accept('w-up',self.setKey,['camUp',0])
        self.accept('s',self.setKey,['camDown',1])
        self.accept('s-up',self.setKey,['camDown',0])
        self.accept('a',self.setKey,['camLeft',1])
        self.accept('a-up',self.setKey,['camLeft',0])
        self.accept('d',self.setKey,['camRight',1])
        self.accept('d-up',self.setKey,['camRight',0])
        self.accept('q',self.setKey,['camRotateLeft',1])
        self.accept('q-up',self.setKey,['camRotateLeft',0])
        self.accept('e',self.setKey,['camRotateRight',1])
        self.accept('e-up',self.setKey,['camRotateRight',0])
        self.accept('r',self.setKey,['camZoomIn',1])
        self.accept('r-up',self.setKey,['camZoomIn',0])
        self.accept('f',self.setKey,['camZoomOut',1])
        self.accept('f-up',self.setKey,['camZoomOut',0])
        self.accept('enter',self.setKey,['endTurn',1])
        self.accept('enter-up',self.setKey,['endTurn',0])
        self.accept('space',self.setKey,['focusTile',1])
        self.accept('space-up',self.setKey,['focusTile',0])
        self.accept('b',self.setKey,['focusBase',1])
        self.accept('b-up',self.setKey,['focusBase',0])
        
        self.accept('0',self.setKey,['zero',1])
        self.accept('0-up',self.setKey,['zero',0])
        self.accept('1',self.setKey,['one',1])
        self.accept('1-up',self.setKey,['one',0])
        self.accept('2',self.setKey,['two',1])
        self.accept('2-up',self.setKey,['two',0])
        self.accept('3',self.setKey,['three',1])
        self.accept('3-up',self.setKey,['three',0])
        self.accept('4',self.setKey,['four',1])
        self.accept('4-up',self.setKey,['four',0])
        self.accept('5',self.setKey,['five',1])
        self.accept('5-up',self.setKey,['five',0])
        self.accept('6',self.setKey,['six',1])
        self.accept('6-up',self.setKey,['six',0])
        self.accept('7',self.setKey,['seven',1])
        self.accept('7-up',self.setKey,['seven',0])
        self.accept('8',self.setKey,['eight',1])
        self.accept('8-up',self.setKey,['eight',0])
        
        self.accept('mouse1',self.setKey, ['left_click',1])
        self.accept('mouse1-up',self.setKey, ['left_click',0])
        
    def setKey(self,key,value):
        self.keyMap[key] = value
        