"""
.. module:: gameEngine
.. synopsis: The Game's driving loop, This is where the whole game will be run from
"""
import mapSelectionList
import sys
from player import Player
import pygame
from playerSkinsList import getSkin
import gameFrame
from swordHitBoxes import getSwordLine
from time import time
import mainMenuFrame
from camera import Camera
import math


# temp data, should not be here for long....
# Player 1 meta info, store inputs and send to the player object
p1_meta_info = {
    "up": False,  # if the player is moving in this direction
    "left": False,  # if the player is moving in this direction
    "right": False,  # if the player is moving in this direction
    "down": False,  # if the player is moving in this direction
    "sword_movement": 0, #if the sword is moving up its +1 if its moving down its -1 if not moving its 0
    "sword_down": False,  # down due to movement greater than 1/4sec
    "movement_clock": 0,  # time in milliseconds in which the player has moved without stopping
    "attack": False
}

    # Player 2 meta info, store inputs and send to the player object
p2_meta_info = {
    "up": False,  # if the player is moving in this direction
    "left": False,  # if the player is moving in this direction
    "right": False,  # if the player is moving in this direction
    "down": False,  # if the player is moving in this direction
    "sword_movement": 0,  # if the sword is moving up its +1 if its moving down its -1 if not moving its 0
    "sword_down": False,  # down due to movement greater than 1/4sec
    "movement_clock": 0,  # time in milliseconds in which the player has moved without stopping
    "attack": False
}

def mainMenu(screen):  # TODO Call Main Menu Frame instead and have it call startGame
    mainMenuFrame.mainMenu(screen)


def adjustPlayer(player, aspect, value):
    if player == 1:
        p1_meta_info[aspect] = value
    elif player == 2:
        p2_meta_info[aspect] = value

# :param Requires a Screen Objects (Created in the main passed to main menu),
#  an int map_selection to determine what map to put on,
# and 2 string skin_selection to determine what skins the players choose
def startGame(screen, map_selection, skin_selection1, skin_selection2):

    current_map = mapSelectionList.selectMap(map_selection)  # returns a child of the map class

    entities = current_map.getCollidableEntities()

    player1 = Player((300, 100), 1, 2, False, True, 'Resources/Images/MontoyaMedR.png',
                     getSkin(skin_selection1))  # Initializes player1
    player2 = Player((400, 100), 1, 2, False, False, 'Resources/Images/MontoyaMedL.png',
                     getSkin(skin_selection2))  # Initializes player2
	
    draw_buffer, my_sprites = gameFrame.init(player1, player2, current_map, entities)

    clock = pygame.time.Clock()

    print("starting")

    player1_y_vel = 0 #temp will be altered soon
    player2_y_vel = 0  # temp will be altered soon

    active_match = True
    while active_match:
        # Delta time is implemented to help make sure that player's models will move at the same speed regardless of monitor refresh rate and processor speed.
        # Could use further optimizing and troubleshooting.
        clock.tick(90)

        for event in pygame.event.get():
            # What to do on quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Pressed a key so perform said action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    adjustPlayer(1, "right", True)
                elif event.key == pygame.K_a:
                    adjustPlayer(1, "left", True)
                if event.key == pygame.K_SPACE:
                    adjustPlayer(1, "up", True)
                if event.key == pygame.K_s:
                    adjustPlayer(1, "sword_movement", -1)
                elif event.key == pygame.K_w:
                    adjustPlayer(1, "sword_movement", 1)
                if event.key == pygame.K_f:
                    adjustPlayer(1, "attack", True)
                    player1.setIsAttacking(True)
                if event.key == pygame.K_LEFT:
                    adjustPlayer(2, "left", True)
                elif event.key == pygame.K_RIGHT:
                    adjustPlayer(2, "right", True)
                if event.key == pygame.K_RSHIFT:
                    adjustPlayer(2, "up", True)
                if event.key == pygame.K_DOWN:
                    adjustPlayer(2, "sword_movement", -1)
                elif event.key == pygame.K_UP:
                    adjustPlayer(2, "sword_movement", 1)
                if event.key == pygame.K_QUESTION:
                    adjustPlayer(1, "attack", True)
                    player2.setIsAttacking(True)

            # Let go of key so stop performing said action
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    adjustPlayer(1, "right", False)
                elif event.key == pygame.K_a:
                    adjustPlayer(1, "left", False)
                if event.key == pygame.K_SPACE:
                    adjustPlayer(1, "up", False)
                if event.key == pygame.K_LEFT:
                    adjustPlayer(2, "left", False)
                elif event.key == pygame.K_RIGHT:
                    adjustPlayer(2, "right", False)
                if event.key == pygame.K_RSHIFT:
                    adjustPlayer(2, "up", False)


        # NON EVENT BASED ACTIONS
        # Player 1 Sprite/Movement

        if p1_meta_info["sword_movement"] != 0:
            player1.setSwordHeight(player1.getSwordHeight() + p1_meta_info["sword_movement"])
            player1.sword_positioning()
            p1_meta_info["sword_movement"] = 0
        elif p1_meta_info["attack"] != True:
            player1.sword_positioning()
            p1_meta_info["attack"] = False

        if player1.rect.x > player2.rect.x:
            player1.setDirection("left")
        else:
            player1.setDirection("right")


        p1_x_shift = 0
        if p1_meta_info["left"]:
            p1_x_shift += -5
            if abs(player1.getXVelocity()) > 30:
                player1.setDirection("left")
        elif p1_meta_info["right"]:
            p1_x_shift += 5
            if abs(player1.getXVelocity()) > 30:
                player1.setDirection("right")
        if p1_meta_info["up"] and player1.is_on_ground:#TODO: make better Gravity
            player1_y_vel = -15
            player1.setAirTime(time())
            player1.setOnGround(False)
        elif not player1.is_on_ground: #TODO: make better Gravity
            if player1.getAirTime() == 0:
                player1.setAirTime(time())
            player1_y_vel = player1_y_vel + 5*(time()-player1.getAirTime())
        p1_y_shift = player1_y_vel

        if p1_x_shift ==0 and p1_y_shift ==0:
            sdap=0
            # No movement NOT IMPLEMENTED , SDAP IS PLACE HOLDER SO THERE IS NO ERROR
        else:
            sdap = 1
            # No movement NOT IMPLEMENTED , SDAP IS PLACE HOLDER SO THERE IS NO ERROR

        collisions = player1.move(p1_x_shift, p1_y_shift, entities)

        if collisions["bottom"]:
            player1_y_vel = 0

        # Player 2 Sprite/Movement

        if p2_meta_info["sword_movement"] != 0:
            player2.setSwordHeight(player2.getSwordHeight() + p2_meta_info["sword_movement"])
            player2.sword_positioning()
            p2_meta_info["sword_movement"] = 0
        elif p2_meta_info["attack"] != True:
            player2.sword_positioning()
            p2_meta_info["attack"] = False

        if player1.rect.x > player2.rect.x:
            player2.setDirection("right")
        else:
            player2.setDirection("left")

        p2_x_shift = 0
        if p2_meta_info["left"]:
            p2_x_shift += -5
            if abs(player2.getXVelocity()) > 30:
                player2.setDirection("left")

        elif p2_meta_info["right"]:
            p2_x_shift += 5
            if abs(player2.getXVelocity()) > 30:
                player2.setDirection("right")

        if p2_meta_info["up"] and player2.is_on_ground:  # TODO: make better Gravity
            player2_y_vel = -15
            player2.setAirTime(time())
            player2.setOnGround(False)
        elif not player2.is_on_ground:  # TODO: make better Gravity
            if player2.getAirTime() == 0:
                player2.setAirTime(time())
            player2_y_vel = player2_y_vel + 5 * (time() - player2.getAirTime())
        p2_y_shift = player2_y_vel

        if p2_x_shift == 0 and p2_y_shift == 0:
            sdap = 0;
            # No movement NOT IMPLEMENTS , SDAP IS PLACE HOLDER SO TEHRE IS NO ERROR
        else:
            sdap = 1;
            # No movement NOT IMPLEMENTS , SDAP IS PLACE HOLDER SO TEHRE IS NO ERROR

        collisions = player2.move(p2_x_shift, p2_y_shift, entities)

        if collisions["bottom"]:
            player2_y_vel = 0

        player1body = player1.getCollisionRect()
        player2body = player2.getCollisionRect()
        if getSwordLine(player1).colliderect(getSwordLine(player2)):
            #print("Clash!")
            if player1.getDirectionFacing() == "left":
                player1.move(3.5, 0, entities)
                player2.move(-3.5, 0, entities)
            else:
                player1.move(-3.5, 0, entities)
                player2.move(3.5, 0, entities)
            player1.setXVelocity(0)
            player2.setXVelocity(0)
        else:
            if (player1body.colliderect(getSwordLine(player2)) and player2body.colliderect(getSwordLine(player1))):
                #print("players both died")
                player1.setIsGhost(True)
                player2.setIsGhost(True)
                #screen locked in place
            elif player1body.colliderect(getSwordLine(player2)):
                #print("player 1 had an ouchie")
                player1.setIsGhost(True) #Should start a counter for each frame of death animation, followed by a respawn delay, followed by drawing them as a ghost in that spot
                player2.setIsGhost(False)
                #screen follows player 2
            elif player2body.colliderect(getSwordLine(player1)):
                #print("player 2 had an ouchie")
                player2.setIsGhost(True) #Should start a counter for each frame of death animation, followed by a respawn delay, followed by drawing them as a ghost in that spot
                player1.setIsGhost(False)
                #screen follows player 1




        gameFrame.render(my_sprites, draw_buffer)
