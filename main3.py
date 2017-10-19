import pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 30

screenwidth = 1280
screenheight = 720

screen = pygame.display.set_mode((screenwidth, screenheight))

forest = pygame.image.load("img/forestoil.jpg")
totororight = pygame.image.load("img/totororight.png")
totoroleft = pygame.image.load("img/totoroleft.png")
# tree = pygame.image.load("img/elmtree.png")
bush = pygame.image.load("img/bush.png")

totoro = totororight

totorosong = pygame.mixer.Sound("snd/totoro-song.wav")
totorosong.play()

totorox = 291
totoroy = 402

# treex = 1000
bushx = 1000
backgroundx = 0

direction = "right"
gameon = True

while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = "right"
                totoro = totororight
            if event.key == pygame.K_LEFT:
                direction = "left"
                totoro = totoroleft
    screen.blit(forest, (backgroundx, 0))
    # screen.blit(tree, (treex, 250))
    screen.blit(bush, (bushx, 520))
    screen.blit(totoro, (totorox, totoroy))
    
    if direction == "right":
        if backgroundx >= -4147 + 1280:
            backgroundx = backgroundx - 10
            bushx = bushx - 3
    if direction == "left":
        if not backgroundx >= 1:
            backgroundx = backgroundx + 1
            # treex = treex + 3
            bushx = bushx - 3

    print(backgroundx)
    clock.tick(FPS)
    pygame.display.update()