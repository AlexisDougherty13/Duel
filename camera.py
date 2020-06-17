import pygame

#camera object allows for scrolling and centering on one player
class Camera:
    def __init__(self, width, height):
	    self.state = pygame.Rect(0, 0, width, height)
		
    def cameraMovement(self, target_rect): #method that determines centering on target
        l, t, _, _ = target_rect # l = left,  t = top
        _, _, w, h = self     # w = width, h = height
        return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)
	
    def apply(self, target):
	    return target.rect.move(self.state.topleft)

    def update(self, target):
	    self.state = self.cameraMovement(target.rect)
	
	
#Source: https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame