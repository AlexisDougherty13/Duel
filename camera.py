import pygame

#camera object allows for scrolling and centering on one player
class Camera:
    def __init__(self, cameraMovement, width, height):
        self.state = pygame.Rect(0, 0, width, height)
        self.cameraMovement = cameraMovement
		
    
	
    def apply(self, target):
	    return target.rect.move(self.state.topleft)

    def update(self, target):
	    self.state = self.cameraMovement(self.state, target.rect)
	
	
#Source: https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame