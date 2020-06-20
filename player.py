"""
.. module:: Player
.. synopsis: module for a player object
"""
import pygame
from pygame import Rect
import time

# change these
hit_box_width = 102
hit_box_height = 140
player_shift_amount_x = 80  # This variable represents the amount of pixels of whitespace in the X dirrection from the left side of the player
player_shift_amount_y = 8  # This variable represents the amount of pixels of whitespace in the Y dirrection from the left side of the player


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
    def __init__(self, center, direction_facing, sword_height, is_ghost, is_locked_on, image_dict):
        pygame.sprite.DirtySprite.__init__(self)
        self._player_state = {
            "running": False,
            "jumping": False,
            "ducking": False,
            "thrusting": False,
            "on_right_wall": False,
            "on_left_wall": False,
            "on_ground": False,
            "attacking": False,
            "locked_on": False,
            "ghost": False,
            "sword_height": 1,
            "direction_facing": direction_facing,
            "air_time": 0,
            "x_velocity": 0,
            "y_velocity": 0
        }
        self._image_dict = image_dict
        self.image = pygame.image.load(self.getSprite())
        self.rect = self.image.get_rect(center=center)

    def getXPos(self):
        return self.rect.x

    def getYPos(self):
        return self.rect.y

    def update(self):
        self.image = pygame.image.load(self.getSprite())
        x, y = self.rect.center
        x = (x + self._player_state["x_velocity"]) # move by dx,dy and wrap modulo window size
        y = (y + self._player_state["y_velocity"])
        self.rect.center = (x, y)  # changes where sprite will be copied to buffer
        self.dirty = 1  # force redraw from image, since we moved the sprite rect

    def getPlayerState(self, type):
        return self._player_state[type]

    def setPlayerState(self , type, value):
        self._player_state[type]=value

    def setDirection(self, direction):
        if (direction == "left"):
            self._player_state["direction_facing"] = 1
        else:
            self._player_state["direction_facing"] = 0

    def getDirection(self):
        if (self._player_state["direction_facing"] == 1):
            return "left"
        else:
            return "right"

    def adjustSwordHeight(self, adjustment):
        self._player_state["sword_height"] += adjustment
        if self._player_state["sword_height"] > 0:
            self._player_state["sword_height"] = 1
        elif self._player_state["sword_height"] < 4:
            self._player_state["sword_height"] = 3

    def getSprite(self):
        if self._player_state["direction_facing"] == 1:
            append = "_l"
        else:
            append = "_r"
        if self._player_state["running"]:
            return self._image_dict["run" + append]
        if self._player_state["jumping"]:
            return self._image_dict["jump" + append]
        if self._player_state["ducking"]:
            return self._image_dict["duck" + append]
        if self._player_state["sword_height"] == 1:
            append = "_low"+append
        elif self._player_state["sword_height"] == 2:
            append = "_med" + append
        else:
            append = "_high" + append
        if self._player_state["thrusting"]:
            return self._image_dict["thrust" + append]
        else:
            return self._image_dict["sword" + append]

    def getImageDict(self):
        return self._image_dict

    def setImageDict(self, image_dict):
        self._image_dict = image_dict

    def getCollisionRect(self):
        return Rect(self.rect.x + self._player_state["x_velocity"], self.rect.y - self._player_state["y_velocity"], 73, 140)

    def move(self, entities): #TODO Check for being stabbed in this method
        print(self.rect.x)
        self.rect.x += (self.getPlayerState("x_velocity"))
        print(self.rect.x)
        self.rect.y += (self.getPlayerState("y_velocity"))
        collisions = {"top": False, "bottom": False, "left": False, "right": False} #List of directions that have collisions

        collision_list = self.test_collision(entities)                              #Test all entities on the map for collision with player

        self._is_on_wall = ""
        self._is_on_ground = False
        for objects in collision_list:
            self._x_velocity = 0
            if self.getPlayerState("x_velocity") > 0:  # Moving right
                self.rect.right = objects.left - player_shift_amount_x
                collisions["right"] = True
                self.setPlayerState("on_right_wall", True)
            elif self.getPlayerState("x_velocity") < 0: #Moving left
                self.rect.left = objects.right
                collisions["left"] = True
                self.setPlayerState("on_left_wall", True)
        #Lock player to look at other player when standing still or moving short time.
        #Flip player if they have been moving a certain amount of time.

        collision_list = self.test_collision(entities)
        for objects in collision_list:
            if self.getPlayerState("y_velocity") < 0: #Moving up
                self.rect.top = objects.bottom
                collisions["top"] = True
            elif self.getPlayerState("y_velocity") > 0: #Moving down
                self.rect.bottom = objects.top
                collisions["bottom"] = True
                self.setPlayerState("on_ground", True)

        self.update()  # updates players position
        return collisions

    def test_collision(self, entities):
        collision_list = []
        rect = Rect(self.rect.x + self.getPlayerState("x_velocity"), self.rect.y - self.getPlayerState("y_velocity"), 73, 140)
        for objects in entities:
            if self.rect.colliderect(objects):
                collision_list.append(objects)
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
