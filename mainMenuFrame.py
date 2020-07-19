import gameEngine
import pygame
import sys
import menuButtons
import pauseButtons
import gameFrame
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
    "credits_clicked": "Resources/Images/Buttons/CreditsButtonClicked.png"
}

menu_buttons = {
    "play_button": menuButtons.Button(button_sprites["play_unhighl"], 400, 300, 220, 50),
    "settings_button": menuButtons.Button(button_sprites["settings_unhighl"], 400, 400, 50, 50),
    "exit_button": menuButtons.Button(button_sprites["exit_unhighl"], 400, 500, 220, 50),
    "back_button": menuButtons.Button(button_sprites["back_unhighl"], 400, 500, 220, 50),
    "restart_button": menuButtons.Button(button_sprites["restart_unhighl"], 0, 0, 220, 50),
    "tutorial_button": menuButtons.Button(button_sprites["tutorial_unhighl"], 0, 0, 220, 50),
    "credits_button": menuButtons.Button(button_sprites["credits_unhighl"], 0, 0, 220, 50)
}

#Remember to change game state booleans when going between menus.
game_state = {
    "start": False,
    "exit": False,
    "settings": False,
    "back": False,
    "paused": False,
    "resume": False,
    "restart": False,
    "tutorial": False,
    "credits": False
}

images_dictionary = dict()
pygame.font.init()
lobster_font = pygame.font.Font("Resources/Lobster.ttf", 64)


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
        if menu_buttons["play_button"].button_rect.collidepoint(mx, my):
            menu_buttons["play_button"].sprite = button_sprites["play_highl"]
            if m1_clicked: #Mouse click inside of the button's sprite
                game_state["start"] = True
                menu_buttons["play_button"].sprite = button_sprites["play_clicked"]
        else:
            menu_buttons["play_button"].sprite = button_sprites["play_unhighl"]

        if menu_buttons["exit_button"].button_rect.collidepoint(mx, my):
            menu_buttons["exit_button"].sprite = button_sprites["exit_highl"]
            if m1_clicked:
                game_state["exit"] = True
                menu_buttons["exit_button"].sprite = button_sprites["exit_clicked"]
        else:
            menu_buttons["exit_button"].sprite = button_sprites["exit_unhighl"]
        if menu_buttons["settings_button"].button_rect.collidepoint(mx, my):
            menu_buttons["settings_button"].sprite = button_sprites["settings_highl"]
            if m1_clicked:
                game_state["settings"] = True
                menu_buttons["settings_button"].sprite = button_sprites["settings_clicked"]
        else:
            menu_buttons["settings_button"].sprite = button_sprites["settings_unhighl"]

        if menu_buttons["tutorial_button"].button_rect.collidepoint(mx, my):
            menu_buttons["tutorial_button"].sprite = button_sprites["tutorial_highl"]
            if m1_clicked:
                game_state["tutorial"] = True
                menu_buttons["tutorial_button"].sprite = button_sprites["tutorial_clicked"]
        else:
            menu_buttons["tutorial_button"].sprite = button_sprites["tutorial_unhighl"]

        if menu_buttons["credits_button"].button_rect.collidepoint(mx, my):
            menu_buttons["credits_button"].sprite = button_sprites["credits_highl"]
            if m1_clicked:
                game_state["credits"] = True
                menu_buttons["credits_button"].sprite = button_sprites["credits_clicked"]
        else:
            menu_buttons["credits_button"].sprite = button_sprites["credits_unhighl"]



        renderMenuButtons("Main", screen, menu_buttons)
        pygame.display.update()


        #Game state handling, i.e. changing menus, quitting, etc. in order to produce "button clicked" effect
        if game_state["start"]:
            pygame.time.delay(400)
            game_state["start"] = False #Reset game states to false.
            gameEngine.startGame(screen, 1, "Montoya", "Montoya", audio)
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
            pygame.quit()
            sys.exit()

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


        if menu_buttons["back_button"].button_rect.collidepoint(mx, my):
            menu_buttons["back_button"].sprite = button_sprites["back_highl"]
            if m1_clicked: #Mouse click inside of the button's sprite
                game_state["back"] = True
                menu_buttons["back_button"].sprite = button_sprites["back_clicked"]
        else:
            menu_buttons["back_button"].sprite = button_sprites["back_unhighl"]


        renderMenuButtons("Tutorial", screen, menu_buttons)
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


        if menu_buttons["back_button"].button_rect.collidepoint(mx, my):
            menu_buttons["back_button"].sprite = button_sprites["back_highl"]
            if m1_clicked: #Mouse click inside of the button's sprite
                game_state["back"] = True
                menu_buttons["back_button"].sprite = button_sprites["back_clicked"]
        else:
            menu_buttons["back_button"].sprite = button_sprites["back_unhighl"]


        renderMenuButtons("Credits", screen, menu_buttons)
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


        if menu_buttons["back_button"].button_rect.collidepoint(mx, my):
            menu_buttons["back_button"].sprite = button_sprites["back_highl"]
            if m1_clicked: #Mouse click inside of the button's sprite
                game_state["back"] = True
                menu_buttons["back_button"].sprite = button_sprites["back_clicked"]
        else:
            menu_buttons["back_button"].sprite = button_sprites["back_unhighl"]


        renderMenuButtons("Settings", screen, menu_buttons)
        pygame.display.update()

        if game_state["back"]:
            pygame.time.delay(400)
            game_state["back"] = False
            if game_state["paused"]:
                pauseMenu(screen)
            else:
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


        if menu_buttons["play_button"].button_rect.collidepoint(mx, my):
            menu_buttons["play_button"].sprite = button_sprites["play_highl"]
            if m1_clicked: #Mouse click inside of the button's sprite
                game_state["resume"] = True
                menu_buttons["play_button"].sprite = button_sprites["play_clicked"]
        else:
            menu_buttons["play_button"].sprite = button_sprites["play_unhighl"]

        if menu_buttons["exit_button"].button_rect.collidepoint(mx, my):
            menu_buttons["exit_button"].sprite = button_sprites["exit_highl"]
            if m1_clicked: #Mouse click inside of the button's sprite
                game_state["exit"] = True
                menu_buttons["exit_button"].sprite = button_sprites["exit_clicked"]
        else:
            menu_buttons["exit_button"].sprite = button_sprites["exit_unhighl"]

        if menu_buttons["restart_button"].button_rect.collidepoint(mx, my):
            menu_buttons["restart_button"].sprite = button_sprites["restart_highl"]
            if m1_clicked:  # Mouse click inside of the button's sprite
                game_state["restart"] = True
                menu_buttons["restart_button"].sprite = button_sprites["restart_clicked"]
        else:
            menu_buttons["restart_button"].sprite = button_sprites["restart_unhighl"]

        renderMenuButtons("Pause", screen, menu_buttons)
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
def renderMenuButtons(menu_name, screen, buttons):
    if menu_name == "Main":
        drawButton(buttons, screen, "play_button", 500, 330)
        drawButton(buttons, screen, "tutorial_button", 500, 400)
        drawButton(buttons,screen, "settings_button", 50, 545)
        drawButton(buttons, screen, "exit_button", 500, 540)
        drawButton(buttons, screen, "credits_button", 500, 470)
        #Draw the duel logo
        screen.blit(gameFrame.getImage("Resources/Images/MenuTitle.png", images_dictionary), (0,0))

    elif menu_name == "Settings":
        drawButton(buttons, screen, "back_button", 500, 450)

    elif menu_name == "Tutorial":
        #tutorial sprite draw
        screen.blit(gameFrame.getImage("Resources/Images/TutorialScreen.png", images_dictionary), (0,0))
        drawButton(buttons, screen, "back_button", 140, 555)

    elif  menu_name == "Credits":
        #blit credits screen here
        drawButton(buttons, screen, "back_button", 140, 555)

    elif menu_name == "Pause":
        drawButton(buttons, screen, "play_button", 500, 300)
        drawButton(buttons, screen, "restart_button", 500, 350)
        drawButton(buttons, screen, "exit_button", 500, 400)



    #Add new menus by adding elif's and creating a function that holds the menu loop.

def drawButton(buttons, screen, button_name, x_pos, y_pos): #This function was not working when I implemented it, need to find a better way to simplify rendering function.
    #Center the button on its x and y coordinates to make it flush with the window.
    buttons[button_name].button_rect.center = (x_pos, y_pos)
    #Blit it to the screen
    screen.blit(gameFrame.getImage(buttons[button_name].sprite, images_dictionary), (buttons[button_name].button_rect.x, buttons[button_name].button_rect.y))