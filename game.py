import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('Background.jpg')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('battleship.png')
playerX = 370
playerY = 500
playerX_change = 0

# Enemy
enemyimg = pygame.image.load('alien.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(30, 120)
enemyX_change = 0.2
enemyY_change = 30

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = 'ready'


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))


# Game Loop
running = True
while running:
    screen.fill((128, 0, 0))  # Maroon(dark red) color
    # Background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    # Get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement
    # Checking for boundaries
    playerX += playerX_change
    if playerX >= 736:
        playerX = 736
    elif playerX <= 0:
        playerX = 0
    player(playerX, playerY)

    # Enemy movement
    enemyX += enemyX_change
    if enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change
    elif enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    enemy(enemyX, enemyY)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    pygame.display.update()
