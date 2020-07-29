"""
.. module:: Player
.. synopsis: module for a player object
"""
import pygame
from pygame import Rect
import time
from tile import Tile

# change these
hit_box_width = 102
hit_box_height = 140
image_shift_amount_x = 90  # This variable represents the amount of pixels of whitespace in the X dirrection from the left side of the player
image_shift_amount_y = 12  # This variable represents the amount of pixels of whitespace in the Y dirrection from the left side of the player


# 102x203
"""Grace's sprite update
        : no more x_pos and y_pos variables, now in self.rect.x and self.rect.y_pos
		: no more self.player_rect, uses self.rect instead
		: update updates the player's position, is called from the movement method
		: dx is the change in the player's x position
		: dy is the change in the player's y position

"""

class Player(pygame.sprite.DirtySprite):
    """Class representing individual players' avatar, their attributes, and movement
       :param direction_facing: the direction the player is facing (0 for left and 1 for right)
       :param sword_height: the height at which the player is holding the sword (0 means no sword, 3 is high, 2 is med, 1 is low sword)
       :param is_ghost: True if the player has respawned as a ghost and False if the player is not currently a ghost
       :param is_locked_on: True if camera is following this player, False otherwise
       :param sprite: the image name for the player's current motion
       :param image_dict: a dictionary of image file names for each motion
    """
    def __init__(self, x_pos, y_pos, direction_facing, sword_height, is_ghost, is_locked_on, image_dict, win_direction):
        pygame.sprite.DirtySprite.__init__(self)
        self._player_state = {
            "running": False,
            "jumping": False,
            "ducking": False,
            "thrusting": False,
            "on_right_wall": False,
            "on_left_wall": False,
            "on_ground": False,
            "locked_on": False,
            "ghost": False,
            "ghost_counter": -1,
            "sword_height": 2,
            "direction_facing": direction_facing,
            "air_time": 0,
            "x_velocity": 0,
            "y_velocity": 0,
            "count_until_turn_around" : 0,
            "sword": True,
            "sword_moving": True,
            "run_counter": 0,
            "ignore_gravity" : False,
            "player_won": False,
            "win_direction": win_direction #-1 left, 1 right
        }
        self._image_dict = image_dict
        self.image = pygame.image.load(self.getSprite()).convert_alpha()
        self.rect = Rect(x_pos + image_shift_amount_x, y_pos - image_shift_amount_y, 73, 140)

    def getXPos(self):
        return self.rect.x

    def getYPos(self):
        return self.rect.y

    def moveLeft(self):
        if (self.getPlayerState("ghost_counter") > 150 or self.getPlayerState("ghost_counter") == -1):
            self.setPlayerState("x_velocity", self.getPlayerState("x_velocity") - 1)
            if abs(self.getPlayerState("x_velocity")) > 5:
                self._player_state["count_until_turn_around"] += 1
            else:
                self._player_state["count_until_turn_around"] -= 4
            if self._player_state["count_until_turn_around"] > 15:
                self.setDirection("left")
                self._player_state["count_until_turn_around"] = 20
                self.setPlayerState("running", True)
            elif self._player_state["count_until_turn_around"] < 0:
                self._player_state["count_until_turn_around"] = 0
            if self.getPlayerState("x_velocity") < -10:
                self.setPlayerState("x_velocity", -10)
            if self.getPlayerState("ducking") and self.getPlayerState("x_velocity") < -3:
            	self.setPlayerState("x_velocity", -3)
        else:
            self.setPlayerState("x_velocity", 0)

    def moveRight(self):
        if (self.getPlayerState("ghost_counter") > 150 or self.getPlayerState("ghost_counter") == -1):
            self.setPlayerState("x_velocity", self.getPlayerState("x_velocity") + 1)
            if abs(self.getPlayerState("x_velocity")) > 5:
                self._player_state["count_until_turn_around"] += 1
            else:
                self._player_state["count_until_turn_around"] -= 4
            if self._player_state["count_until_turn_around"] > 15:
                self.setDirection("right")
                self._player_state["count_until_turn_around"] = 20
                self.setPlayerState("running", True)
            elif self._player_state["count_until_turn_around"] < 0:
                self._player_state["count_until_turn_around"] = 0

            if self.getPlayerState("x_velocity") > 10:
                self.setPlayerState("x_velocity", 10)
            if self.getPlayerState("ducking") and self.getPlayerState("x_velocity") > 3:
            	self.setPlayerState("x_velocity", 3)
        else:
            self.setPlayerState("x_velocity", 0)

    def standingStill(self):
        if self.getPlayerState("x_velocity") > 0:
            self.setPlayerState("x_velocity", self.getPlayerState("x_velocity") / 5)
        elif self.getPlayerState("x_velocity") < 0:
            self.setPlayerState("x_velocity", self.getPlayerState("x_velocity") / 5)
        if abs(self.getPlayerState("x_velocity")) < .1:
            self.setPlayerState("x_velocity", 0)
        if abs(self.getPlayerState("x_velocity")) < 1:
            self._player_state["count_until_turn_around"] -= 4
        if self._player_state["count_until_turn_around"] > 15:
            self.setDirection("right")
        elif self._player_state["count_until_turn_around"] < 0:
            self._player_state["count_until_turn_around"] = 0

    def calculateGravity(self, time):
        if self.getPlayerState("air_time") == 0:
            self.setPlayerState("air_time", time)
        self.setPlayerState("y_velocity", self.getPlayerState("y_velocity") + 5 * (time - self.getPlayerState("air_time")))
        if self.getPlayerState("y_velocity") > 50:
            self.setPlayerState("y_velocity", 50)
        if self.getPlayerState("on_ground") or self.getPlayerState("ignore_gravity"):
            self.setPlayerState("y_velocity", 0)
        #if self.getPlayerState("ignore_gravity"):
        #    self.setPlayerState("y_velocity", 0)


    def jump(self, time):
        self.setPlayerState("y_velocity", - 12)
        self.setPlayerState("air_time", time)
        self.setPlayerState("on_ground", False)

    def update(self):
        #print(self.getSprite())
        self.image = pygame.image.load(self.getSprite())
        self.dirty = 1  # force redraw from image, since we moved the sprite rect

    def getPlayerState(self, type):
        return self._player_state[type]

    def setPlayerState(self, type, value):
        self._player_state[type] = value

    def setDirection(self, direction):
        if (self.getPlayerState("ghost_counter") > 150 or self.getPlayerState("ghost_counter") == -1):
            if direction == "left":
                self._player_state["direction_facing"] = 1
            else:
                self._player_state["direction_facing"] = 0

    def getDirection(self):
        if self._player_state["direction_facing"] == 1:
            return "left"
        else:
            return "right"

    def adjustSwordHeight(self, adjustment):
        self._player_state["sword_height"] += adjustment
        if self._player_state["sword_height"] < 1:
            self._player_state["sword_height"] = 1
        elif self._player_state["sword_height"] > 3:
            self._player_state["sword_height"] = 3

    def respawn(self, startx, starty):
        if self._player_state["win_direction"] == -1:
            self.rect.x = startx + 314
            self.rect.y = starty - 150
        else:
            self.rect.x = startx - 386
            self.rect.y = starty - 150

    def getSprite(self):
        #print(self._player_state["ghost_counter"])
        if self._player_state["ghost"]:
            front = "ghost_"
        else:
            front = ""
        if self._player_state["direction_facing"] == 1:
            append = "_l"
        else:
            append = "_r"
        if not self._player_state["sword"]:
        	append = append + "_nosword"
        if self._player_state["ghost_counter"] >= 0 and self._player_state["ghost_counter"] < 50:
            return self._image_dict[front + "dead" + append + "_1"]
        elif self._player_state["ghost_counter"] >= 50 and self._player_state["ghost_counter"] < 100:
            return self._image_dict[front + "dead" + append + "_2"]
        elif self._player_state["ghost_counter"] >= 100 and self._player_state["ghost_counter"] < 150:    
            return self._image_dict[front + "dead" + append + "_3"]

        else:
            if self._player_state["ghost_counter"] == 151:
                self._player_state["ghost"] = True
            if self._player_state["running"]:
                self._player_state["run_counter"] = self._player_state["run_counter"] + 1
                if self._player_state["run_counter"] == 22:
                    self._player_state["run_counter"] = 1
                if self._player_state["run_counter"] > 14:
                    run = "_1"
                elif self._player_state["run_counter"] > 7:
                    run = "_2"
                else:
                    run = "_3"
                return self._image_dict[front + "run" + append + run]
            if self._player_state["jumping"]:
                return self._image_dict[front + "jump" + append]
            if self._player_state["ducking"]:
                return self._image_dict[front + "duck" + append]
            if self._player_state["sword_height"] == 1:
                append = "_low"+append
            elif self._player_state["sword_height"] == 2:
                append = "_med" + append
            else:
                append = "_high" + append
            if self._player_state["thrusting"]:
                return self._image_dict[front + "thrust" + append]
            else:
                return self._image_dict[front + "sword" + append]

    def getImageDict(self):
        return self._image_dict

    def setImageDict(self, image_dict):
        self._image_dict = image_dict

    def getCollisionRect(self):
        return Rect(self.rect.x + image_shift_amount_x, self.rect.y - image_shift_amount_y, 73, 140)

    def debug(self):
        print("x_vel: ", end="")
        print(self.getPlayerState("x_velocity"), end=" ")
        print("y_vel: ", end="")
        print(self.getPlayerState("y_velocity"), end=" ")
        print("x_cord: ", end="")
        print(self.rect.x, end=" ")
        print("y_cord: ", end="")
        print(self.rect.y)
        print("count: ", end="")
        print(self.getPlayerState("count_until_turn_around"))

    def move(self, entities, camera): #TODO Check for being stabbed in this method

        self.setPlayerState("on_ground", False)
        self.setPlayerState("on_right_wall", False)
        self.setPlayerState("on_left_wall", False)

        if self.getPlayerState("ducking"):
        	self.setPlayerState("running", False)

        ghost_multiplier = 1
        if self.getPlayerState("ghost"):
        	ghost_multiplier = 1.5

        collision_list = self.test_collision_X(entities,camera)  # Test all entities on the map for collision with player
        self.rect.x += (self.getPlayerState("x_velocity")) * ghost_multiplier
        for objects in collision_list:
            if self.getPlayerState("x_velocity") < 0:  # Moving left
                self.rect.left = objects.right - image_shift_amount_x
                self.setPlayerState("on_left_wall", True)
            elif self.getPlayerState("x_velocity") > 0:  # Moving right
                self.rect.right = objects.left - image_shift_amount_x
                self.setPlayerState("on_right_wall", True)
        # Lock player to look at other player when standing still or moving short time.
        # Flip player if they have been moving a certain amount of time.

        collision_list = self.test_collision_Y(entities,camera)
        self.rect.y += (self.getPlayerState("y_velocity"))
        for objects in collision_list:
            if self.getPlayerState("y_velocity") < 0:  # Moving up
                self.rect.top = objects.bottom - image_shift_amount_y
            elif self.getPlayerState("y_velocity") > 0:  # Moving down
                self.rect.bottom = objects.top + image_shift_amount_y
                self.setPlayerState("on_ground", True)

        if  self._player_state["ghost_counter"] < 0 or self._player_state["ghost_counter"] >= 150: # if player is not dying
            screen_rect = camera.getScreenRect()
            offset = camera.getOffset()
            screen_rect = pygame.Rect(screen_rect.left + offset[0], 0, 1000, 600)
            self.rect.clamp_ip(screen_rect) # makes player stay on screen
        
        self.update()  # updates players position

    def test_collision_Y(self, entities, camera):
        collision_list = []
        self.rect.y += (self.getPlayerState("y_velocity"))
        length = len(entities)
        for objects in entities:
            if self.getCollisionRect().colliderect(objects.getRect()):
                if objects.getEffects()["Kill"] and (self.getPlayerState("ghost_counter")== -1 or self.getPlayerState("ghost_counter")> 151):
                    if self.getPlayerState("win_direction") == camera.getTarget().getPlayerState("win_direction"):
                        camera.setActive(False)
                    self.setPlayerState("ghost_counter", 0)
                    self.setPlayerState("sword", True)
                if length <= 2:
                    pass
                else:
                    collision_list.append(objects.getRect())
            length = length - 1
        self.rect.y -= (self.getPlayerState("y_velocity"))
        return collision_list

    def test_collision_X(self, entities, camera):
        collision_list = []
        self.rect.x += (self.getPlayerState("x_velocity"))
        length = len(entities)
        for objects in entities:
            if self.getCollisionRect().colliderect(objects.getRect()):
                if objects.getEffects()["Kill"]:
                    if self.getPlayerState("win_direction") == camera.getTarget().getPlayerState("win_direction"):
                        camera.setActive(False)
                    self.setPlayerState("ghost_counter", 0)
                    self.setPlayerState("sword", True)
                elif objects.getEffects()["P2Flag"]:
                    if self.getPlayerState("win_direction") == -1 and not self.getPlayerState("ghost"):
                        self.setPlayerState("player_won", True)
                elif objects.getEffects()["P1Flag"]:
                    if self.getPlayerState("win_direction") == 1 and not self.getPlayerState("ghost"):
                        self.setPlayerState("player_won", True)
                else:
                    collision_list.append(objects.getRect())
            length = length - 1
        self.rect.x -= (self.getPlayerState("x_velocity"))
        return collision_list

    def duck(self):
        global hit_box_height
        hit_box_height /= 2

    def standUp(self):
        global hit_box_height
        hit_box_height *= 2

    sprite = property(getSprite)
    image_dict = property(getImageDict, setImageDict)
    duck = property(duck)
    stand_up = property(standUp)
    #Sources: https://github.com/gerryjenkinslb/pygame_dirtysprites/blob/master/Simple_Example_dirty_Sprites.py
