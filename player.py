"""
.. module:: Player
.. synopsis: module for a player object
"""
from pygame import Rect
import time

#change these
hit_box_width = 102
hit_box_height = 140
player_shift_amount_x = 80 #This variable represents the amount of pixels of whitespace in the X dirrection from the left side of the player
player_shift_amount_y = 8 #This variable represents the amount of pixels of whitespace in the Y dirrection from the left side of the player


# 102x203

class Player:
    """Class representing individual players' avatar, their attributes, and movement
       :param x_pos: the player's x-coordinate
       :param y_pos: the player's y-coordinate
       :param direction_facing: the direction the player is facing (0 for left and 1 for right)
       :param sword_height: the height at which the player is holding the sword (0 means no sword, 3 is high, 2 is med, 1 is low sword)
       :param is_ghost: True if the player has respawned as a ghost and False if the player is not currently a ghost
       :param is_locked_on: True if camera is following this player, False otherwise
       :param sprite: the image name for the player's current motion
       :param image_dict: a dictionary of image file names for each motion
    """
    def __init__(self, x_pos, y_pos, direction_facing, sword_height, is_ghost, is_locked_on, sprite, image_dict):
        self._x_pos = x_pos #we should not be saving this as varaibles if it is in a rectangle
        self._y_pos = y_pos #we also should keep the rectangle for hitbox and image seperate.
        self._direction_facing = direction_facing
        self._sword_height = sword_height
        self._is_ghost = is_ghost
        self._is_locked_on = is_locked_on
        self._sprite = sprite
        self.player_rect = Rect(x_pos, y_pos, 73, 140)
        self._image_dict = image_dict
        self._is_on_wall = ""
        self._is_on_ground = False
        self._air_time = 0

    def getXPos(self):
        return self._x_pos

    def setXPos(self, x_pos):
        self._x_pos = x_pos

    def getYPos(self):
        return self._y_pos

    def setYPos(self, y_pos):
        self._y_pos = y_pos

    def getOnGround(self):
        return self._is_on_ground

    def setOnGround(self, is_on_ground):
        self._is_on_ground = is_on_ground

    def getOnWall(self):
        return self._is_on_wall

    def setOnWall(self, is_on_wall):
        self._is_on_ground = is_on_wall

    def setAirTime(self, air_time):
        self._air_time = air_time

    def getAirTime(self):
        return self._air_time

    def getDirectionFacing(self):
        return self._direction_facing

    def switchDirection(self):
        if(self._x_pos):
            self._x_pos = False
        else:
            self._x_pos = True

    # 0 means no sword, 3 is high, 2 is med, 1 is low sword
    def getSwordHeight(self):
        return self._sword_height

    def setSwordHeight(self, new_pos):
        self._sword_height = new_pos

    def getIsGhost(self):
        return self._is_ghost

    def setIsGhost(self):
        if self._is_ghost:
            self._is_ghost = False
        else:
            self._is_ghost = True

    def getIsLockedOn(self):
        return self._is_locked_on

    def setIsLockedOn(self):
        if self._is_locked_on:
            self._is_locked_on = False
        else:
            self._is_locked_on = True

    def getSprite(self):
        return self._sprite

    def setSprite(self, sprite):

        self._sprite = sprite

    def getImageDict(self):
        return self._image_dict

    def setImageDict(self, image_dict):
        self._image_dict = image_dict

    def move(self, x_shift, y_shift, entities): #TODO Check for being stabbed in this method
        collisions = {"top": False, "bottom": False, "left": False, "right": False} #List of directions that have collisions
        self.player_rect.x += x_shift                                               #Move the player by given amount on the X cordinate
        collision_list = self.test_collision(entities)                              #Test all entities on the map for collision with player
        self._is_on_wall = ""
        for objects in collision_list:
            if x_shift > 0: #Moving right
                self.player_rect.right = objects.left - player_shift_amount_x
                collisions["right"] = True
                self._is_on_wall = "right"
            elif x_shift < 0: #Moving left
                self.player_rect.left = objects.right - player_shift_amount_x
                collisions["left"] = True
                self._is_on_wall = "left"
        #Lock player to look at other player when standing still or moving short time.
        #Flip player if they have been moving a certain amount of time.
        self.player_rect.y += y_shift                                               #Move the player by given amount on the X cordinate
        collision_list = self.test_collision(entities)
        for objects in collision_list:
            if y_shift < 0: #Moving up
                self.player_rect.top = objects.bottom + player_shift_amount_y
                collisions["top"] = True
            elif y_shift > 0: #Moving down
                self.player_rect.bottom = objects.top + player_shift_amount_y
                collisions["bottom"] = True
                self._is_on_ground = True

        return collisions


    def test_collision(self, entities):
        collision_list = []
        rect = Rect(self.player_rect.x + player_shift_amount_x, self.player_rect.y - player_shift_amount_y, 73, 140)
        for objects in entities:
            if rect.colliderect(objects):
                collision_list.append(objects)
        return collision_list

    def moveLeft(self, time):
        self._x_pos -= 3.0
        if time>=0.25:
            self._direction_facing = 0
            self._sprite = self._image_dict["stand_l"]

    def moveRight(self, time):
        self._x_pos += 3.0
        if time>=0.25:
            self._direction_facing = 1

            self._sprite = self._image_dict["stand_l"]

    # 0 means no sword, 3 is high, 2 is med, 1 is low sword
    def raiseSword(self):
        if(self._sword_height >= 1 and self._sword_height < 3):
            self._sword_height += 1

    def lowerSword(self):
        if(self._sword_height <= 3 and self._sword_height > 1):
            self._sword_height -= 1

    def duck(self):
        global hit_box_height
        hit_box_height /= 2

    def standUp(self):
        global hit_box_height
        hit_box_height *= 2

    x_pos = property(getXPos, setXPos)
    y_pos = property(getYPos, setYPos)
    is_on_ground = property(getOnGround, setOnGround)
    air_time = property(getAirTime, setAirTime)
    is_on_wall = property(getOnWall, setOnWall) #is one of 3 strings "left" , "right" , "" empty string means not on wall
    direction_facing = property(getDirectionFacing, switchDirection)
    sword_height = property(getSwordHeight, setSwordHeight)
    is_ghost = property(getIsGhost, setIsGhost)
    is_locked_on = property(getIsLockedOn, setIsLockedOn)
    sprite = property(getSprite, setSprite)
    image_dict = property(getImageDict, setImageDict)
    move_left = property(moveLeft)
    move_right = property(moveRight)
    raise_sword = property(raiseSword)
    lower_sword = property(lowerSword)
    duck = property(duck)
    stand_up = property(standUp)
