import player
import pygame
import os
import sys
import time


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


def get_image(path, _image_library):
        if path not in _image_library:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path).convert_alpha()
                _image_library[path] = image
        return _image_library[path]

def sword_positioning1(player):
	if(player.sword_height == 1 and player.direction_facing == 1):
		player.sprite = player.image_dict["sword_low_r"]
	if(player.sword_height == 2 and player.direction_facing == 1):
		player.sprite = player.image_dict["sword_med_r"]
	if(player.sword_height == 3 and player.direction_facing == 1):
		player.sprite = player.image_dict["sword_high_r"]
	if(player.sword_height == 1 and player.direction_facing == 0):
		player.sprite = player.image_dict["sword_low_l"]
	if(player.sword_height == 2 and player.direction_facing == 0):
		player.sprite = player.image_dict["sword_med_l"]
	if(player.sword_height == 3 and player.direction_facing == 0):
		player.sprite = player.image_dict["sword_high_l"]

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
    
def setSkins(characterType):
    imagesDictionary = dict()
    if(characterType == "Montoya"):
        imagesDictionary = {"stand_l": "FillerSpriteL.png", "stand_r": "FillerSpriteR.png", "sword_high_l": "MontoyaHighL.png", "sword_high_r": "MontoyaHighR.png", "sword_med_l": "MontoyaMedL.png", "sword_med_r": "MontoyaMedR.png", "sword_low_l": "MontoyaLowL.png", "sword_low_r": "MontoyaLowR.png", "duck_l": "FillerSpriteL.png", "duck_r": "FillerSpriteR.png", "jump_l": "FillerSpriteL.png", "jump_r": "FillerSpriteR.png", "thrust_high_l": "FillerSpriteL.png", "thrust_high_r": "FillerSpriteR.png", "thrust_med_l": "FillerSpriteL.png", "thrust_med_r": "FillerSpriteR.png", "thrust_low_l": "FillerSpriteL.png", "thrust_low_r": "FillerSpriteR.png"}
        return imagesDictionary
    else:
        # set a default skin
        imagesDictionary = {"stand_l": "FillerSpriteL.png", "stand_r": "FillerSpriteR.png", "sword_high_l": "MontoyaHighL.png", "sword_high_r": "MontoyaHighR.png", "sword_med_l": "MontoyaMedL.png", "sword_med_r": "MontoyaMedR.png", "sword_low_l": "MontoyaLowL.png", "sword_low_r": "MontoyaLowR.png", "duck_l": "FillerSpriteL.png", "duck_r": "FillerSpriteR.png", "jump_l": "FillerSpriteL.png", "jump_r": "FillerSpriteR.png", "thrust_high_l": "FillerSpriteL.png", "thrust_high_r": "FillerSpriteR.png", "thrust_med_l": "FillerSpriteL.png", "thrust_med_r": "FillerSpriteR.png", "thrust_low_l": "FillerSpriteL.png", "thrust_low_r": "FillerSpriteR.png"}
        return imagesDictionary

def main():
	texture_pack = dict()
	#Initialize texture pack to handle loading, storing, and retrieving textures.

	#JZ Player 1 Vars
	p1ml = False
	p1mr = False
	p1mu = False
	setmovebool1 = True #these two vars help in determining if player 1's sword should be up or down
	setmovebool1b = True
	moving1time = 0
	moving2time = 0
	setjump1bool = True
	jumping1time = 0

	#Player 2 Variables (Test Version)
	p2ml = False
	p2mr = False
	p2mu = False
	setmovebool2 = True
	setmovebool2b = True
	setjump2bool = True
	jumping2time = 0

	#Player selection variable.
	selected_player = 1 #The other option is 2, for player 2
	print("starting")

	clock = pygame.time.Clock()
	window_size = (1000, 600)

	pygame.init()
	screen = pygame.display.set_mode(window_size, 0, 32)
    

	player1 = player.Player(400, 300, 1, 2, False, True, 'MontoyaMedR.png', setSkins("Montoya"))
	player2 = player.Player(600, 300, 1, 2, False, False, 'MontoyaMedL.png', setSkins("Montoya"))
	game = True

	while game:
		#Delta time is implemented to help make sure that player's models will move at the same speed regardless of monitor refresh rate and processor speed.
		#Could use further optimizing and troubleshooting.
		clock.tick(120)
		pressed = pygame.key.get_pressed()
		alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:  #WARNING: Do not hit q and switch players while pressing any other button or while current player is jumping. Will create buggy behavior.
					if selected_player == 1:
						selected_player = 2
					elif selected_player == 2:
						selected_player = 1
				if event.key == pygame.K_a:
					if selected_player == 1:
						p1ml=True
					elif selected_player == 2:
						p2ml=True
				if event.key == pygame.K_d:
					if selected_player == 1:
						p1mr=True
					elif selected_player == 2:
						p2mr=True
				if event.key == pygame.K_SPACE:
					if selected_player == 1:
						p1mu=True
					elif selected_player == 2:
						p2mu=True
				if event.key == pygame.K_s:
					if selected_player == 1:
						if player1.sword_height > 1:
							player1.lower_sword
						sword_positioning1(player1)
					elif selected_player == 2:
						if player2.sword_height > 1:
							player2.lower_sword
						sword_positioning1(player2)

				if event.key == pygame.K_w:
					if selected_player == 1:
						if player1.sword_height > 0:
							player1.raise_sword
						sword_positioning1(player1)
					elif selected_player == 2:
						if player2.sword_height > 0:
							player2.raise_sword
						sword_positioning1(player2)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					if selected_player == 1:
						p1ml=False
					elif selected_player == 2:
						p2ml=False
				if event.key == pygame.K_d:
					if selected_player == 1:
						p1mr=False
					elif selected_player == 2:
						p2mr=False
				if event.key == pygame.K_SPACE:
					if selected_player == 1:
						p1mu=False
					elif selected_player == 2:
						p2mu=False


		#NON EVENT BASED ACTIONS
		#Player 1 Sprite/Movement
		if selected_player == 1:
			if not p1mr and not p1ml:
				if setmovebool1:
					moving1time = time.time()
					setmovebool1 = False
				elif (time.time() - moving1time) >= 0.25:
					setmovebool1 = True
					sword_positioning1(player1)
			else:
				if setmovebool1b:
					moving1time = time.time()
					setmovebool1b = False
				elif (time.time() - moving1time) >= 0.25:
					setmovebool1b = True
					if p1ml:
						player1.sprite = player1.image_dict["stand_l"]
					if p1mr:
						player1.sprite = player1.image_dict["stand_r"]
				if p1ml:
					player1.moveLeft(time.time() - moving1time)
				if p1mr:
					player1.moveRight(time.time() - moving1time)
			if p1mu and player1.y_pos == 300:
				#switch to jump sprite, sword shouldnt be up
				if setjump1bool:
					jumping1time = time.time()
					setjump1bool = False
			if not setjump1bool:
				print("jumptime")
				player1.setYPos(player1.getYPos()- 1.0)
				if (time.time() - jumping1time) >= 0.5:
					setjump1bool = True
			if player1.getYPos() < 300:
				player1.setYPos(player1.getYPos()+ 0.4)
				if player1.getYPos() >300:
					player1.setYPos(300)

		#Player 2 Sprite Drawing/Movement
		elif selected_player == 2:  #We can start compressing some of these conditionals into separate functions for readability.
			if not p2mr and not p2ml:
				if setmovebool2:
					moving2time = time.time()
					setmovebool2 = False
				elif (time.time() - moving2time) >= 0.25:
					setmovebool2 = True
					sword_positioning1(player2)
			else:
				if setmovebool2b:
					moving2time = time.time()
					setmovebool2b = False
				elif (time.time() - moving2time) >= 0.25:
					setmovebool2b = True
					if p2ml:
						player2.sprite = player2.image_dict["stand_l"]
					if p2mr:
						player2.sprite = player2.image_dict["stand_r"]
				if p2ml:
					player2.moveLeft(time.time() - moving2time)
				if p2mr:
					player2.moveRight(time.time() - moving2time)
			if p2mu and player2.y_pos == 300:
				# switch to jump sprite, sword shouldnt be up
				if setjump2bool:
					jumping2time = time.time()
					setjump2bool = False
			if not setjump2bool:
				print("jumptime")
				player2.setYPos(player2.getYPos() - 1.0)
				if (time.time() - jumping2time) >= 0.5:
					setjump2bool = True
			if player2.getYPos() < 300:
				player2.setYPos(player2.getYPos() + 0.4)
				if player2.getYPos() > 300:
					player2.setYPos(300)

		screen.fill((255, 255, 255))
		screen.blit(get_image("UF_Background.png", texture_pack), (0,0))
		screen.blit(get_image(player1.sprite, texture_pack), (player1.getXPos(), player1.getYPos())) #(width, height)
		screen.blit(get_image(player2.sprite, texture_pack), (player2.getXPos(), player2.getYPos()))

		pygame.display.flip()

main()


# Sources:
# https://nerdparadise.com/programming/pygame/part2
