import pygame

#camera object allows for scrolling and centering on one player
class Camera:
   #GET SPECIFIC OFFSETS FOR SPECIFICATION
   def __init__(self):
      self._offset = [0,0]
      self._active = True

   def getOffset(self):
      self._offset[0] += .25
      #self._offset[0] += (self._target.rect.x-self._offset[0]-152)/20
      #self._offset[1] += (self._target.rect.y-self._offset[1]-106)/20
      return self._offset

   def setTarget(self, target):
      self._target = target

   def setActive(self, active):
      self._active = active
   
   def getActive(self):
      return self._active
	
#Source: https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame