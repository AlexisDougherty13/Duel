import pygame
import os


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


def getImage(path, _image_library):
    if path not in _image_library:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path).convert_alpha()
        _image_library[path] = image
    return _image_library[path]



