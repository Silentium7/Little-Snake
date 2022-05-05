import pygame
from random import randint
from time   import sleep

def draw_bg(screen):
    if screen.get_width()>screen.get_height():
        pygame.draw.rect(screen, (0,255,0),(int((screen.get_width()-screen.get_height())/2),0,screen.get_height(),screen.get_height()))
    elif screen.get_width()<screen.get_height():
        pygame.draw.rect(screen, (0,255,0),(0,int((screen.get_height()-screen.get_width())/2),screen.get_width(),screen.get_width()))        
    else :
        pygame.draw.rect(screen, (0,255,0),(0,0,screen.get_width(),screen.get_height()))
    

def draw_snake(screen, pixels):
    if screen.get_width()>screen.get_height():
        for i in range(len(pixels)):
            pygame.draw.rect(screen, (0,0,255), (int(pixels[i][0]*screen.get_height()/20)+int((screen.get_width()-screen.get_height())/2), int(pixels[i][1]*screen.get_height()/20), int(screen.get_height()/20), int(screen.get_height()/20)))
    elif screen.get_width()<screen.get_height():
        for i in range(len(pixels)):
            pygame.draw.rect(screen, (0,0,255), (int(pixels[i][0]*screen.get_width()/20), int(pixels[i][1]*screen.get_width()/20)+int((screen.get_height()-screen.get_width())/2), int(screen.get_width()/20), int(screen.get_width()/20)))
    else :
        for i in range(len(pixels)):
            pygame.draw.rect(screen, (0,0,255), (int(pixels[i][0]*screen.get_width()/20), int(pixels[i][1]*screen.get_width()/20), int(screen.get_width()/20), int(screen.get_width()/20)))

def move(pixels, direction):
    pixels.remove(pixels[0])
    if direction == 'E': pixels.append((pixels[len(pixels)-1][0]+1, pixels[len(pixels)-1][1]))
    elif direction == 'O': pixels.append((pixels[len(pixels)-1][0]-1, pixels[len(pixels)-1][1]))
    elif direction == 'N': pixels.append((pixels[len(pixels)-1][0], pixels[len(pixels)-1][1]-1))
    elif direction == 'S': pixels.append((pixels[len(pixels)-1][0], pixels[len(pixels)-1][1]+1))
    return pixels

def change_direction(direction):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != 'S': direction = 'N'
    elif keys[pygame.K_DOWN] and direction != 'N': direction = 'S'
    elif keys[pygame.K_LEFT] and direction != 'E': direction = 'O'
    elif keys[pygame.K_RIGHT] and direction != 'O': direction = 'E'
    return direction

def draw_apple(screen, apple):
    if screen.get_width()>screen.get_height():
        pygame.draw.rect(screen, (255,0,0), (int(apple[0]*screen.get_height()/20)+int((screen.get_width()-screen.get_height())/2), int(apple[1]*screen.get_height()/20), int(screen.get_height()/20), int(screen.get_height()/20)))
    elif screen.get_width()<screen.get_height():
        pygame.draw.rect(screen, (255,0,0), (int(apple[0]*screen.get_width()/20), int(apple[1]*screen.get_width()/20)+int((screen.get_height()-screen.get_width())/2), int(screen.get_width()/20), int(screen.get_width()/20)))
    else :
        pygame.draw.rect(screen, (255,0,0), (int(apple[0]*screen.get_width()/20), int(apple[1]*screen.get_width()/20), int(screen.get_width()/20), int(screen.get_width()/20)))

def apple_eat(apple, pixels):
    stop = False
    if apple in pixels:
        apple = (randint(0,19),randint(0,19))
        pixels.append((pixels[len(pixels)-1][0],pixels[len(pixels)-1][1]))
    elif pixels[len(pixels)-1] in pixels[0:-1]:
        sleep(0.5)
        stop = True
    return apple, stop

def lose(pixels):
    pass