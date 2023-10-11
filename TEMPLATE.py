import pygame
import os

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PYGAME")
WHITE = (255, 255, 255)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# Load spaceship images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# Initial spaceship positions
yellow_x, yellow_y = 100, 300
red_x, red_y = 800, 300
# Spaceship speed
SPACESHIP_SPEED = 5

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SHIP, (yellow_x, yellow_y))
    WIN.blit(RED_SHIP, (red_x, red_y))
    pygame.display.update()

def handle_movement(keys_pressed):
    global yellow_x, yellow_y, red_x, red_y

    # Yellow spaceship controls
    if keys_pressed[pygame.K_a]:  # A key
        yellow_x -= SPACESHIP_SPEED
    if keys_pressed[pygame.K_d]:  # D key
        yellow_x += SPACESHIP_SPEED
    if keys_pressed[pygame.K_w]:  # W key
        yellow_y -= SPACESHIP_SPEED
    if keys_pressed[pygame.K_s]:  # S key
        yellow_y += SPACESHIP_SPEED

    # Red spaceship controls
    if keys_pressed[pygame.K_LEFT]:  # Left Arrow
        red_x -= SPACESHIP_SPEED
    if keys_pressed[pygame.K_RIGHT]:  # Right Arrow
        red_x += SPACESHIP_SPEED
    if keys_pressed[pygame.K_UP]:  # Up Arrow
        red_y -= SPACESHIP_SPEED
    if keys_pressed[pygame.K_DOWN]:  # Down Arrow
        red_y += SPACESHIP_SPEED

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed)
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
