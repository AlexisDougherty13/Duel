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