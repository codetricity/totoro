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

whitetotoro = pygame.image.load("img/whitetotorosmall.png")
whitetotoroRect = whitetotoro.get_rect(x=100, y=620)

totororect = totororight.get_rect()
# tree = pygame.image.load("img/elmtree.png")
bush = pygame.image.load("img/bush.png")
bushrect = bush.get_rect(x=1000, y=520)
bush2rect = bush.get_rect(x=2700, y=520)
bushCollisionRect = pygame.Rect(1000, 520, 120, 120)
bushCollisionRect.bottom = bushrect.bottom
bushCollisionRect2 = pygame.Rect(2700, 520, 120, 120)
bushCollisionRect2.bottom = bush2rect.bottom

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
jumpdirection = "stop"
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
            if event.key == pygame.K_SPACE:
                if jumpdirection == "stop":
                    jumpdirection = "up"
    
    screen.blit(forest, (backgroundx, 0))
    # screen.blit(tree, (treex, 250))
    screen.blit(totoro, totororect)
    screen.blit(whitetotoro, whitetotoroRect)
    screen.blit(bush, bushrect)
    screen.blit(bush, (bush2rect))
    
    
    if direction == "right":
        if backgroundx >= -4147 + 1280:
            backgroundx = backgroundx - speed
            bushrect.centerx = bushrect.centerx - speed - 2
            bushCollisionRect.centerx = bushrect.centerx
            bush2rect.centerx = bush2rect.centerx - speed - 2
            bushCollisionRect2.centerx = bush2rect.centerx
    if direction == "left":
        if not backgroundx >= 1:
            backgroundx = backgroundx + speed
            # treex = treex + 3
            bushrect.centerx = bushrect.centerx + speed + 2
            bushCollisionRect.centerx = bushrect.centerx
            bush2rect.centerx = bush2rect.centerx - speed - 2
            bushCollisionRect2.centerx = bush2rect.centerx
    if jumpdirection == "up":
        if totororect.top > 15:
            totororect.centery = totororect.centery - 5
            whitetotoroRect.centery = whitetotoroRect.centery - 5
        else:
            jumpdirection = "down"
    if jumpdirection == "down":
        if totororect.centery < 570:
            totororect.centery = totororect.centery + 3
            whitetotoroRect.centery = whitetotoroRect.centery + 3
        else:
            jumpdirection = "stop"
    
    if totororect.colliderect(bushCollisionRect):
        print("murp")
    if totororect.colliderect(bushCollisionRect2):
        print("meh")
    clock.tick(FPS)
    pygame.display.update()