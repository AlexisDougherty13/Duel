import player
import math
from pygame import Rect
def getSwordLine(player): 
	point1 = -1
	point2 = -1
	height = -1
	if abs(player.getPlayerState("x_velocity")) < 10 and (player.getPlayerState("ghost_counter") > 300 or player.getPlayerState("ghost_counter") == -1) and (player.getPlayerState("sword")): #if sword is ready
		if player.getPlayerState("ducking") == False:
			if player.getDirection() == "left":
				if not player.getPlayerState("thrusting"): #if player is not attacking
					point1 = player.rect.x + 41
					point2 = player.rect.x + 97
				else: #player is attacking
					point1 = player.rect.x + 0
					point2 = player.rect.x + 55
			else:
				if not player.getPlayerState("thrusting"): #if player is not attacking
					point1 = player.rect.x + 171
					point2 = player.rect.x + 227
				else: #player is attacking
					point1 = player.rect.x + 213
					point2 = player.rect.x + 268
			if player.getPlayerState("sword_height") == 1:
				height = player.rect.y + 61
			elif player.getPlayerState("sword_height") == 2:
				height = player.rect.y + 37
			elif player.getPlayerState("sword_height") == 3:
				height = player.rect.y + 13
		else:
			if player.getDirection() == "left":
				point1 = player.rect.x + 95
				point2 = player.rect.x + 97
			else:
				point1 = player.rect.x + 171
				point2 = player.rect.x + 173
			height = player.rect.y + 20
	return Rect(point1, height, point2-point1, 3)

