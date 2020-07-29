"""
.. module:: map
.. synopsis: module for a map object
"""
from pygame import Rect
from tile import Tile

class Map():
    """Class representing a General Map's attributes, this is applied to all maps, this is an abstract class
           :param x_length: the level's width
           :param y_length: the level's height
           :param p1_init_x_pos: the player's x-coordinate
           :param p1_init_y_pos: the player's y-coordinate
           :param p2_init_x_pos: the player's x-coordinate
           :param p2_init_y_pos: the player's y-coordinate
           :param background: The background image
           :param assets_dict: a dictionary of all image assets used in this map
           :param floor_height: a set height for the floor
        """

    def __init__(self, x_length, y_length, p1_init_x_pos, p1_init_y_pos, p2_init_x_pos, p2_init_y_pos, assets_dict, TxtFileName):
        self._x_length = x_length
        self._y_length = y_length
        self._p1_init_pos = {
            "X": p1_init_x_pos,
            "Y": p1_init_y_pos
        }
        self._p2_init_pos = {
            "X": p2_init_x_pos,
            "Y": p2_init_y_pos
        }
        self.assets_dict = assets_dict
        self._collidable_entities = []
        self.setCollidableEntities(TxtFileName)

    # abstract method
    ##@abstractmethod
    def setCollidableEntities(self):
        pass

    def getCollidableEntities(self):
        return self._collidable_entities

    def getXLength(self):
        return self._x_length

    def setXLength(self, length):
        self._x_length = length

    def getYLength(self):
        return self._y_length

    def setYLength(self, length):
        self._y_length = length

    def getP1InitialPosition(self):
        return self._p1_init_pos

    def setP1InitialPosition(self, x_pos, y_pos):
        self._p1_init_pos = {
            "X": x_pos,
            "Y": y_pos
            }

    def getP2InitialPosition(self):
        return self._p2_init_pos

    def setP2InitialPosition(self, x_pos, y_pos):
        self._p1_init_pos = {
            "X": x_pos,
            "Y": y_pos
        }

    def getBackground(self):
        return self._assets_dict["Background"]

    def setCollidableEntities(self, TxtFileName):
        entities = []
        file = open(TxtFileName)
        y = 0
        for line in file:
            x = 0
            for num in line:
                effects = {
                    "Kill": False,
                    "Invisible": False,
                    "Slow": False,
                    "Jump": False,
                    "Platform": False,
                    "Speed": False,
                    "P1Flag": False,
                    "P2Flag": False
                }
                if num == "1": # Map Floor Tile
                    entities.append(Tile((x * 50) - 6000, y * 50, 50, 50, self.assets_dict["Tile"], effects))

                elif num == "2": # Invisible Tile
                    effects["Invisible"] = True
                    entities.append(Tile((x * 50) - 6000, y * 50, 50, 50, self.assets_dict["Tile"], effects))

                elif num == "3": # Invisible Kill Tile
                    effects["Invisible"] = True
                    effects["Kill"] = True
                    entities.append(Tile((x * 50) - 6000, y * 50, 50, 50, self.assets_dict["Tile"], effects))

                elif num == "4": # Spike  Tile
                    effects["Kill"] = True
                    entities.append(Tile((x * 50) - 6000, y * 50, 50, 50, self.assets_dict["Spike"], effects))

                elif num == "5": # Platform
                    effects["Platform"] = True
                    entities.append(Tile((x * 50) - 6000, y * 50, 50, 50, self.assets_dict["Tile"], effects))

                elif num == "B": # Player Two Flag
                    effects["P2Flag"] = True
                    entities.append(Tile((x * 50) - 6000, y * 50, 50, 50, self.assets_dict["KingFlag"], effects))

                elif num == "A": # Player One Flag
                    effects["P1Flag"] = True
                    entities.append(Tile((x * 50) - 6000, y * 50, 50, 50, self.assets_dict["KingFlag"], effects))
                

                x = x + 1
            y = y + 1
        file.close()

        self._collidable_entities = entities


    x_length = property(getXLength, setXLength)
    y_length = property(getYLength, setYLength)
    p1_init_pos = property(getP1InitialPosition, setP1InitialPosition)
    p2_init_pos = property(getP2InitialPosition, setP2InitialPosition)
