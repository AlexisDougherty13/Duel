import pygame
import os
from camera import Camera
from tile import Tile


def render(display, screen, player1, player2, entities, camera, swords, assets):
    imagesDict = dict()


    offset = camera.getOffset()

   
    #display.fill((146,244,255))

    display.blit(getImage(assets["Background"], imagesDict), (0, 0))

    display.blit(player1.image, (player1.rect.x - offset[0], player1.rect.y - offset[1]))
    display.blit(player2.image, (player2.rect.x - offset[0], player2.rect.y - offset[1]))

    for entity in entities:
        if not entity.getEffects()["Invisible"]:
            display.blit(getImage(entity.getImagePath(), imagesDict), (entity.getRect().left - offset[0], entity.getRect().top - offset[1]))
       
    for sword in swords:
        display.blit(pygame.transform.rotate(sword.image, sword.getState("current_r")), (sword.rect.x - offset[0], sword.rect.y - offset[1]))
        #display.blit(pygame.transform.rotate(sword.image, 25), (sword.rect.x - offset[0], sword.rect.y - offset[1]))
    screen.blit(display, (0,0))
    pygame.display.update()

def init(current_map):
    display = pygame.Surface((current_map.x_length, current_map.y_length))
    camera = Camera()
    return display, camera
    
def getImage(path, _image_library):
    if path not in _image_library:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path).convert_alpha()
        _image_library[path] = image
    return _image_library[path]
