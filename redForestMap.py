"""
.. module:: map
.. synopsis: module for a map object
"""
from map import Map
from pygame import Rect

class RedForestMap(Map):
    """Class representing a Specific Map
        """
    def __init__(self):
        Map.__init__(self, 1000, 600, 450, 300, 550, 300, "Resources/Images/ScaledBackgroundAutumnForest.png", "assets_dict") #TODO: implement Assets Dict
        self.setCollidableEntities()
        self.songName = "Red Forest"

    def setCollidableEntities(self):
        floor_rect = Rect(-5000, 500, 11000, 50)
        self._collidable_entities.append(floor_rect)
        
        block_rect = Rect(100, 400, 100, 100)
        self._collidable_entities.append(block_rect)
        block2_rect = Rect(800, 400, 100, 100)
        self._collidable_entities.append(block2_rect)

        player2_flag = Rect(-1000, 275, 225, 225)
        self._collidable_entities.append(player2_flag)
        player1_flag = Rect(2000, 275, 225, 225)
        self._collidable_entities.append(player1_flag)

   # collidable_entities = property(getCollidableEntities, setCollidableEntities)