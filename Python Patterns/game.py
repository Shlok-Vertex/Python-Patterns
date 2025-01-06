import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 400

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player settings
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 7

# Block settings
block_width = 50
block_height = 50
block_speed = 5
block_frequency = 25  # Higher number means fewer blocks will spawn

# Set up fonts
font = pygame.font.SysFont(None, 35)

# Initialize clock
clock = pygame.time.Clock()

# Game loop flag
running = True

# List of falling blocks
blocks = []

# Function to display the score
def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Function to create new blocks
def create_block():
    x_pos = random.randint(0, WIDTH - block_width)
    y_pos = -block_height
    return [x_pos, y_pos]

# Function to move blocks
def move_blocks():
    for block in blocks:
        block[1] += block_speed

# Function to remove off-screen blocks
def remove_off_screen_blocks():
    global blocks
    blocks = [block for block in blocks if block[1] < HEIGHT]

# Function to check for collisions
def check_collision():
    global running
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    
    for block in blocks:
        block_rect = pygame.Rect(block[0], block[1], block_width, block_height)
        if player_rect.colliderect(block_rect):
            running = False  # End the game if collision happens

# Main game loop
score = 0
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses for movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Create new blocks periodically
    if random.randint(1, block_frequency) == 1:
        blocks.append(create_block())

    # Move and remove blocks
    move_blocks()
    remove_off_screen_blocks()

    # Check for collisions
    check_collision()

    # Update score
    score += 1

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

    # Draw blocks
    for block in blocks:
        pygame.draw.rect(screen, RED, (block[0], block[1], block_width, block_height))

    # Show the score
    show_score(score)

    # Update the screen
    pygame.display.update()

    # Control the game speed (frames per second)
    clock.tick(60)

# Quit pygame
pygame.quit()
