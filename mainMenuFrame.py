import gameEngine
import pygame
import sys
import menuButtons
import pauseButtons
import gameFrame
import audioEngine
from audioEngine import AudioEngine


#To-do: create a function that checks for button sprite changes based on mx and my and an inputted string.

button_sprites = {
    "play_unhighl" : "Resources/Images/Buttons/PlayButtonUnhighlighted.png",
    "play_highl": "Resources/Images/Buttons/PlayButtonHighlighted.png",
    "play_clicked": "Resources/Images/Buttons/PlayButtonClicked.png",
    "exit_unhighl": "Resources/Images/Buttons/ExitButtonUnhighlighted.png",
    "exit_highl": "Resources/Images/Buttons/ExitButtonHighlighted.png",
    "exit_clicked": "Resources/Images/Buttons/ExitButtonClicked.png",
    "settings_unhighl": "Resources/Images/Buttons/SettingsButtonUnhighlighted.png",
    "settings_highl": "Resources/Images/Buttons/SettingsButtonHighlighted.png",
    "settings_clicked": "Resources/Images/Buttons/SettingsButtonClicked.png",
    "back_unhighl": "Resources/Images/Buttons/BackButtonUnhighlighted.png",
    "back_highl": "Resources/Images/Buttons/BackButtonHighlighted.png",
    "back_clicked": "Resources/Images/Buttons/BackButtonClicked.png",
    "restart_unhighl": "Resources/Images/Buttons/RestartButtonUnhighlighted.png",
    "restart_highl": "Resources/Images/Buttons/RestartButtonHighlighted.png",
    "restart_clicked": "Resources/Images/Buttons/RestartButtonClicked.png",
    "tutorial_unhighl": "Resources/Images/Buttons/TutorialButtonUnhighlighted.png",
    "tutorial_highl": "Resources/Images/Buttons/TutorialButtonHighlighted.png",
    "tutorial_clicked": "Resources/Images/Buttons/TutorialButtonClicked.png",
    "credits_unhighl": "Resources/Images/Buttons/CreditsButtonUnhighlighted.png",
    "credits_highl": "Resources/Images/Buttons/CreditsButtonHighlighted.png",
    "credits_clicked": "Resources/Images/Buttons/CreditsButtonClicked.png",
    "minus_unhighl": "Resources/Images/Buttons/MinusButtonUnhighlighted.png",
    "minus_highl": "Resources/Images/Buttons/MinusButtonHighlighted.png",
    "minus_clicked": "Resources/Images/Buttons/MinusButtonClicked.png",
    "plus_unhighl": "Resources/Images/Buttons/PlusButtonUnhighlighted.png",
    "plus_highl": "Resources/Images/Buttons/PlusButtonHighlighted.png",
    "plus_clicked": "Resources/Images/Buttons/PlusButtonClicked.png",
}

menu_buttons = {
    "play_button": menuButtons.Button(button_sprites["play_unhighl"], 400, 300, 220, 50),
    "settings_button": menuButtons.Button(button_sprites["settings_unhighl"], 400, 400, 50, 50),
    "exit_button": menuButtons.Button(button_sprites["exit_unhighl"], 400, 500, 220, 50),
    "back_button": menuButtons.Button(button_sprites["back_unhighl"], 400, 500, 220, 50),
    "restart_button": menuButtons.Button(button_sprites["restart_unhighl"], 0, 0, 220, 50),
    "tutorial_button": menuButtons.Button(button_sprites["tutorial_unhighl"], 0, 0, 220, 50),
    "credits_button": menuButtons.Button(button_sprites["credits_unhighl"], 0, 0, 220, 50),
    "minus_button": menuButtons.Button(button_sprites["minus_unhighl"], 0, 0, 50, 50),
    "plus_button": menuButtons.Button(button_sprites["plus_unhighl"], 0, 0, 50, 50)
}

#Remember to change game state booleans when going between menus.
game_state = {
    "start": False,
    "pregame": False,
    "exit": False,
    "settings": False,
    "back": False,
    "paused": False,
    "resume": False,
    "restart": False,
    "tutorial": False,
    "credits": False,
    "increase_volume": False,
    "decrease_volume": False
}

player_skins = list(["Montoya",
                   "Zoro"
                   ])

images_dictionary = dict()
pygame.font.init()
volume_font = pygame.font.Font("Resources/Lobster.ttf", 32)
settings_label_font = pygame.font.Font("Resources/Lobster.ttf", 42)

def mainMenu(screen, audio):
    #Menu loop
    while True:
        screen.fill((0,0,0)) #Temporary black background
        mx, my = pygame.mouse.get_pos()

        m1_clicked = False
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                audio.closeAudioEngine()
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    m1_clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    audio.closeAudioEngine()
                    pygame.mixer.quit()
                    pygame.quit()
                    sys.exit()


        #Button sprite changing with mouse interaction:
        checkCollision("play_button", "play", "pregame", mx, my, m1_clicked)
        checkCollision("exit_button", "exit", "exit", mx, my, m1_clicked)
        checkCollision("settings_button", "settings", "settings", mx, my, m1_clicked)
        checkCollision("tutorial_button", "tutorial", "tutorial", mx, my, m1_clicked)
        checkCollision("credits_button", "credits", "credits", mx, my, m1_clicked)

        renderMenuButtons("Main", screen)
        pygame.display.update()


        #Game state handling, i.e. changing menus, quitting, etc. in order to produce "button clicked" effect
        if game_state["pregame"]:
            pygame.time.delay(400)
            pregameMenu(screen, audio)
        if game_state["tutorial"]:
            pygame.time.delay(400)
            game_state["tutorial"] = False
            tutorialMenu(screen, audio)
        if game_state["credits"]:
            pygame.time.delay(400)
            creditsMenu(screen, audio)
        if game_state["settings"]:
            pygame.time.delay(400)
            game_state["settings"] = False
            settingsMenu(screen, audio)
        if game_state["exit"]:
            pygame.time.delay(400)
            audio.closeAudioEngine()
            pygame.mixer.quit()
            pygame.quit()
            sys.exit()

def pregameMenu(screen, audio):
    #String values to change based on user selection. Default values initially.
    p1_skin_selection = player_skins[0]
    p2_skin_selection = player_skins[0]
    map_selection = 1

    while True:
        screen.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()

        m1_clicked = False
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                audio.closeAudioEngine()
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    m1_clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state["back"] = True

        # Button sprite changing with mouse interaction:
        checkCollision("play_button", "play", "start", mx, my, m1_clicked)
        checkCollision("back_button", "back", "back", mx, my, m1_clicked)
        #Add arrow buttons that check for collisions.

        #Using arrow buttons, change the p1 r p2 skin string that is passed to the startGame() function. Same for map.

        renderMenuButtons("Pregame", screen)
        pygame.display.update()

        if game_state["start"]:
            pygame.time.delay(400)
            game_state["start"] = False
            game_state["pregame"] = False  # Reset game states to false.
            gameEngine.startGame(screen, map_selection, p1_skin_selection, p2_skin_selection, audio)
        if game_state["back"]:
            pygame.time.delay(400)
            game_state["back"] = False
            game_state["pregame"] = False
            mainMenu(screen, audio)




def tutorialMenu(screen, audio):

    while True:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()

        m1_clicked = False
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                audio.closeAudioEngine()
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    m1_clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state["back"] = True

        checkCollision("back_button", "back", "back", mx, my, m1_clicked)

        renderMenuButtons("Tutorial", screen)
        pygame.display.update()

        if game_state["back"]:
            pygame.time.delay(400)
            game_state["back"] = False
            mainMenu(screen, audio)

def creditsMenu(screen, audio):

    while True:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()

        m1_clicked = False
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                audio.closeAudioEngine()
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    m1_clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state["back"] = True

        checkCollision("back_button", "back", "back", mx, my, m1_clicked)

        renderMenuButtons("Credits", screen)
        pygame.display.update()

        if game_state["back"]:
            pygame.time.delay(400)
            game_state["back"] = False
            game_state["credits"] = False
            mainMenu(screen, audio)

def settingsMenu(screen, audio):

    #Menu loop
    while True:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()

        m1_clicked = False
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                audio.closeAudioEngine()
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    m1_clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state["back"] = True

        checkCollision("back_button", "back", "back", mx, my, m1_clicked)
        checkCollision("minus_button", "minus", "decrease_volume", mx, my, m1_clicked)
        checkCollision("plus_button", "plus", "increase_volume", mx, my, m1_clicked)

        renderMenuButtons("Settings", screen)

        volume = str(int(round(audio.getVolume(), 1)*100))
        volume_level = volume_font.render(volume, True, (255,255,255))
        volume_rect = volume_level.get_rect()
        volume_rect.center = (502, 350)
        screen.blit(volume_level, volume_rect)

        volume_text = settings_label_font.render("Music Volume", True, (255,255,255))
        volume_rect = volume_text.get_rect()
        volume_rect.center = (260, 350)
        screen.blit(volume_text, volume_rect)

        pygame.display.update()

        if game_state["decrease_volume"]:
            pygame.time.delay(200)
            audio.changeVolume(round(audio.getVolume() - 0.1, 1))
            game_state["decrease_volume"] = False
        if game_state["increase_volume"]:
            pygame.time.delay(200)
            audio.changeVolume(round(audio.getVolume() + 0.1, 1))
            game_state["increase_volume"] = False
        if game_state["back"]:
            pygame.time.delay(400)
            game_state["back"] = False
            mainMenu(screen, audio)

def pauseMenu(screen, p1_meta_info, p2_meta_info, audio):

    #Reset Player meta info to prevent infinite movement after unpausing.
    p1_meta_info["left"] = False
    p1_meta_info["right"] = False
    p1_meta_info["up"] = False
    p1_meta_info["down"] = False
    p2_meta_info["left"] = False
    p2_meta_info["right"] = False
    p2_meta_info["up"] = False
    p2_meta_info["down"] = False

    game_state["resume"] = False
    game_state["paused"] = True
    #Menu loop
    while True:
        mx, my = pygame.mouse.get_pos()

        m1_clicked = False
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                audio.closeAudioEngine()
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    m1_clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state["resume"] = True

        checkCollision("play_button", "play", "resume", mx, my, m1_clicked)
        checkCollision("exit_button", "exit", "exit", mx, my, m1_clicked)
        checkCollision("restart_button", "restart", "restart", mx, my, m1_clicked)

        renderMenuButtons("Pause", screen)
        pygame.display.update()

        if game_state["resume"]:
            pygame.time.delay(400)
            game_state["paused"] = False
            game_state["resume"] = False
            break

        if game_state["restart"]:
            pygame.time.delay(400)
            game_state["restart"] = False
            game_state["paused"] = False
            gameEngine.startGame(screen, 1, "Montoya", "Montoya", audio)
        #if game_state["settings"]:
            #pygame.time.delay(400)
            #game_state["settings"] = False
            #game_state["paused"] = True
            #settingsMenu(screen)
        if game_state["exit"]:
            pygame.time.delay(400)
            game_state["exit"] = False
            game_state["paused"] = False
            mainMenu(screen, audio)




#Reusable render function that will render depending on which menu loop you are in.
def renderMenuButtons(menu_name, screen):
    if menu_name == "Main":
        drawButton(screen, "play_button", 500, 330)
        drawButton(screen, "tutorial_button", 500, 400)
        drawButton(screen, "settings_button", 50, 542)
        drawButton(screen, "exit_button", 500, 540)
        drawButton(screen, "credits_button", 500, 470)
        #Draw the duel logo
        screen.blit(gameFrame.getImage("Resources/Images/MenuTitle.png", images_dictionary), (0,0))

    elif menu_name == "Pregame":
        drawButton(screen, "play_button", 850, 555)
        drawButton(screen, "back_button", 150, 555)

    elif menu_name == "Settings":
        drawButton(screen,"minus_button",415, 350)
        drawButton(screen,"plus_button", 585, 350)
        drawButton(screen, "back_button", 500, 450)

    elif menu_name == "Tutorial":
        #tutorial sprite draw
        screen.blit(gameFrame.getImage("Resources/Images/TutorialScreen.png", images_dictionary), (0,0))
        drawButton(screen, "back_button", 140, 555)

    elif  menu_name == "Credits":
        #blit credits screen here
        drawButton(screen, "back_button", 140, 555)

    elif menu_name == "Pause":
        drawButton(screen, "play_button", 500, 300)
        drawButton(screen, "restart_button", 500, 350)
        drawButton(screen, "exit_button", 500, 400)



    #Add new menus by adding elif's and creating a function that holds the menu loop.

def drawButton(screen, button_name, x_pos, y_pos): #This function was not working when I implemented it, need to find a better way to simplify rendering function.
    #Center the button on its x and y coordinates to make it flush with the window.
    menu_buttons[button_name].button_rect.center = (x_pos, y_pos)
    #Blit it to the screen
    screen.blit(gameFrame.getImage(menu_buttons[button_name].sprite, images_dictionary), (menu_buttons[button_name].button_rect.x, menu_buttons[button_name].button_rect.y))

def checkCollision(button_name,short_name, state, mx, my, m1_clicked):
    if menu_buttons[button_name].button_rect.collidepoint(mx, my):
        menu_buttons[button_name].sprite = button_sprites[short_name + "_highl"]
        if m1_clicked:  # Mouse click inside of the button's sprite
            game_state[state] = True
            menu_buttons[button_name].sprite = button_sprites[short_name + "_clicked"]
    else:
        menu_buttons[button_name].sprite = button_sprites[short_name + "_unhighl"]