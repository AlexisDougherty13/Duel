import pygame
import os
from camera import Camera 


def render(my_sprites, draw_buffer):
    rects = my_sprites.draw(draw_buffer)
    pygame.display.update(rects)  # copy rects from buffer to screen
    imagesDictionary = dict()
    return 5

def init():
    camera = Camera(gameFrame.cameraMovement, current_map.x_length, current_map.y_length) # initializes camera with level's width and height

    draw_buffer = pygame.display.set_mode((current_map.x_length, current_map.y_length))

    #create the background used to restore sprite previous location
    background = pygame.Surface(draw_buffer.get_size())
    background.blit(gameFrame.getImage("Resources/Images/UF_Background.png"), (0, 0))
    pygame.draw.rect(background, (255, 0, 0), entities[0])
    pygame.draw.rect(background, (255, 0, 255), entities[1])
    pygame.draw.rect(background, (255, 0, 255), entities[2])
    my_sprites = pygame.sprite.LayeredDirty()  # holds sprites to be drawn
    my_sprites.add(player1, player2)  # add both to our group
    my_sprites.clear(draw_buffer, background) # copy background to screen

def cameraMovement(camera, target_rect): #method that determines centering on target
        l, t, _, _ = target_rect # l = left,  t = top
        _, _, w, h = camera     # w = width, h = height
        return pygame.Rect(-l+(.5 * camera.width), -t+(.5 * camera.height), w, h)
		
def getImage(path, _image_library):
    if path not in _image_library:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path).convert_alpha()
        _image_library[path] = image
    return _image_library[path]



