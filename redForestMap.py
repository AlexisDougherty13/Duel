"""
.. module:: map
.. synopsis: module for a map object
"""
from map import Map

class RedForestMap(Map):
    """Class representing a Specific Map
        """
    def __init__(self):

        assets_dict = {
            "Tile": "Resources/Images/RedForestTile.png",
            "Background": "Resources/Images/ScaledBackgroundAutumnForest.png"
        }
        Map.__init__(self, 1000, 600, 450, 300, 550, 300, assets_dict, "redForestMap.txt")
        self.songName = "Red Forest"
