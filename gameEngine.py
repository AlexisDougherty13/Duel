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

# temp data, should not be here for long....
# Player 1 meta info, store inputs and send to the player object
p1_meta_info = {
    "up": False,  # if the player is moving in this direction
    "left": False,  # if the player is moving in this direction
    "right": False,  # if the player is moving in this direction
    "down": False,  # if the player is moving in this direction
    "sword_movement": 0, #if the sword is moving up its +1 if its moving down its -1 if not moving its 0
    "sword_down": False,  # down due to movement greater than 1/4sec
    "movement_clock": 0  # time in milliseconds in which the player has moved without stopping
}

    # Player 2 meta info, store inputs and send to the player object
p2_meta_info = {
    "up": False,  # if the player is moving in this direction
    "left": False,  # if the player is moving in this direction
    "right": False,  # if the player is moving in this direction
    "down": False,  # if the player is moving in this direction
    "sword_movement": 0,  # if the sword is moving up its +1 if its moving down its -1 if not moving its 0
    "sword_down": False,  # down due to movement greater than 1/4sec
    "movement_clock": 0  # time in milliseconds in which the player has moved without stopping
}

def mainMenu(screen):  # TODO Call Main Menu Frame instead and have it call startGame
    startGame(screen, 0, "Montoya", "Montoya")


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

    player1 = Player(400, 100, 1, 2, False, True, 'Resources/Images/MontoyaMedR.png',
                     getSkin(skin_selection1))  # Initializes player1
    player2 = Player(600, 300, 1, 2, False, False, 'Resources/Images/MontoyaMedL.png',
                     getSkin(skin_selection2))  # Initializes player2
    clock = pygame.time.Clock()
    print("starting")

    player1_y_vel = 0 #temp will be altered soon
    player2_y_vel = 0  # temp will be altered soon

    active_match = True
    while active_match:
        # Delta time is implemented to help make sure that player's models will move at the same speed regardless of monitor refresh rate and processor speed.
        # Could use further optimizing and troubleshooting.
        clock.tick(120)

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
                if event.key == pygame.K_KP4:
                    adjustPlayer(1, "left", True)
                elif event.key == pygame.K_KP6:
                    adjustPlayer(1, "right", True)
                if event.key == pygame.K_KP_ENTER:
                    adjustPlayer(1, "up", True)
                if event.key == pygame.K_KP5:
                    adjustPlayer(1, "sword_movement", -1)
                elif event.key == pygame.K_KP8:
                    adjustPlayer(1, "sword_movement", 1)

            # Let go of key so stop performing said action
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    adjustPlayer(1, "right", False)
                elif event.key == pygame.K_a:
                    adjustPlayer(1, "left", False)
                if event.key == pygame.K_SPACE:
                    adjustPlayer(1, "up", False)
                if event.key == pygame.K_KP4:
                    adjustPlayer(1, "left", True)
                elif event.key == pygame.K_KP6:
                    adjustPlayer(1, "right", True)
                if event.key == pygame.K_KP_ENTER:
                    adjustPlayer(1, "up", True)


        # NON EVENT BASED ACTIONS
        # Player 1 Sprite/Movement
        p1_x_shift = 0
        if p1_meta_info["left"]:
            p1_x_shift += -3
        elif p1_meta_info["right"]:
            p1_x_shift += 3
        if p1_meta_info["up"] and player1.is_on_ground:#TODO: make better Gravity
            player1_y_vel =-10
        elif not player1.is_on_ground: #TODO: make better Gravity
            player1_y_vel = (player1_y_vel/6) +1

        p1_y_shift = player1_y_vel
        collisions = player1.move(p1_x_shift, p1_y_shift, entities)

        if collisions["bottom"]:
            player1_y_vel = 0

        # Player 2 Sprite/Movement
        p2_x_shift = 0
        if p2_meta_info["left"]:
            p2_x_shift += -3
        elif p2_meta_info["right"]:
            p2_x_shift += 3
        if p2_meta_info["up"] and player1.is_on_ground:  # TODO: make better Gravity
            player2_y_vel = 6
        elif not player2.is_on_ground:  # TODO: make better Gravity
            player2_y_vel += (-player1_y_vel / 3) - 1

        p2_y_shift = player2_y_vel
        collisions = player2.move(p2_x_shift, p2_y_shift, entities)

        if collisions["bottom"]:
            player2_y_vel = 0

        gameFrame.render(screen, player1,player2,current_map)