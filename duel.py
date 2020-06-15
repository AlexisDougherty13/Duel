







#Here be Davey Jones Locker, a scrap yard of old and forgotten code,
# 			Long forgotten by the brutal passage of time,
#						will your code die here too?




























from player import Player
import os
import time
from pygame import Rect

#Joshua's Magical TODO list
# 1. Add player movement timer, when player isnt moving for .2 secs his sword should be up - DONE, could use some tweaking to make movement less shit
# 2. Add gravity / jumping. Player should never be below y=ground - DONE, could use some tweaking to make jumps more realistic, player shouldnt be holding sword while airborne

# 3. Add hitbox values for the player at all times.
# 4. Add sword image functionality
# 5. Add sword hitboxes
# 6. Create our buddy player two to test with
# 7. Do stuff with sword hitboxes. People can die. OMG, now we have a somewhat competent looking game
# 8. Dead guy respawns as ghost. Ghost kills person => person becomes ghost, ghost becomes person.
# 9. Add some sort of background and goal points at either side of the map, so we can test screen movement
# 10.Screen locks on to whoever isnt a ghost, and locks in place at the start.
# 11.Reaching the edge of screen => victory conditions show
# CONGRATS, NOW WE HAVE SOMETHING TO SHOW FOR OUR MIDTERM :D
# 12.Fix bugs and make game look good

#Code Revamp Notes:
#Could add a move function to player and use positive and negative values + booleans to determine movement.
#Could add a collision test function that is ran anytime the player moves in any of the 3 directions. This would handle collisions with the map.
#Remove unused functions/variables from player and duel.
#Use rect objects for collisions
#Implement function for map generation using 2D Matrix of symbols that represent when and where to draw a certain object.
#Continous terrain sprite or individual tiles pasted together?
#Implement gravity system off the bat then worry about jumping.
#Remove a lot of unnecessary booleans and conditional statements.
#Hitbox: Could use rects, if player1_rect.colliderect(player2_sword_rect): do the thing


def determineHitBoxes(player): #THIS FUNCTION IS INCOMPLETE AND NOT IN USE
	#Should return a list of [minX, maxX, minY, maxY, minSwordX, maxSwordX, minSwordY, maxSwordY]
	returnList = []
	returnList.append(player.getXPos())
	returnList.append(player.getXPos() + 148)
	returnList.append(player.getYPos())
	returnList.append(player.getYPos() + 111)
	#SWORD STUFF. -1 if sword is down. need to adjust for height of sword
	returnList.append(-1)
	returnList.append(-1)
	returnList.append(-1)
	returnList.append(-1)
	return returnList

def hitBoxComparison(p1, p2): #THIS FUNCTION IS INCOMPLETE AND NOT IN USE
	#[minX, maxX, minY, maxY, minSwordX, maxSwordX, minSwordY, maxSwordY]
	#[minX, maxX, minY, maxY, minSwordX, maxSwordX, minSwordY, maxSwordY]

	#if swords are touching
		#disarm?
		#clash?
	if clashDetection(p1[4], p1[5], p1[6], p1[7], p2[4], p2[5], p2[6], p2[7]):
		print("Clash")
	#if p1 is in p2 sword
	if clashDetection(p1[0], p1[1], p1[2], p1[3], p2[4], p2[5], p2[6], p2[7]):
		print("Player 1 had an ouchie")
	#if p2 is in p1 sword
	if clashDetection(p2[0], p2[1], p2[2], p2[3], p1[4], p1[5], p1[6], p1[7]):
		print("Player 2 had an ouchie")


def clashDetection(xMin1, xMax1, yMin1, yMax1, xMin2, xMax2, yMin2, yMax2): #THIS FUNCTION IS INCOMPLETE AND NOT IN USE
	for x in range(xMin2, xMax2):
		for y in range(yMin2, yMax2):
			if (x > xMin1 and x < xMax1 and y > yMin1 and y < yMax1):
				return True
	return False



# Sources:
# https://nerdparadise.com/programming/pygame/part2
