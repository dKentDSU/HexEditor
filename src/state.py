#base State class used by all other state classes

class State:
    def __init__(self):
        pass
    #abstract class

    def drawState(self,application):
    #virtual class stub
        raise NotImplementedError()
    def gameLogic(self):
    #virual method stub
        raise NotImplementedError()

    def drawWorld(self):
    #virtual method stub
        raise NotImplementedError()

    def drawUI(self):
    #virtual method stub
        raise NotImplementedError()
	
	