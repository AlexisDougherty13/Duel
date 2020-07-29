
"""
.. module:: map
.. synopsis: module for a map object
"""
from map import Map

class DesolateDesertMap(Map):
    """Class representing a Specific Map
        """
    def __init__(self):
        assets_dict = {
            "Tile": "Resources/Images/DesolateDesertTile.png",
            "Background": "Resources/Images/DesolateDesertBG.png",
            "Spike": "Resources/Images/DesolateDesertSpike.png",
            "MontoyaFlag": "Resources/Images/MontoyaFlag.png",
            "ZorroFlag": "Resources/Images/ZorroFlag.png",
            "KingFlag":"Resources/Images/KingArthurFlag.png"
        }
        Map.__init__(self, 1000, 600, 450, 300, 550, 300, assets_dict, "desolateDesertMap.txt")
        self.songName = "Desolate Desert"
