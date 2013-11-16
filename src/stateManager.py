from state import State
#from splashScreenState import SplashScreenState
from mainMenuState import MainMenuState
from gameState import GameState

class StateManager:
    def __init__(self,application,filename):
        self.filename = filename
        # the lists of states, initialize put in list
        self.application = application
        #m = MainMenuState(application)
        #s = SplashScreenState(application)
        g = GameState(application,filename)
        self.stateList = {'game': g}
        # the current state
        self.currentState = self.stateList['game']
        
    def getCurrentState(self):
        return self.currentState
        
    def setCurrentState(self,key):
        self.currentState = self.stateList[key]
        
    def runState(self):
        self.currentState.run()
        
        