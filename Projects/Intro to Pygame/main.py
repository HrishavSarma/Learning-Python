from sys import exit
import pygame
import pygame.locals

pygame.init()

our_screen = pygame.display.set_mode((800,400), pygame.FULLSCREEN)
pygame.display.set_caption("Runner")

our_clock = pygame.time.Clock()

our_font = pygame.font.Font('assets/font/Pixeltype.ttf', 77) #(font_type, font_size)

sky_surface = pygame.image.load('assets/graphics/Sky.png').convert()

ground_surface = pygame.image.load('assets/graphics/ground.png').convert()

text_surface = our_font.render("WELCOME!", False, 'gray23') #(text, AA, color)
text_rect = text_surface.get_rect(center = (400,150))

snail_surface = pygame.image.load('assets/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surface = pygame.image.load('assets/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

x_surface = pygame.image.load('assets/graphics/X/x7.png').convert_alpha()
x_rect = x_surface.get_rect(topright = (785,10))

#Variables
velocity = 1
text_pos = text_rect.centery # holds the original value of text
target = text_rect.centery # holds where the text will go
snail_pos = snail_rect.left # holds the position of the snail

#triggers
text_triggered = False
player_triggered = False

while True:
    # this loop
    # draw all our elements
    # updates everything
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # pygame.quit() is polar opposite of pygame.init()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_triggered = True # triggers when clicked on the player
                print("M2P collision") # mouse to player
            if text_rect.collidepoint(event.pos): # triggers when clicked on the text
                 text_triggered = True
                 print("M2T collision") # mouse to text
            if x_rect.collidepoint(event.pos): # When X is pressed the game quits
                 pygame.quit()
                 exit()

    our_screen.blit(sky_surface,(0,0)) #block image transfer (surface, position)
    
    our_screen.blit(ground_surface,(0,300))
    
    # # Text movement
    # text_rect.centery += velocity
    # if text_rect.centery >= 155:
    #     velocity = -1
    # if text_rect.centery <=145:
    #     velocity = +1

    # Text pop
    # if text_rect.collidepoint(mouse_pos):
    #     text_rect.centery += velocity
    #     print(mouse_pos)
    #     if text_rect.centery >= 155:
    #         velocity = -1
    #     if text_rect.centery == 150:
    #         velocity = 0

    # Text bops when clicked on it
    if text_triggered:

        text_rect.centery += velocity

        if text_rect.centery == target+4:
             velocity = -1
             text_pos -= 5

        if text_rect.centery == target-2:
             velocity = 1
             text_pos += 5

        if text_rect.centery == text_pos:
             text_triggered = False
    our_screen.blit(text_surface, text_rect)

    # Moves snail when click on player
    if player_triggered:
        snail_rect.right -= 1
        if snail_rect.right <= 0: #for loop from right side
            snail_rect.left = 800
        if snail_rect.left == snail_pos-50: #goes towards the player 50 pixels
                player_triggered = False
                snail_pos -= 50
    our_screen.blit(snail_surface, snail_rect)

    our_screen.blit(player_surface, player_rect)

    our_screen.blit(x_surface,x_rect)

    # if player_rect.colliderect(snail_rect): #return 0 or 1 # rect to rect colli
    #     print('collision')

    # if player_rect.collidepoint(mouse_pos): # mouse to rect colli
    #     print('M2P collision')

    # if snail_rect.collidepoint(mouse_pos):
    #     print('M2S collision')

    pygame.display.update()
    our_clock.tick(60) #while loop should not run faster than 60 time per seconds or 1 while for every 17 miliseconds