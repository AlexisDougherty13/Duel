
"""
.. module:: map
.. synopsis: module for a map object
"""
from map import Map
from pygame import Rect


class DesolateDesertMap(Map):
    """Class representing a Specific Map
        """
    def __init__(self):
        assets_dict = {
            "Tile": "Resources/Images/DesolateDesertTile.png",
            "Background": "Resources/Images/DesolateDesertBG.png"
        }
        Map.__init__(self, 1000, 600, 450, 300, 550, 300, "Resources/Images/DesolateDesertBG.png",
                     assets_dict)  # TODO: implement Assets Dict
        self.setCollidableEntities()
        self.songName = "Desolate Desert"
        
     def setCollidableEntities(self):
        color_list = []
        entities = []
        file = open("redForestMap.txt")
        y = 0
        for line in file:
            x = 0
            for num in line:
                if num == "1":
                    entities.append(Rect((x * 50) - 6000, y * 50, 50, 50))
                    color_list.append(1)
                elif num == "3":
                    entities.append(Rect((x * 50) - 6000, y * 50, 50, 50))
                    color_list.append(3)
                x = x + 1
            y = y + 1
        file.close()
        
        self.color_list = color_list
        self._collidable_entities = entities

   # collidable_entities = property(getCollidableEntities, setCollidableEntities)