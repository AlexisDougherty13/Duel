"""
.. module:: gameEngine
.. synopsis: The Game's driving loop, This is where the whole game will be run from
"""
import mapSelectionList
import sys
from player import Player
from sword import Sword
import pygame
from pygame import Rect
from playerSkinsList import getSkin
import gameFrame
from swordHitBoxes import getSwordLine
from time import time
import mainMenuFrame
import pauseButtons
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

def getSwordDisarm(player): 
    point1 = -1
    height = -1
    if player.getDirection() == "left":
        point1 = player.rect.x + 41
    else:
        point1 = player.rect.x + 171
    if player.getPlayerState("sword_height") == 1:
        height = player.rect.y + 61
    elif player.getPlayerState("sword_height") == 2:
        height = player.rect.y + 37
    elif player.getPlayerState("sword_height") == 3:
        height = player.rect.y + 13

    return [point1, height]

# :param Requires a Screen Objects (Created in the main passed to main menu),
#  an int map_selection to determine what map to put on,
# and 2 string skin_selection to determine what skins the players choose
def startGame(screen, map_selection, skin_selection1, skin_selection2 , audio):
    paused = False

    current_map = mapSelectionList.selectMap(map_selection)  # returns a child of the map class

    entities = current_map.getCollidableEntities()
    entity_colors = current_map.color_list
    left_wall = Rect(-20, 0, 20, 1000)
    right_wall = Rect(-20, 0, 20, 1000)


    swords = []

    player1 = Player(-50, 100, 1, 2, False, True, getSkin(skin_selection1), 1)  # Initializes player1 -50, 100
    player2 = Player(675, 100, 1, 2, False, False, getSkin(skin_selection2), -1)  # Initializes player2 675, 100

    display, camera = gameFrame.init(current_map)
    
    clock = pygame.time.Clock()

    print("starting")

    active_match = True

    audio.changeSong(current_map.songName)

    while active_match:
        # Delta time is implemented to help make sure that player's models will move at the same speed regardless of monitor refresh rate and processor speed.
        # Could use further optimizing and troubleshooting.
        clock.tick(90)

        for event in pygame.event.get():
            # What to do on quit
            if event.type == pygame.QUIT:
                audio.closeAudioEngine()
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()

            # Pressed a key so perform said action
            if event.type == pygame.KEYDOWN:

                if player1.getPlayerState("ghost_counter") == -1 or player1.getPlayerState("ghost_counter") > 300:
                    if event.key == pygame.K_d:
                        adjustPlayer(1, "right", True)
                    elif event.key == pygame.K_a:
                        adjustPlayer(1, "left", True)
                    if event.key == pygame.K_SPACE:
                        adjustPlayer(1, "up", True)
                    if event.key == pygame.K_s:
                        if player1.getPlayerState("sword_height") == 1:
                            player1.setPlayerState("ducking", True)
                        adjustPlayer(1, "sword_movement", -1)
                        player1.setPlayerState("sword_moving", True)
                    elif event.key == pygame.K_w:
                        adjustPlayer(1, "sword_movement", 1)
                        player1.setPlayerState("sword_moving", True)
                    else:
                        player1.setPlayerState("sword_moving", False)
                    if event.key == pygame.K_f:
                        adjustPlayer(1, "attack_count", 30)
                if player2.getPlayerState("ghost_counter") == -1 or player2.getPlayerState("ghost_counter") > 300:
                    if event.key == pygame.K_LEFT:
                        adjustPlayer(2, "left", True)
                    elif event.key == pygame.K_RIGHT:
                        adjustPlayer(2, "right", True)
                    if event.key == pygame.K_RSHIFT:
                        adjustPlayer(2, "up", True)
                    if event.key == pygame.K_DOWN:
                        if player2.getPlayerState("sword_height") == 1:
                            player2.setPlayerState("ducking", True)
                        adjustPlayer(2, "sword_movement", -1)
                        player2.setPlayerState("sword_moving", True)
                    elif event.key == pygame.K_UP:
                        adjustPlayer(2, "sword_movement", 1)
                        player2.setPlayerState("sword_moving", True)
                    else:
                        player2.setPlayerState("sword_moving", False)
                    if event.key == pygame.K_RCTRL:
                        adjustPlayer(2, "attack_count", 30)
                        player2.setPlayerState("attacking", True)
                if event.key == pygame.K_ESCAPE:
                    mainMenuFrame.pauseMenu(screen, p1_meta_info, p2_meta_info, audio)


            # Let go of key so stop performing said action
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    adjustPlayer(1, "right", False)
                elif event.key == pygame.K_a:
                    adjustPlayer(1, "left", False)
                if event.key == pygame.K_SPACE:
                    adjustPlayer(1, "up", False)
                if event.key == pygame.K_s:
                    player1.setPlayerState("ducking", False)
                if event.key == pygame.K_LEFT:
                    adjustPlayer(2, "left", False)
                elif event.key == pygame.K_RIGHT:
                    adjustPlayer(2, "right", False)
                if event.key == pygame.K_RSHIFT:
                    adjustPlayer(2, "up", False)
                if event.key == pygame.K_DOWN:
                    player2.setPlayerState("ducking", False)

        # NON EVENT BASED ACTIONS
        # Player 1 Sprite/Movement
        player1.setPlayerState("running", False)
        player2.setPlayerState("running", False)
        

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
        if p1_meta_info["up"] and player1.getPlayerState("on_ground") and (player1.getPlayerState("ghost_counter") > 300 or player1.getPlayerState("ghost_counter") == -1):
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
        if p2_meta_info["up"] and player2.getPlayerState("on_ground") and (player2.getPlayerState("ghost_counter") > 300 or player2.getPlayerState("ghost_counter") == -1):
            player2.jump(time())
        elif not player2.getPlayerState("on_ground"):
            player2.calculateGravity(time())

        #Collision stuffs
        if player1.getPlayerState("ghost_counter") > 300 or player1.getPlayerState("ghost_counter") == -1:
            if player1.getPlayerState("ducking") == False:
                player1body = Rect(player1.rect.x + 127, player1.rect.y - 16, 15, 140)
            else:
                player1body = Rect(player1.rect.x + 127, player1.rect.y + 54, 15, 70)
        else:
            player1body = Rect(-100, -100, 1, 1)

        if player2.getPlayerState("ghost_counter") > 300 or player2.getPlayerState("ghost_counter") == -1:
            if player2.getPlayerState("ducking") == False:
                player2body = Rect(player2.rect.x + 127, player2.rect.y - 16, 15, 140)
            else:
                player2body = Rect(player2.rect.x + 127, player2.rect.y + 54, 15, 70)
        else:
            player2body = Rect(-100, -100, 1, 1)

        while getSwordLine(player1).colliderect(getSwordLine(player2)):
            player1.setPlayerState("x_velocity", 0)
            player2.setPlayerState("x_velocity", 0)
            if player1.getPlayerState("sword_moving") and player2.getPlayerState("thrusting"):
                print("player 1 disarmed player 2")
                player2.setPlayerState("sword", False)
                swordInfo = getSwordDisarm(player2)
                swords.append(Sword(swordInfo[0], swordInfo[1], 0, player2.getPlayerState("direction_facing")))
            elif player2.getPlayerState("sword_moving") and player1.getPlayerState("thrusting"):
                print("player 2 disarmed player 1")
                player1.setPlayerState("sword", False)
                swordInfo = getSwordDisarm(player1)
                swords.append(Sword(swordInfo[0], swordInfo[1], 0, player1.getPlayerState("direction_facing")))                
            else:
                if player1.getDirection() == "left":
                    player1.moveRight()
                    player2.moveLeft()
                    player1.move(entities)
                    player2.move(entities)
                else:
                    player1.moveLeft()
                    player2.moveRight()
                    player1.move(entities)
                    player2.move(entities)
        else:
            if player1body.colliderect(getSwordLine(player2)) and player2body.colliderect(getSwordLine(player1)):
                print("players both died")
                player1.setPlayerState("ghost_counter", 0)
                player2.setPlayerState("ghost_counter", 0)
                camera.setActive(False)
                

                #screen locked in place
            elif player1body.colliderect(getSwordLine(player2)):
                print("player 1 had an ouchie")
                player1.setPlayerState("ghost_counter", 0) #Should start a counter for each frame of death animation, followed by a respawn delay, followed by drawing them as a ghost in that spot
                player2.setPlayerState("ghost_counter", -1)
                player2.setPlayerState("ghost", False)
                camera.setActive(True)
                camera.setTarget(player2)
                player1.setPlayerState("sword", True)
                #screen follows player 2
            elif player2body.colliderect(getSwordLine(player1)):
                print("player 2 had an ouchie")
                player2.setPlayerState("ghost_counter", 0) #Should start a counter for each frame of death animation, followed by a respawn delay, followed by drawing them as a ghost in that spot
                player1.setPlayerState("ghost_counter", -1)
                player1.setPlayerState("ghost", False)
                camera.setActive(True)
                camera.setTarget(player1)
                player2.setPlayerState("sword", True)
                #screen follows player 1

        #sword pickups
        if player1.getPlayerState("ducking") and not player1.getPlayerState("sword"):
            for sword in swords:
                if player1body.colliderect(sword.rect):
                    player1.setPlayerState("sword", True)
                    swords.remove(sword)
        if player2.getPlayerState("ducking") and not player2.getPlayerState("sword"):
            for sword in swords:
                if player2body.colliderect(sword.rect):
                    player2.setPlayerState("sword", True)
                    swords.remove(sword)


        #Just died
        if player1.getPlayerState("ghost_counter") == 0:
            player1.setPlayerState("ducking", False)
        if player2.getPlayerState("ghost_counter") == 0:
            player2.setPlayerState("ducking", False)

        if player1.getPlayerState("ghost_counter") > -1:
            #print("woooooowie")
            player1.setPlayerState("ghost_counter", player1.getPlayerState("ghost_counter") + 1)
        if player2.getPlayerState("ghost_counter") > -1:
            #print("woooooowie 2")
            player2.setPlayerState("ghost_counter", player2.getPlayerState("ghost_counter") + 1)
        if player1.getPlayerState("ghost_counter") == 300:
            #print("woooooowie")
            player1.respawn(player2.getXPos())
        if player2.getPlayerState("ghost_counter") == 300:
            #print("woooooowie 2")
            player2.respawn(player1.getXPos())

        player1.move(entities)
        player2.move(entities)

        for sword in swords:
            if not sword.getState("on_ground"):
                sword.calculateGravity(time())
            sword.move(entities)


        #render
        #gameFrame.render(my_sprites, draw_buffer)

        gameFrame.render(display, screen, player1, player2, entities, camera, swords, current_map._assets_dict, entity_colors)


#if player1.getPlayerState("ghost_counter") >= 0 and player1.getPlayerState("ghost_counter") < 11: