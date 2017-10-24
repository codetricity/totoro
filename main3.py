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
acorns = pygame.image.load("img/acorns.png")
acornsrect = acorns.get_rect(x=2000, y=220)

flute = pygame.image.load("img/flute.png")
fluterect = flute.get_rect(x=230, y=570)
fluteFollow = True

whitetotoro = pygame.image.load("img/whitetotorosmall.png")
whitetotoroRect = whitetotoro.get_rect(x=1400, y=620)
whitetotoroFollow = False

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

plop = pygame.mixer.Sound("snd/blop2.wav")
acornplay = False

totororect.centerx = 291
totororect.centery = 570

# treex = 1000
bushx = 1000
backgroundx = 0

speed = 1
direction = "right"
jumpdirection = "stop"
foregroundspeed = 2
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
    screen.blit(acorns, acornsrect)
    screen.blit(flute, fluterect)
    
    
    if direction == "right":
        if backgroundx >= -4147 + 1280:
            backgroundx = backgroundx - speed
            bushrect.centerx = bushrect.centerx - speed - foregroundspeed
            bushCollisionRect.centerx = bushrect.centerx
            bush2rect.centerx = bush2rect.centerx - speed - foregroundspeed
            bushCollisionRect2.centerx = bush2rect.centerx
            acornsrect.centerx = acornsrect.centerx - speed 
            if not whitetotoroFollow:
                whitetotoroRect.centerx = whitetotoroRect.centerx - speed - 1
            if not fluteFollow:
                fluterect.centerx = fluterect.centerx - speed - 1
    if direction == "left":
        if not backgroundx >= 1:
            backgroundx = backgroundx + speed
            # treex = treex + 3
            bushrect.centerx = bushrect.centerx + speed + foregroundspeed
            bushCollisionRect.centerx = bushrect.centerx
            bush2rect.centerx = bush2rect.centerx + speed + foregroundspeed
            bushCollisionRect2.centerx = bush2rect.centerx
            acornsrect.centerx = acornsrect.centerx + speed 
            if not whitetotoroFollow:
                whitetotoroRect.centerx = whitetotoroRect.centerx + speed + 1
            if not fluteFollow:
                fluterect.centerx = fluterect.centerx + speed + 1
    if jumpdirection == "up":
        if totororect.top > 15:
            totororect.centery = totororect.centery - 5
            
            if whitetotoroFollow:
                whitetotoroRect.centery = whitetotoroRect.centery - 5
            if fluteFollow:
                print(fluterect.centery)
                fluterect.centery = fluterect.centery - 5                                
        else:
            jumpdirection = "down"
    if jumpdirection == "down":
        if totororect.centery < 570:
            totororect.centery = totororect.centery + 3
            if whitetotoroFollow and whitetotoroRect.y < 620:
                whitetotoroRect.centery = whitetotoroRect.centery + 3
            if fluteFollow and fluterect.y < 570:
                fluterect.centery = fluterect.centery + 3
        else:
            jumpdirection = "stop"
    
    if totororect.colliderect(bushCollisionRect) or \
            (whitetotoroRect.colliderect(bushCollisionRect)):
        print("murp")
        fluteFollow = False
        fluterect.x = bushrect.x - 150
        fluterect.y = 650
    if totororect.colliderect(bushCollisionRect2) or \
            (whitetotoroRect.colliderect(bushCollisionRect2)):
        print("meh")
        whitetotoroFollow = False
        fluteFollow = False
        fluterect.x = bush2rect.x - 150
        fluterect.y = 650
    
    if totororect.colliderect(whitetotoroRect):
        whitetotoroFollow = True
        print("totoro follow")
        whitetotoroRect.y = 620
        # if (whitetotoroRect.centerx - totororect.centerx) > 140: 
            # whitetotoroRect.centerx = whitetotoroRect.centerx - speed - 1
        whitetotoroRect.centerx = totororect.centerx - 150
    
    if totororect.colliderect(fluterect) and not fluteFollow:
        fluteFollow = True
        fluterect.y = 570
        fluterect.centerx = totororect.centerx

    if totororect.colliderect(acornsrect):
        if not acornplay:
            plop.play()
            acornplay = True
    else:
        acornplay = False

    clock.tick(FPS)
    pygame.display.update()