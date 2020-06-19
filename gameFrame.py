import pygame
import os
from camera import Camera 


<<<<<<< HEAD
def render(screen, player1, player2, current_map):
    imagesDictionary = dict()
    screen.fill((255, 255, 255))
    screen.blit(getImage("Resources/Images/UF_Background.png", imagesDictionary), (0, 0))
    entities = current_map.getCollidableEntities()
    pygame.draw.rect(screen, (255, 0, 0), entities[0])
    pygame.draw.rect(screen, (255, 0, 255), entities[1])
    pygame.draw.rect(screen, (255, 0, 255), entities[2])
    screen.blit(getImage(player1.sprite, imagesDictionary),
                (player1.player_rect.x, player1.player_rect.y))  # (width, height)
    screen.blit(getImage(player2.sprite, imagesDictionary),
                (player2.player_rect.x, player2.player_rect.y))

    pygame.display.update()
=======
def render(my_sprites, draw_buffer):
    rects = my_sprites.draw(draw_buffer)
    pygame.display.update(rects)  # copy rects from buffer to screen
	
    return 5
>>>>>>> master

def cameraMovement(camera, target_rect): #method that determines centering on target
        l, t, _, _ = target_rect # l = left,  t = top
        _, _, w, h = camera     # w = width, h = height
        return pygame.Rect(-l+(.5 * camera.width), -t+(.5 * camera.height), w, h)
		
def getImage(path):
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    image = pygame.image.load(canonicalized_path).convert_alpha()
    return image



