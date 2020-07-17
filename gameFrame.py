import pygame
import os
from camera import Camera

#OLD RENDER
#def render(my_sprites, draw_buffer):
    #rects = my_sprites.draw(draw_buffer)
    #pygame.display.update(rects)  # copy rects from buffer to screen

def render(display, screen, player1, player2, entities, camera):
    #imagesDict = dict()
    if camera.getActive() == True:
        offset = camera.getOffset()
    else:
        offset = [0,0]
   
    display.fill((146,244,255))
    #display.blit(getImage("Resources/Images/ScaledBackgroundAutumnForest.png", imagesDict), (0, 0))

    display.blit(player1.image, (player1.rect.x - offset[0], player1.rect.y - offset[1]))
    display.blit(player2.image, (player2.rect.x - offset[0], player2.rect.y - offset[1]))

    for rec in entities:
        newRect = pygame.Rect(rec.left - offset[0], rec.top - offset[1], rec.width, rec.height)
        pygame.draw.rect(display, (255,255,255), newRect)

    screen.blit(display, (0,0))
    pygame.display.update()

def initTwo(current_map):
    display = pygame.Surface((current_map.x_length, current_map.y_length))
    camera = Camera()
    return display, camera
    

#OLD INIT
# def init(player1, player2, current_map, entities, pause_buttons):
#     imagesDict = dict()
#     draw_buffer = pygame.display.set_mode((current_map.x_length, current_map.y_length))

#     #create the background used to restore sprite previous location
#     background = pygame.Surface(draw_buffer.get_size())
#     pygame.draw.rect(background, (255, 255, 255, 255), entities[0])
#     background.blit(getImage("Resources/Images/ScaledBackgroundAutumnForest.png", imagesDict), (0, 0))
    
#     pygame.draw.rect(background, (139, 69, 19), entities[1])
#     pygame.draw.rect(background, (139, 69, 19), entities[2])

#     my_sprites = pygame.sprite.LayeredDirty()  # holds sprites to be drawn
#     initializePauseButtons(pause_buttons)
#     my_sprites.add(player1, player2, pause_buttons["play_button"], pause_buttons["restart_button"], pause_buttons["exit_button"])  # add both to our group
#     my_sprites.clear(draw_buffer, background) # copy background to screen

#     return draw_buffer, my_sprites

def getImage(path, _image_library):
    if path not in _image_library:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path).convert_alpha()
        _image_library[path] = image
    return _image_library[path]

def initializePauseButtons(pause_buttons):
    pause_buttons["play_button"].visible = 0
    pause_buttons["restart_button"].visible = 0
    pause_buttons["exit_button"].visible = 0
    pause_buttons["play_button"].initializeRect()
    pause_buttons["restart_button"].initializeRect()
    pause_buttons["exit_button"].initializeRect()