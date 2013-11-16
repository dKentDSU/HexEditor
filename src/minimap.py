from button import Button

class MiniMap(Button):
    def __init__(self,xpos,ypos,width,height,image,imageh,handler):
        Button.__init__(self,xpos,ypos,width,height,image,imageh,handler)
        # not sure if this is how it should go with minimap
        
    
    def clicked(x,y):
        #do something with the mouse clicked
        # not sure what to do with the ratios and stuff
        if self.mouseIsOver(x,y):
            self.buttonHandler(x,y)
        
        
    def mouseIsOver(x,y):
        # do something when hovered over
        if x > self.xpos and x < (self.xpos + self.width):
            if y > self.ypos and y < (self.ypos + self.width):
                return True
        return False
        