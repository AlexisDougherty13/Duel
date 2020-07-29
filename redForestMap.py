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
            "Background": "Resources/Images/ScaledBackgroundAutumnForest.png",
            "Spike": "Resources/Images/DesolateDesertSpike.png",
            "MontoyaFlag": "Resources/Images/MontoyaFlag.png",
            "ZorroFlag": "Resources/Images/ZorroFlag.png",
            "KingFlag": "Resources/Images/KingArthurFlag.png"
        }
        Map.__init__(self, 1000, 600, -50, 140, 675, 140, assets_dict, "redForestMap.txt")
        self.songName = "Red Forest"
