import random
# TODO this will contain a list of every map and import them all
from redForestMap import RedForestMap
from desolateDesertMap import DesolateDesertMap

def selectMap(map_selection):
    if map_selection == 0:
        map_selection = random.randrange(1, 3, 1)  # update this function to include RNG chance of new map
    if map_selection == 1:
        return RedForestMap()
    elif map_selection == 2:
        return DesolateDesertMap()
