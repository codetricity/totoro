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

totororect = totororight.get_rect()
# tree = pygame.image.load("img/elmtree.png")
bush = pygame.image.load("img/bush.png")
bushrect = bush.get_rect(x=1000, y=520)
bush2rect = bush.get_rect(x=2300, y=520)

totoro = totororight

totorosong = pygame.mixer.Sound("snd/totoro-song.wav")
totorosong.play()

totororect.centerx = 291
totororect.centery = 570

# treex = 1000
bushx = 1000
backgroundx = 0

speed = 1
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
    screen.blit(totoro, totororect)
    screen.blit(bush, bushrect)
    screen.blit(bush, (bush2rect))
    
    
    if direction == "right":
        if backgroundx >= -4147 + 1280:
            backgroundx = backgroundx - speed
            bushrect.centerx = bushrect.centerx - speed - 2
            bush2rect.centerx = bush2rect.centerx - speed - 2
    if direction == "left":
        if not backgroundx >= 1:
            backgroundx = backgroundx + speed
            # treex = treex + 3
            bushrect.centerx = bushrect.centerx + speed + 2
            bush2rect.centerx = bush2rect.centerx - speed - 2
    
    if totororect.colliderect(bushrect):
        print("murp")
    if totororect.colliderect(bush2rect):
        print("meh")
    clock.tick(FPS)
    pygame.display.update()