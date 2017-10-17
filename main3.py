import pygame

screenwidth = 1280
screenheight = 720

screen = pygame.display.set_mode((screenwidth, screenheight))

forest = pygame.image.load("img/forestoil.jpg")
totororight = pygame.image.load("img/totororight.png")
gameon = True

while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
    screen.blit(forest, (0, 0))
    screen.blit(totororight, (291, 402))
    pygame.display.update()