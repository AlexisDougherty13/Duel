import time

class Player:
    def __init__(self, xpos, ypos, directionFacing, sprite):
        self._xpos = xpos
        self._ypos = ypos
        self._directionFacing = directionFacing
        self._sprite = sprite
        
    def get_xpos(self):
        return self._xpos
        
    def set_xpos(self, newXPos):
        self._xpos = newXPos
        
    def get_ypos(self):
        return self._ypos
        
    def set_ypos(self, newYPos):
        self._ypos = newYPos
        
    def get_directionFacing(self):
        return self.__directionFacing
        
    def switchDirection(self):
        if(self._xpos):
            self._xpos = False
        else:
            self._xpos = True
        
    def get_sprite(self):
        return self._sprite
        
    def set_sprite(self, sprite):
        self._sprite = sprite  
       
    def moveLeft(self):
        if(self._directionFacing == 0):
            self._xpos = self._xpos - 50
        else:
            self._directionFacing = 0
        
    def moveRight(self):
        if(self._directionFacing == 1):
            self._xpos = self._xpos + 50
        else:
            self._directionFacing = 1
        
    xpos = property(get_xpos, set_xpos)
    ypos = property(get_ypos, set_ypos)
    directionFacing = property(get_directionFacing, switchDirection)
    sprite = property(get_sprite, set_sprite)
    
    moveLeft = property(moveLeft)
    moveRight = property(moveRight)
