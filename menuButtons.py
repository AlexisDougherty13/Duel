import pygame
import os



class Button(pygame.sprite.Sprite):
    def __init__(self, sprite_path, x_pos, y_pos, rect_width, rect_height):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite_path
        self.button_rect = pygame.Rect(x_pos, y_pos, rect_width, rect_height)
        self.image = getImage(sprite_path)
        self.sprite_mask = pygame.mask.from_surface(self.image)



def getImage(path):
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    image = pygame.image.load(canonicalized_path)
    return image