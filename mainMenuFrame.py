import gameEngine
import pygame
import sys
import menuButtons
import gameFrame

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
    "restart_clicked": "Resources/Images/Buttons/RestartButtonClicked.png"
}

menu_buttons = {
    "play_button": menuButtons.Button(button_sprites["play_unhighl"], 400, 300, 220, 50),
    "settings_button": menuButtons.Button(button_sprites["settings_unhighl"], 400, 400, 220, 50),
    "exit_button": menuButtons.Button(button_sprites["exit_unhighl"], 400, 500, 220, 50),
    "back_button": menuButtons.Button(button_sprites["back_unhighl"], 400, 500, 220, 50),
    "restart_button": menuButtons.Button(button_sprites["restart_unhighl"], 0, 0, 220, 50)
}

#Remember to change game state booleans when going between menus.
game_state = {
    "start": False,
    "exit": False,
    "settings": False,
    "back": False,
    "paused": False,
    "restart": False
}

images_dictionary = dict()

def mainMenu(screen):

    #Menu loop
    while True:
        screen.fill((0,0,0)) #Temporary black background
        mx, my = pygame.mouse.get_pos()

        m1_clicked = False
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    m1_clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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



        renderMenuButtons("Main", screen, menu_buttons)
        pygame.display.update()


        #Game state handling, i.e. changing menus, quitting, etc. in order to produce "button clicked" effect
        if game_state["start"]:
            pygame.time.delay(400)
            game_state["start"] = False #Reset game states to false.
            gameEngine.startGame(screen, 1, "Montoya", "Montoya")
        if game_state["settings"]:
            pygame.time.delay(400)
            game_state["settings"] = False
            settingsMenu(screen)
        if game_state["exit"]:
            pygame.time.delay(400)
            pygame.quit()
            sys.exit()


def settingsMenu(screen):

    #Menu loop
    while True:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()

        m1_clicked = False
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
                mainMenu(screen)

def pauseMenu(screen): #Only can be brought up once in game

    game_state["paused"] = True
    #Menu loop
    while True:
        mx, my = pygame.mouse.get_pos()

        m1_clicked = False
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    m1_clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state["back"] = True


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

        if menu_buttons["restart_button"].button_rect.collidepoint(mx, my):
            menu_buttons["restart_button"].sprite = button_sprites["restart_highl"]
            if m1_clicked:
                game_state["restart"] = True
                menu_buttons["restart_button"].sprite = button_sprites["restart_clicked"]
        else:
            menu_buttons["restart_button"].sprite = button_sprites["restart_unhighl"]


        renderMenuButtons("Pause", screen, menu_buttons)
        pygame.display.update()

        if game_state["start"]:
            pygame.time.delay(400)
            game_state["paused"] = False
            #resume game.
        if game_state["restart"]:
            pygame.time.delay(400)
            game_state["restart"] = False
            game_state["paused"] = False
            gameEngine.startGame(screen, 1, "Montoya", "Montoya")
        if game_state["settings"]:
            pygame.time.delay(400)
            game_state["settings"] = False
            settingsMenu(screen)
        if game_state["exit"]:
            pygame.time.delay(400)
            game_state["paused"] = False
            mainMenu(screen)



#Reusable render function that will render depending on which menu loop you are in.
def renderMenuButtons(menu_name, screen, buttons):
    if menu_name == "Main":
        #drawButton(buttons, screen, "play_button")
        buttons["play_button"].button_rect.center = (500, 350)
        screen.blit(gameFrame.getImage(buttons["play_button"].sprite, images_dictionary), (buttons["play_button"].button_rect.x, buttons["play_button"].button_rect.y))
        buttons["settings_button"].button_rect.center = (500, 450)
        screen.blit(gameFrame.getImage(buttons["settings_button"].sprite, images_dictionary), (buttons["settings_button"].button_rect.x, buttons["settings_button"].button_rect.y))
        buttons["exit_button"].button_rect.center = (500, 550)
        screen.blit(gameFrame.getImage(buttons["exit_button"].sprite, images_dictionary), (buttons["exit_button"].button_rect.x, buttons["exit_button"].button_rect.y))
        #Draw the duel logo
        screen.blit(gameFrame.getImage("Resources/Images/MenuTitle.png", images_dictionary), (0,0))

    elif menu_name == "Settings":
        buttons["back_button"].button_rect.center = (500, 450)
        screen.blit(gameFrame.getImage(buttons["back_button"].sprite, images_dictionary), (buttons["back_button"].button_rect.x, buttons["back_button"].button_rect.y))

    elif menu_name == "Pause":
        buttons["play_button"].button_rect.center = (500, 300)
        screen.blit(gameFrame.getImage(buttons["play_button"].sprite, images_dictionary), (buttons["play_button"].button_rect.x, buttons["play_button"].button_rect.y))
        buttons["settings_button"].button_rect.center = (500, 400)
        screen.blit(gameFrame.getImage(buttons["settings_button"].sprite, images_dictionary), (buttons["settings_button"].button_rect.x, buttons["settings_button"].button_rect.y))
        buttons["exit_button"].button_rect.center = (500, 500)
        screen.blit(gameFrame.getImage(buttons["exit_button"].sprite, images_dictionary), (buttons["exit_button"].button_rect.x, buttons["exit_button"].button_rect.y))

    #Add new menus by adding elif's and creating a function that holds the menu loop.

def drawButton(buttons, screen, button_name): #This function was not working when I implemented it, need to find a better way to simplify rendering function.
    #Center the button on its x and y coordinates to make it flush with the window.
    buttons[button_name].button_rect.center = (buttons[button_name].button_rect.x, buttons[button_name].button_rect.y)
    #Blit it to the screen
    screen.blit(gameFrame.getImage(buttons[button_name].sprite, images_dictionary), (buttons[button_name].button_rect.x, buttons[button_name].button_rect.y))