import pygame
from functions import draw_bg
from functions import draw_snake
from functions import move
from functions import change_direction
from functions import draw_apple
from functions import apple_eat
from functions import lose

from time import sleep
from os   import startfile


screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
pygame.display.set_caption("Snake by Silentium")

pixels = [(5,10),(6,10),(7,10)]
direction = 'E'
apple = (14,10)

en_jeu = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and en_jeu == False:
            en_jeu = True
    
    if en_jeu :
        direction = change_direction(direction)
        pixels = list(move(pixels, direction))
        apple, stop = apple_eat(apple, pixels)
        
    draw_bg(screen)
    draw_snake(screen, pixels)
    draw_apple(screen, apple)
    lose(pixels)
    
    if not en_jeu : pygame.display.flip()
    
    if en_jeu :
        
        if pixels[len(pixels)-1][0] < 0 or pixels[len(pixels)-1][0] > 19 or pixels[len(pixels)-1][1] < 0 or pixels[len(pixels)-1][1] > 19 or stop == True:
            sleep(0.5)
            running = False
        
        else :
            pygame.display.flip()
            sleep(0.1)

pygame.quit()

meilleur_score = False
with open("assets.txt", 'a') : pass
with open("assets.txt", 'r') as fic:
    content = int(fic.readline())
    if len(pixels) > content :
        meilleur_score = True

if meilleur_score :
    with open("assets.txt", 'w') as fic :
        fic.write(str(len(pixels)))

with open("assets.txt", 'r') as fic:
    content = int(fic.readline())

with open("msg.vbs", 'a') : pass
with open("msg.vbs", 'w') as fic:
    chaine = 'a = MsgBox ("SCORE : ' + str(len(pixels)) + ' , BEST SCORE : ' + str(content) + '", vbOK, "SNAKE SAYS")'
    fic.write(chaine)

startfile("msg.vbs")
