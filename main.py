import pygame, sys

#general setup
pygame.init()
clock = pygame.time.Clock()

#screen
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Clicker')


while True:
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#window update
    pygame.display.flip()
    clock.tick(60)