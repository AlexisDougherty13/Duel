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
from audioEngine import AudioEngine

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
    "attack_count": 0
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
    "attack_count": 0
}

def mainMenu(screen , audio):  # TODO Call Main Menu Frame instead and have it call startGame
    audio.changeSong("Main Menu")
    mainMenuFrame.mainMenu(screen, audio)

def adjustPlayer(player, aspect, value):
    if player == 1:
        p1_meta_info[aspect] = value
    elif player == 2:
        p2_meta_info[aspect] = value

# :param Requires a Screen Objects (Created in the main passed to main menu),
#  an int map_selection to determine what map to put on,
# and 2 string skin_selection to determine what skins the players choose
def startGame(screen, map_selection, skin_selection1, skin_selection2 , audio):
    paused = False

    current_map = mapSelectionList.selectMap(map_selection)  # returns a child of the map class

    entities = current_map.getCollidableEntities()

    player1 = Player(300, 100, 1, 2, False, True, getSkin(skin_selection1))  # Initializes player1
    player2 = Player(400, 100, 1, 2, False, False, getSkin(skin_selection2))  # Initializes player2

    draw_buffer, my_sprites = gameFrame.init(player1, player2, current_map, entities)

    clock = pygame.time.Clock()

    print("starting")

    player1_y_vel = 0 #temp will be altered soon
    player2_y_vel = 0  # temp will be altered soon

    active_match = True

    audio.changeSong(current_map.songName)

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
                    adjustPlayer(1, "attack_count", 30)
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
                    player2.setPlayerState("attacking", True)
                if event.key == pygame.K_ESCAPE:
                    mainMenuFrame.pauseMenu(screen)


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
        if p1_meta_info["attack_count"] > 0:
            player1.setPlayerState("thrusting", True)
            p1_meta_info["attack_count"] -= 1
        else:
            player1.setPlayerState("thrusting", False)
            if p1_meta_info["sword_movement"] != 0:
                player1.adjustSwordHeight(p1_meta_info["sword_movement"])
                p1_meta_info["sword_movement"] = 0

        if player1.rect.x > player2.rect.x:
            player1.setDirection("left")
        else:
            player1.setDirection("right")

        if p1_meta_info["left"]:
            player1.moveLeft()
        elif p1_meta_info["right"]:
            player1.moveRight()
        elif player1.getPlayerState("x_velocity") != 0:
            player1.standingStill()
        if p1_meta_info["up"] and player1.getPlayerState("on_ground"):
            player1.jump(time())
        elif not player1.getPlayerState("on_ground"):
            player1.calculateGravity(time())

        # Player 2 Sprite/Movement

        if p2_meta_info["attack_count"] > 0:
            player2.setPlayerState("thrusting", True)
            p2_meta_info["attack_count"] -= 1
        else :
            player2.setPlayerState("thrusting", False)
            if p2_meta_info["sword_movement"] != 0:
                player2.adjustSwordHeight(p2_meta_info["sword_movement"])
                p2_meta_info["sword_movement"] = 0

        if player2.rect.x > player1.rect.x:
            player2.setDirection("left")
        else:
            player2.setDirection("right")

        if p2_meta_info["left"]:
            player2.moveLeft()
        elif p2_meta_info["right"]:
            player2.moveRight()
        elif player2.getPlayerState("x_velocity") != 0:
            player2.standingStill()
        if p2_meta_info["up"] and player2.getPlayerState("on_ground"):
            player2.jump(time())
        elif not player2.getPlayerState("on_ground"):
            player2.calculateGravity(time())

        #Collision stuffs
        player1body = player1.getCollisionRect()
        player2body = player2.getCollisionRect()
        if getSwordLine(player1).colliderect(getSwordLine(player2)):
            #print("Clash!")
            player1.setPlayerState("x_velocity", 0)
            player2.setPlayerState("x_velocity", 0)
            if player1.getDirection() == "left":
                player1.moveRight()
                player2.moveLeft()
            else:
                player1.moveLeft()
                player2.moveRight()
        else:
            if player1body.colliderect(getSwordLine(player2)) and player2body.colliderect(getSwordLine(player1)):
                print("players both died")
                player1.setPlayerState("ghost", True)
                player2.setPlayerState("ghost", True)
                #screen locked in place
            elif player1body.colliderect(getSwordLine(player2)):
                print("player 1 had an ouchie")
                player1.setPlayerState("ghost", True) #Should start a counter for each frame of death animation, followed by a respawn delay, followed by drawing them as a ghost in that spot
                player2.setPlayerState("ghost", False)
                #screen follows player 2
            elif player2body.colliderect(getSwordLine(player1)):
                print("player 2 had an ouchie")
                player2.setPlayerState("ghost", True) #Should start a counter for each frame of death animation, followed by a respawn delay, followed by drawing them as a ghost in that spot
                player1.setPlayerState("ghost", False)
                #screen follows player 1

        player1.move(entities)
        player2.move(entities)

        #render
        gameFrame.render(my_sprites, draw_buffer)
