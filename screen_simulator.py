import pygame

pygama.init()

multiplier = 2
screen = pygame.display.set_mode((119*multiplier, 35*multiplier))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
