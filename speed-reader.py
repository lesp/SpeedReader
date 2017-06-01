import pygame
import time

pygame.font.init()
screen = pygame.display.set_mode((800,600))
background = (0, 0, 0)
screen.fill((background))
myfont = pygame.font.Font(None, 90)
f = open("/home/les/text.txt","r")
for line in f:
    for word in line.split():
        text = myfont.render(word,1,(0,255,0))
        screen.blit(text, (300,300))
        pygame.display.update()
        time.sleep(0.2)
        screen.fill((background))
        pygame.display.update()
pygame.display.quit()
