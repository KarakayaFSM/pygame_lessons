import pygame
import sys

pygame.init()
gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False

white = (255, 255,255)
black = (0,0,0)
blue =  (0,0,255)


clock = pygame.time.Clock()



x=30
y=30
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white) #ekranı her framede tekrar çizdiriyoruz
    pygame.draw.rect(gameDisplay, blue, [x,y,100,100]) #şekil herseferinde yeni konumunda çiziliyor
    x=x+1
    y=y+1

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
