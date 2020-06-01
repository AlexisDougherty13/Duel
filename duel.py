import player
import pygame
import os
import time


_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
        

def main():

    screen_width = 1000
    screen_height = 600

    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    
    player1 = player.Player(500, 300, 1, 'fillerSprite.png')
    
    done = False

    while not done:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player1.moveLeft
                    if event.key == pygame.K_d:
                        player1.moveRight
        
        screen.fill((255, 255, 255))
        
        screen.blit(get_image(player1.get_sprite()), (player1.get_xpos(), player1.get_ypos())) #(width, height)
    
        
        pygame.display.flip()
	
main()


# Sources:
# https://nerdparadise.com/programming/pygame/part2