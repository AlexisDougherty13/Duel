import pygame

#camera object allows for scrolling and centering on one player
class Camera:
   def __init__(self):
      self._offset = [0,0]
      self._active = False
      self._screen_rect = pygame.Rect(-100, 0, 1000, 2000)

   def getOffset(self):
      if(self._active):
         self._offset[0] += (self._target.rect.x - self._offset[0] - 370)/20
      return self._offset

   def setTarget(self, target):
      self._target = target

   def setActive(self, active):
      self._active = active
   
   def getActive(self):
      return self._active

   def getTarget(self):
      return self._target

   def getScreenRect(self):
      return self._screen_rect
	
#Source: https://www.youtube.com/watch?v=5q7tmIlXROg&t=262s