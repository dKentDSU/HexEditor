#the wonderful button class, use it wisely

class Button:

    def __init__(self,xpos,ypos,width,height,image,imageh,handler):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.image = image
        self.imageHover = imageh
        self.buttonHandler = handler
    
    def clicked(x,y):
        #do something with the mouse clicked
        if self.mouseIsOver(x,y):
            self.buttonHandler()
        
    def mouseIsOver(x,y):
        # is mouse over this button?
        # don't know if have to convert from pixel to screen position
        if x > self.xpos and x < (self.xpos + self.width):
            if y > self.ypos and y < (self.ypos + self.width):
                self.image.hide()
                self.imageh.show()
                return True
                
        self.imageh.hide()
        self.image.show()
        return False
        