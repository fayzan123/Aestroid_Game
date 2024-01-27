import sys
import pygame
import random

# Variable list: screen dimensions, game speeds, fonts, background images, colours used
pygame.init()
screen_width = 800
screen_height = 512
FPS = 30
aestroid_speed = 25
black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
clock = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((screen_width, screen_height))
smallfont = pygame.font.Font(None, 28)
menufont = pygame.font.Font(None, 48)
rocket = pygame.image.load('ROCKETREDD.png')
background = pygame.image.load('space.png')
aestroid = pygame.image.load('aestroid.png')
pygame.mixer.music.load("spacemusic.mp3")
crash_sound = pygame.mixer.Sound("crash.mp3")


# Quit game function
def quit_game():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# Main gameloop function
def gameloop():
    #music plays
    pygame.mixer.music.play(-1)
    # rocketship dimensions
    rect = rocket.get_rect()
    rect.x = 200
    rect.y = 400
    # velocity of how fast the rokcetship can manuever
    vel = 12
    # astroid dimensions
    roid_rect = aestroid.get_rect()
    roid_rect.x = random.randrange(0, screen_width)
    roid_rect.y = 50
    dodged = 0
    # how fast the astroid falls from a random position
    aestroid_speed = 21
    gameExit = False
    #get the hitbox for the rocket and asteroid. use random module to get asteroid to fall at random place on the width of the screen_height
    #dodged = 0 initializes counter for amount of objects dodged
    while not gameExit:
        quit_game()
        DISPLAY.fill(white)
        DISPLAY.blit(background, (0,0))
        #fills screen white and blits background of space
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_LEFT]:
            rect.x -= vel
        if userInput[pygame.K_RIGHT]:
            rect.x += vel
        #get user input of left or right keys
        # if userInput [pygame.K_UP]:
        # rect.y -= vel
        # if userInput [pygame.K_DOWN]:
        # rect.y += vel
        #in case we want user to be able to move up and down

        roid_rect.y = roid_rect.y + aestroid_speed
        if roid_rect.y > screen_height:
            roid_rect.x = random.randrange(0, screen_width)
            roid_rect.y = -25
            dodged += 1
        #conditional for asteroid falling at random position along the screen width

        DISPLAY.blit(rocket, rect)
        DISPLAY.blit(aestroid, roid_rect)
        #blit the asteroid and rocket to the screen, init their hitboxes
        aestroids_dodged(dodged)
        #run asteroid dodged function to get how many have been dodged onto screen

        if rect.colliderect(roid_rect) or vel > screen_width - rect.x or vel < 0 - rect.x:
            pygame.mixer.Sound.play(crash_sound)
            endmenu(dodged)
        #conditional to end the game, if the rocket collides with asteroid, or side of screen



        pygame.time.delay(30)
        pygame.display.update()
        # start = menufont.render('PLAY AGAIN',True,black)
        # quit = menufont.render('QUIT GAME',True,black)

# The score in the top left corner of the sceen for every time the user dodges astroid
def aestroids_dodged(count):
    text = smallfont.render('Dodged: ' + str(count), True, white)
    DISPLAY.blit(text, (0, 0))

# The final score that is displayed for when the game is over
def final_score(count):
    text = smallfont.render('ASTEROIDS DODGED: ' + str(count), True, white)
    DISPLAY.blit(text, (100, 300))

# Start menu function
def startmenu():
    point = 0
    # while loop to start the code until a user presses either start game or quit game
    while 1:
        DISPLAY.fill(black)
        if point == 0:
            # Start, quit, rules variables
            start = menufont.render('START GAME', True, blue)
            quit = menufont.render('QUIT GAME', True, white)
            rules = smallfont.render('RULES: Dodge the Asteroid Using Left and Right Arrow Keys', True, white)
            rules2 = smallfont.render('Dont Hit the Edges!', True, white)
        elif point == 1:
            # When the user clicks to the other option the text changes from white to blue
            start = menufont.render('START GAME', True, white)
            quit = menufont.render('QUIT GAME', True, blue)
            # Displays where the start & quit options are as well as the rules are displayed
        DISPLAY.blit(start, (screen_width / 10, screen_height / 10))
        DISPLAY.blit(quit, (screen_width / 10, 3 * screen_height / 10))
        DISPLAY.blit(rules, (50,250))
        DISPLAY.blit(rules2, (50, 300))
        # For loop to see what keys the user are pressing and gives the desired output based on the keys pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    point += 1
                elif event.key == pygame.K_UP:
                    point -= 1
                elif event.key == pygame.K_RETURN:
                    if point == 0:
                        gameloop()
                        # break
                    elif point == 1:
                        pygame.quit()
                        sys.exit()

        point = point % 2
        clock.tick(FPS)
        pygame.display.update()

#uses same function as start menu with different text, says (play again) instead of (start game)
def endmenu(count):
    pygame.mixer.music.stop()
    DISPLAY.fill(black)
    loose = smallfont.render('YOU CRASHED!', True, white)
    DISPLAY.blit(loose, (100, 250))
    final_score(count)
    point = 0
    while 1:
        if point == 0:
            start = menufont.render('PLAY AGAIN', True, blue)
            quit = menufont.render('QUIT GAME', True, white)
        elif point == 1:
            start = menufont.render('PLAY AGAIN', True, white)
            quit = menufont.render('QUIT GAME', True, blue)
        DISPLAY.blit(start, (screen_width / 10, screen_height / 10))
        DISPLAY.blit(quit, (screen_width / 10, 3 * screen_height / 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    point += 1
                elif event.key == pygame.K_UP:
                    point -= 1
                elif event.key == pygame.K_RETURN:
                    if point == 0:
                        gameloop()
                    elif point == 1:
                        pygame.quit()
                        sys.exit()
        point = point % 2
        clock.tick(FPS)
        pygame.display.update()

#run functions in order for initial startup
startmenu()
pygame.quit()
quit()