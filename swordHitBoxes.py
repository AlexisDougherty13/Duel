import player
import math
from pygame import Rect
def getSwordLine(player): 
	point1 = -1
	point2 = -1
	height = -1
	if abs(player.getPlayerState("x_velocity")) < 20: #if sword is ready
		if player.getDirection() == "left":
			if player.getPlayerState("attacking"): #if player is not attacking
				point1 = player.rect.x + 14
				point2 = player.rect.x + 69
			else: #player is attacking
				point1 = player.rect.x + 0
				point2 = player.rect.x + 55
		else:
			if player.getPlayerState("attacking"): #if player is not attacking
				point1 = player.rect.x + 145
				point2 = player.rect.x + 200
			else: #player is attacking
				point1 = player.rect.x + 159
				point2 = player.rect.x + 214
		if player.getPlayerState("sword_height") == 1:
			height = player.rect.y + 61
		elif player.getPlayerState("sword_height") == 2:
			height = player.rect.y + 37
		elif player.getPlayerState("sword_height") == 3:
			height = player.rect.y + 13
	return Rect(point1, height, point2-point1, 3)

