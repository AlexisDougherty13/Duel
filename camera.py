#https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame
#plan- camera class- stores current settings and calculates offset, screen updates in gameFrame
#questions- how exactly is everything rendered, can we do it more efficientily
#derive player as a sprite?
#add yourself to the trello

import pygame

class Camera:
    def __init__(self, width, height):
	    self.state = pygame.Rect(0, 0, width, height)
		
    def cameraMovement(self, target_rect): #method that determines centering on target
	    print("hello")
	
    def apply(self, target):
	    return target.rect.move(self.state.topleft)

    def update(self, target):
	    sefl.state = self.cameraMovement(target.rect)
	
#Source: https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame