import pygame
import os
from camera import Camera 


def render(my_sprites, draw_buffer):
    rects = my_sprites.draw(draw_buffer)
    pygame.display.update(rects)  # copy rects from buffer to screen
	
    return 5


def getImage(path):
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    image = pygame.image.load(canonicalized_path).convert_alpha()
    return image


def swordPositioning(player):
    if player.sword_height == 1 and player.direction_facing == 1:
        player.sprite = player.image_dict["Resources/Images/sword_low_r"]
    if player.sword_height == 2 and player.direction_facing == 1:
        player.sprite = player.image_dict["Resources/Images/sword_med_r"]
    if player.sword_height == 3 and player.direction_facing == 1:
        player.sprite = player.image_dict["Resources/Images/sword_high_r"]
    if player.sword_height == 1 and player.direction_facing == 0:
        player.sprite = player.image_dict["Resources/Images/sword_low_l"]
    if player.sword_height == 2 and player.direction_facing == 0:
        player.sprite = player.image_dict["Resources/Images/sword_med_l"]
    if player.sword_height == 3 and player.direction_facing == 0:
        player.sprite = player.image_dict["Resources/Images/sword_high_l"]
