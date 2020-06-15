"""
.. module:: map
.. synopsis: module for a map object
"""
from pygame import Rect
import abc


class Map(metaclass=abc.ABCMeta):
    """Class representing a General Map's attributes, this is applied to all maps, this is an abstract class
           :param x_length: the player's x-coordinate
           :param y_length: the player's y-coordinate
           :param p1_init_x_pos: the player's x-coordinate
           :param p1_init_y_pos: the player's y-coordinate
           :param p2_init_x_pos: the player's x-coordinate
           :param p2_init_y_pos: the player's y-coordinate
           :param background: The background image
           :param assets_dict: a dictionary of all image assets used in this map
           :param floor_height: a set height for the floor
        """

    def __init__(self, new_x_length, new_y_length, p1_init_x_pos, p1_init_y_pos, p2_init_x_pos, p2_init_y_pos, background, assets_dict):
        self.x_length = new_x_length
        self.y_length = new_y_length
        self.p1_init_x_pos = p1_init_x_pos
        self.p1_init_y_pos = p1_init_y_pos
        self.p2_init_x_pos = p2_init_x_pos
        self.p2_init_y_pos = p2_init_y_pos
        self.background = background
        self.assets_dict = assets_dict
        self.collidable_entities = []

    @abc.abstractmethod
    def setCollidableEntities(self):
        pass

    def getCollidableEntities(self):
        return self.collidable_entities

    def getXLength(self):
        return self.x_length

    def setXLength(self, length):
        self.x_length = length

    def getYLength(self):
        return self.y_length

    def setYLength(self, length):
        self.y_length = length

    def getP1InitialPosition(self):
        return self.p1_init_pos

    def setP1InitialPosition(self, x_pos, y_pos):
        self.p1_init_pos = {
            "X": x_pos,
            "Y": y_pos
            }

    def getP2InitialPosition(self):
        return self.p2_init_pos

    def setP2InitialPosition(self, x_pos, y_pos):
        self.p1_init_pos = {
            "X": x_pos,
            "Y": y_pos
        }

    def getBackground(self):
        return self.background

    def setBackground(self, new_background):
        self.background = new_background

    #collidable_entities = property(getCollidableEntities, setCollidableEntities)
    x_length = property(getXLength, setXLength)
    y_length = property(getYLength, setYLength)
    p1_init_pos = property(getP1InitialPosition, setP1InitialPosition)
    p2_init_pos = property(getP2InitialPosition, setP2InitialPosition)
    background = property(getBackground, setBackground)
