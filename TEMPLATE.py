import pygame
import os
##a simple python lib for making 2d games
##interpreter===python 3.8.10 64 bit
WIDTH,HEIGHT=1000,600
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PYGAME")
WHITE=(255,255,255)
FPS=60
SPACESPACE_WIDTH,SPACESHIP_HEIGHT=55,40

YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SRINK=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESPACE_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SRINK=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESPACE_WIDTH,SPACESHIP_HEIGHT)),270)


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SRINK,(100,300))
    WIN.blit(RED_SRINK,(800,300))
    pygame.display.update()

def main():
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)     
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        
        draw_window()

    pygame.quit()

             
if __name__ == "__main__":
    main()
