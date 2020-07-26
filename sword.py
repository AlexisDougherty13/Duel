import pygame
from pygame import Rect
import time
import random


class Sword(pygame.sprite.DirtySprite):

    def __init__(self, x_pos, y_pos, rotation, direction):
        pygame.sprite.DirtySprite.__init__(self)
        rotate = 180
        if direction ==0:
            direction = -1
            rotate = 0
        self._state = {
            "x_velocity": direction * random.randint(7,12),
            "y_velocity": random.randint(-12,-7),
            "r_velocity": direction * random.randint(-10, -5),
            "current_r": rotate,
            "on_ground": False,
            "air_time": 0,
        }
        self.image = pygame.image.load("Resources/Images/MontoyaSword.png").convert_alpha()
        self.rect = Rect(x_pos, y_pos, 67, 9)

    def getXPos(self):
        return self.rect.x

    def getYPos(self):
        return self.rect.y

    def calculateGravity(self, time):
        if self.getState("air_time") == 0:
            self.setState("air_time", time)
        self.setState("y_velocity", self.getState("y_velocity") + 5 * (time - self.getState("air_time")))
        if self.getState("y_velocity") > 50:
            self.setState("y_velocity", 50)
        if self.getState("on_ground"):
            self.setState("y_velocity", 0)

    def getState(self, type):
        return self._state[type]

    def setState(self, type, value):
        self._state[type] = value

    def getImageDict(self):
        return self._image_dict

    def setImageDict(self, image_dict):
        self._image_dict = image_dict

    def getCollisionRect(self):
        return self.rect

    def move(self, entities): #TODO Check for being stabbed in this method

        collision_list = self.test_collision_X(entities)  # Test all entities on the map for collision with player
        self.rect.x += (self.getState("x_velocity"))
        for objects in collision_list:
            if self.getState("x_velocity") < 0:  # Moving left
                self.rect.left = objects.right
            elif self.getState("x_velocity") > 0:  # Moving right
                self.rect.right = objects.left
        # Lock player to look at other player when standing still or moving short time.
        # Flip player if they have been moving a certain amount of time.

        collision_list = self.test_collision_Y(entities)
        self.rect.y += (self.getState("y_velocity"))
        for objects in collision_list:
            if self.getState("y_velocity") < 0:  # Moving up
                self.rect.top = objects.bottom
            elif self.getState("y_velocity") > 0:  # Moving down
                self.rect.bottom = objects.top
                self.setState("on_ground", True)
                self.setState("x_velocity", 0)
                self.setState("r_velocity", 0)
 
        self.setState("current_r", self.getState("current_r") + self.getState("r_velocity"))

    def test_collision_Y(self, entities):
        collision_list = []
        self.rect.y += (self.getState("y_velocity"))
        for objects in entities:
            if self.getCollisionRect().colliderect(objects.getRect()) and not objects.getEffects()["Invisible"]:
                collision_list.append(objects.getRect())
        self.rect.y -= (self.getState("y_velocity"))
        return collision_list

    def test_collision_X(self, entities):
        collision_list = []
        self.rect.x += (self.getState("x_velocity"))
        for objects in entities:
            if self.getCollisionRect().colliderect(objects.getRect()) and not objects.getEffects()["Invisible"]:
                collision_list.append(objects.getRect())
        self.rect.x -= (self.getState("x_velocity"))
        return collision_list

    image_dict = property(getImageDict, setImageDict)
    #Sources: https://github.com/gerryjenkinslb/pygame_dirtysprites/blob/master/Simple_Example_dirty_Sprites.py
