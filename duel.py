import player
import pygame
import os
import time

#GRACE TESTING- trying to figure out how to use github

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


def get_image(path, _image_library):
        if path not in _image_library:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path).convert_alpha()
                _image_library[path] = image
        return _image_library[path]


def sword_positioning1(player1):
	if(player1.sword_height == 1 and player1.direction_facing == 1):
		player1.sprite = "FillerSpriteLow.png"
	if(player1.sword_height == 2 and player1.direction_facing == 1):
		player1.sprite = "FillerSpriteMed.png"
	if(player1.sword_height == 3 and player1.direction_facing == 1):
		player1.sprite = "FillerSpriteHigh.png"
	if(player1.sword_height == 1 and player1.direction_facing == 0):
		player1.sprite = "FillerSpriteLowR.png"
	if(player1.sword_height == 2 and player1.direction_facing == 0):
		player1.sprite = "FillerSpriteMedR.png"
	if(player1.sword_height == 3 and player1.direction_facing == 0):
		player1.sprite = "FillerSpriteHighR.png"



def main():
	#Initialize texture pack to handle loading, storing, and retrieving textures.
	texture_pack = dict()
    
    imagesDictionary = dict()
    #texture_pack = {"stand_l": "", "stand_r": "", "sword_high_l": "skeletonHighL.png", 
    #"sword_high_r": "skeletonHighR.png", "sword_med_l": "skeletonMedL.png", "sword_med_r": "skeletonMedR.png", "sword_low_l": "skeletonLowR.png", "sword_low_r": "skeletonLowR.png", 
    #"duck_l": "", "duck_r": "", 
    #"jump_l": "", "jump_r": "", "thrust_high_l": "", "thrust_high_r": "", 
    #"thrust_med_l": "", "thrust_med_r": "", "thrust_low_l": "", "thrust_low_r": ""}
    
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


	screen_width = 1000
	screen_height = 600

	pygame.init()
	screen = pygame.display.set_mode((screen_width,screen_height))

	player1 = player.Player(400, 300, 1, 2, False, True, 'FillerSpriteMed.png')
	player2 = player.Player(600, 300, 1, 2, False, False, 'FillerSpriteMed.png')
	game = True

	while game:
		pressed = pygame.key.get_pressed()
		alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
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
						player1.sprite = "FillerSpriteL.png"
					if p1mr:
						player1.sprite = "FillerSpriteR.png"
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
				player1.setYPos(player1.getYPos()-0.9)
				if (time.time() - jumping1time) >= 0.5:
					setjump1bool = True
			if player1.getYPos() < 300:
				player1.setYPos(player1.getYPos()+0.4)
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
						player2.sprite = "FillerSpriteL.png"
					if p2mr:
						player2.sprite = "FillerSpriteR.png"
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
				player2.setYPos(player2.getYPos() - 0.9)
				if (time.time() - jumping2time) >= 0.5:
					setjump2bool = True
			if player2.getYPos() < 300:
				player2.setYPos(player2.getYPos() + 0.4)
				if player2.getYPos() > 300:
					player2.setYPos(300)
					
		screen.fill((255, 255, 255))

		screen.blit(get_image(player1.sprite, texture_pack), (player1.getXPos(), player1.getYPos())) #(width, height)
		screen.blit(get_image(player2.sprite, texture_pack), (player2.getXPos(), player2.getYPos()))

		pygame.display.flip()
	
main()


# Sources:
# https://nerdparadise.com/programming/pygame/part2
