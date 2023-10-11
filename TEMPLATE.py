import pygame
import os

# Initialize Pygame
pygame.init()

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

# Load bullet images
BULLET_WIDTH, BULLET_HEIGHT = 10, 3
YELLOW_BULLET = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
YELLOW_BULLET.fill((255, 255, 0))
RED_BULLET = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
RED_BULLET.fill((255, 0, 0))

# Initial spaceship positions
yellow_x, yellow_y = 100, 300
red_x, red_y = 800, 300
# Spaceship speed
SPACESHIP_SPEED = 5

# Bullet speed
BULLET_SPEED = 7
YELLOW_BULLETS = []
RED_BULLETS = []

# Initialize points
yellow_points = 0
red_points = 0

# Create fonts for displaying points
font = pygame.font.Font(pygame.font.get_default_font(), 36)

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SHIP, (yellow_x, yellow_y))
    WIN.blit(RED_SHIP, (red_x, red_y))
    for bullet in YELLOW_BULLETS:
        WIN.blit(YELLOW_BULLET, (bullet[0], bullet[1]))
    for bullet in RED_BULLETS:
        WIN.blit(RED_BULLET, (bullet[0], bullet[1]))

    # Display points on the screen
    yellow_points_text = font.render(f"Yellow: {yellow_points}", True, (255, 255, 0))
    red_points_text = font.render(f"Red: {red_points}", True, (255, 0, 0))
    WIN.blit(yellow_points_text, (10, 10))
    WIN.blit(red_points_text, (WIDTH - 150, 10))

    pygame.display.update()

def handle_movement(keys_pressed):
    global yellow_x, yellow_y, red_x, red_y

    # Yellow spaceship controls
    if keys_pressed[pygame.K_a] and yellow_x > 0:  # A key
        yellow_x -= SPACESHIP_SPEED
    if keys_pressed[pygame.K_d] and yellow_x + SPACESHIP_WIDTH < WIDTH:  # D key
        yellow_x += SPACESHIP_SPEED
    if keys_pressed[pygame.K_w] and yellow_y > 0:  # W key
        yellow_y -= SPACESHIP_SPEED
    if keys_pressed[pygame.K_s] and yellow_y + SPACESHIP_HEIGHT < HEIGHT:  # S key
        yellow_y += SPACESHIP_SPEED

    # Red spaceship controls
    if keys_pressed[pygame.K_LEFT] and red_x > 0:  # Left Arrow
        red_x -= SPACESHIP_SPEED
    if keys_pressed[pygame.K_RIGHT] and red_x + SPACESHIP_WIDTH < WIDTH:  # Right Arrow
        red_x += SPACESHIP_SPEED
    if keys_pressed[pygame.K_UP] and red_y > 0:  # Up Arrow
        red_y -= SPACESHIP_SPEED
    if keys_pressed[pygame.K_DOWN] and red_y + SPACESHIP_HEIGHT < HEIGHT:  # Down Arrow
        red_y += SPACESHIP_SPEED

def handle_shooting(keys_pressed):
    global YELLOW_BULLETS, RED_BULLETS

    if keys_pressed[pygame.K_SPACE]:
        # Shoot a bullet from the yellow spaceship
        yellow_bullet = [yellow_x + SPACESHIP_WIDTH, yellow_y + SPACESHIP_HEIGHT // 2 - BULLET_HEIGHT // 2]
        YELLOW_BULLETS.append(yellow_bullet)

    if keys_pressed[pygame.K_RCTRL]:
        # Shoot a bullet from the red spaceship
        red_bullet = [red_x - BULLET_WIDTH, red_y + SPACESHIP_HEIGHT // 2 - BULLET_HEIGHT // 2]
        RED_BULLETS.append(red_bullet)

def move_bullets():
    global YELLOW_BULLETS, RED_BULLETS

    for bullet in YELLOW_BULLETS:
        bullet[0] += BULLET_SPEED

    for bullet in RED_BULLETS:
        bullet[0] -= BULLET_SPEED

    # Remove bullets that go off-screen
    YELLOW_BULLETS = [bullet for bullet in YELLOW_BULLETS if 0 < bullet[0] < WIDTH]
    RED_BULLETS = [bullet for bullet in RED_BULLETS if 0 < bullet[0] < WIDTH]

def check_collisions():
    global yellow_points, red_points

    # Check if a yellow bullet hits the red spaceship
    for bullet in YELLOW_BULLETS:
        if red_x < bullet[0] + BULLET_WIDTH < red_x + SPACESHIP_WIDTH and red_y < bullet[1] < red_y + SPACESHIP_HEIGHT:
            yellow_points += 1
            YELLOW_BULLETS.remove(bullet)

    # Check if a red bullet hits the yellow spaceship
    for bullet in RED_BULLETS:
        if yellow_x < bullet[0] < yellow_x + SPACESHIP_WIDTH and yellow_y < bullet[1] < yellow_y + SPACESHIP_HEIGHT:
            red_points += 1
            RED_BULLETS.remove(bullet)

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
        handle_shooting(keys_pressed)
        move_bullets()
        check_collisions()
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
