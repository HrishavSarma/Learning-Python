from sys import exit
import pygame
import pygame.locals

pygame.init()
our_screen = pygame.display.set_mode((800,400))
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

velocity = 1

while True:
    # this loop
    # draw all our elements
    # updates everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # pygame.quit() is polar opposite of pygame.init()
            exit()

    our_screen.blit(sky_surface,(0,0)) #block image transfer (surface, position)
    our_screen.blit(ground_surface,(0,300))
    
    text_rect.centery += velocity
    if text_rect.centery >= 155:
        velocity = -1
    if text_rect.centery <=145:
        velocity = +1

    our_screen.blit(text_surface, text_rect)

    snail_rect.right -= 1
    if snail_rect.right <= 0:
        snail_rect.left = 800
    our_screen.blit(snail_surface, snail_rect)

    player_rect.left += 1
    our_screen.blit(player_surface, player_rect)

    pygame.display.update()
    our_clock.tick(60) #while loop should not run faster than 60 time per seconds or 1 while for every 17 miliseconds