import player
import pygame
import os
import time

# 0 means no sword, 3 is high, 2 is med, 1 is low sword

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
    
    player1 = player.Player(500, 300, 1, 2, False, 'FillerSpriteMed.png')
    
    done = False

    while not done:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player1.move_left
                    if event.key == pygame.K_d:
                        player1.move_right
                    if event.key == pygame.K_DOWN:
                        if(player1.getSwordHeight > 1):
                            player1.lower_sword
                            if(player1.sword_height == 1 and player1.direction_facing == 1):
                                player1.sprite = "FillerSpriteLow.png"
                            if(player1.sword_height == 2 and player1.direction_facing == 1):
                                player1.sprite = "FillerSpriteMed.png"
                            if(player1.sword_height == 3 and player1.direction_facing == 1):
                                player1.sprite = "FillerSpriteHigh.png"
                            if(player1.sword_height == 1 and player1.direction_facing == 0):
                                player1.sprite = "FillerSpriteLowR.png"
                            if(player1.sword_height == 2 and player1.direction_facing == 0):
                                player1.sprite = "FillerSpriteMedR.png"
                            if(player1.sword_height == 3 and player1.direction_facing == 0):
                                player1.sprite = "FillerSpriteHighR.png"
                    if event.key == pygame.K_UP:
                        if(player1.getSwordHeight > 0):
                            player1.raise_sword
                            if(player1.sword_height == 1 and player1.direction_facing == 1):
                                player1.sprite = "FillerSpriteLow.png"
                            if(player1.sword_height == 2 and player1.direction_facing == 1):
                                player1.sprite = "FillerSpriteMed.png"
                            if(player1.sword_height == 3 and player1.direction_facing == 1):
                                player1.sprite = "FillerSpriteHigh.png"
                            if(player1.sword_height == 1 and player1.direction_facing == 0):
                                player1.sprite = "FillerSpriteLowR.png"
                            if(player1.sword_height == 2 and player1.direction_facing == 0):
                                player1.sprite = "FillerSpriteMedR.png"
                            if(player1.sword_height == 3 and player1.direction_facing == 0):
                                player1.sprite = "FillerSpriteHighR.png"
                            
        
        screen.fill((255, 255, 255))
        
        screen.blit(get_image(player1.sprite), (player1.getXPos(), player1.getYPos())) #(width, height)
    
        
        pygame.display.flip()
	
main()


# Sources:
# https://nerdparadise.com/programming/pygame/part2