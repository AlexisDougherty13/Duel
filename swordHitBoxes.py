import player
import math
from pygame import Rect
def getSwordLine(player): 
	point1 = -1
	point2 = -1
	height = -1
	if abs(player.getXVelocity()) < 30: #if sword is ready
		if player.getDirectionFacing() == "left":
			if player.getIsAttacking() == False: #if player is not attacking
				point1 = player.player_rect.x + 14
				point2 = player.player_rect.x + 69
			else: #player is attacking
				point1 = player.player_rect.x + 0
				point2 = player.player_rect.x + 55
		else:
			if player.getIsAttacking() == False: #if player is not attacking
				point1 = player.player_rect.x + 145
				point2 = player.player_rect.x + 200
			else: #player is attacking
				point1 = player.player_rect.x + 159
				point2 = player.player_rect.x + 214
		if player.getSwordHeight() == 1:
			height = player.player_rect.y + 61
		elif player.getSwordHeight() == 2:
			height = player.player_rect.y + 37
		elif player.getSwordHeight() == 3:
			height = player.player_rect.y + 13
	return Rect(point1, height, point2-point1, 3)

