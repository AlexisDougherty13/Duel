import player
import pygame
import os
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

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

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

	#JZ Player 1 Vars
	p1ml = False
	p1mr = False
	p1mu = False
	setmovebool1 = True #these two vars help in determining if player 1's sword should be up or down
	setmovebool1b = True
	moving1time = 0
	setjumpbool = True
	jumping1time = 0
	print("starting")


	screen_width = 1000
	screen_height = 600

	pygame.init()
	screen = pygame.display.set_mode((screen_width,screen_height))

	player1 = player.Player(500, 300, 1, 2, False, 'FillerSpriteMed.png')
	game = True
	while game:
		pressed = pygame.key.get_pressed()
		alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					p1ml=True
				if event.key == pygame.K_d:
					p1mr=True
				if event.key == pygame.K_SPACE:
					p1mu=True
				if event.key == pygame.K_s:
					if(player1.sword_height > 1):
						player1.lower_sword
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
				if event.key == pygame.K_w:
					if(player1.sword_height > 0):
						player1.raise_sword
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
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					p1ml=False
				if event.key == pygame.K_d:
					p1mr=False
				if event.key == pygame.K_SPACE:
					p1mu=False
			

		#NON EVENT BASED ACTIONS
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
				if p1ml:
					player1.sprite = "FillerSpriteR.png"
			if p1ml:
				player1.moveLeft(time.time() - moving1time)
			if p1mr:
				player1.moveRight(time.time() - moving1time)
		if p1mu and player1.y_pos == 300:
			#switch to jump sprite, sword shouldnt be up
			if setjumpbool:
				jumping1time = time.time()
				setjumpbool = False
		if not setjumpbool:
			print("jumptime")
			player1.setYPos(player1.getYPos()-0.9)
			if (time.time() - jumping1time) >= 0.5:
				setjumpbool = True
		if player1.getYPos() < 300:
			player1.setYPos(player1.getYPos()+0.4)
			if player1.getYPos() >300:
				player1.setYPos(300)


		screen.fill((255, 255, 255))

		screen.blit(get_image(player1.sprite), (player1.getXPos(), player1.getYPos())) #(width, height)


		pygame.display.flip()
	
main()


# Sources:
# https://nerdparadise.com/programming/pygame/part2
