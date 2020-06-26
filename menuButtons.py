import pygame



class Button(pygame.sprite.Sprite):
    def __init__(self, sprite_path, x_pos, y_pos, rect_width, rect_height):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite_path
        self.button_rect = pygame.Rect(x_pos, y_pos, rect_width, rect_height)

