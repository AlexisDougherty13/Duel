import pygame


def startScreen():
    window_size = (1000, 600)
    pygame.init()
    screen = pygame.display.set_mode(window_size, 0, 32)
    return screen