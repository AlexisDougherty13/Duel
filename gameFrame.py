import pygame
import os
from camera import Camera 


def render(my_sprites, draw_buffer):
    rects = my_sprites.draw(draw_buffer)
    pygame.display.update(rects)  # copy rects from buffer to screen
	
    return 5

def cameraMovement(camera, target_rect): #method that determines centering on target
        l, t, _, _ = target_rect # l = left,  t = top
        _, _, w, h = camera     # w = width, h = height
        return pygame.Rect(-l+(.5 * camera.width), -t+(.5 * camera.height), w, h)
		
def getImage(path):
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    image = pygame.image.load(canonicalized_path).convert_alpha()
    return image



