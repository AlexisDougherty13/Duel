import time

#change these
shift_size = 0.6
hit_box_width = 102
hit_box_height = 140

# 102x203

class Player:
    def __init__(self, x_pos, y_pos, direction_facing, sword_height, is_ghost, sprite):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._direction_facing = direction_facing
        self._sword_height = sword_height
        self._is_ghost = is_ghost
        self._sprite = sprite


        
    def getXPos(self):
        return self._x_pos
        
    def setXPos(self, new_x_pos):
        self._x_pos = new_x_pos
        
    def getYPos(self):
        return self._y_pos
        
    def setYPos(self, new_y_pos):
        self._y_pos = new_y_pos
        
    def getDirectionFacing(self):
        return self._direction_facing
        
    def switchDirection(self):
        if(self._x_pos):
            self._x_pos = False
        else:
            self._x_pos = True
        
    # 0 means no sword, 3 is high, 2 is med, 1 is low sword
    def getSwordHeight(self):
        return self._sword_height
        
    def setSwordHeight(self, new_pos):
        self._sword_height = new_pos
        
    def getIsGhost(self):
        return self._is_ghost
        
    def setIsGhost(self):
        if(self._is_ghost):
            self._is_ghost = False
        else:
            self._is_ghost = True


        
    def getSprite(self):
        return self._sprite
        
    def setSprite(self, sprite):
        self._sprite = sprite  
        #print("New: ", self._sprite)
        
    #def insert_sting_middle(self, str, word):
        #return str[:2] + word + str[2:]
        
    #def reverseImage(self):
        #if_r = self._sprite.find("R")
        #if(if_r == -1):
            #self._sprite = self.insert_string_middle(self._sprite, "R")
            #print(self._sprite)
       
    def moveLeft(self, time):
        global shift_size
        self._x_pos = self._x_pos - shift_size
        if time>=0.25:
            self._direction_facing = 0
            self._sprite = "FillerSpriteR.png"
        #self.reverseImage()
            
        
    def moveRight(self, time):
        global shift_size
        self._x_pos = self._x_pos + shift_size
        if time>=0.25:
            self._direction_facing = 1
            self._sprite = "FillerSpriteL.png"
        #reverseImage()
            
           
    # 0 means no sword, 3 is high, 2 is med, 1 is low sword
    def raiseSword(self):
        if(self._sword_height >= 1 and self._sword_height < 3):
            self._sword_height += 1
            
    def lowerSword(self):
        if(self._sword_height <= 3 and self._sword_height > 1):
            self._sword_height -= 1
            
    def duck(self):
        global hit_box_height
        hit_box_height /= 2
        
    def standUp(self):
        global hit_box_height
        hit_box_height *= 2
        
    x_pos = property(getXPos, setXPos)
    y_pos = property(getYPos, setYPos)
    direction_facing = property(getDirectionFacing, switchDirection)
    sword_height = property(getSwordHeight, setSwordHeight)
    is_ghost = property(getIsGhost, setIsGhost)
    sprite = property(getSprite, setSprite)
    
    move_left = property(moveLeft)
    move_right = property(moveRight)
    raise_sword = property(raiseSword)
    lower_sword = property(lowerSword)
    duck = property(duck)
    standUp = property(standUp)


# Sources:
# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-16.php