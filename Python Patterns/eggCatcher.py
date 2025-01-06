import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Egg Catcher Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Basket settings
basket_width = 100
basket_height = 20
basket_speed = 10

# Egg settings
egg_width = 30
egg_height = 30
egg_speed = 5

# Fonts
font = pygame.font.SysFont("Arial", 24)

# Game variables
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_direction = 0  # 0: no movement, -1: left, 1: right

eggs = []
score = 0
missed_eggs = 0
max_missed = 5  # Number of eggs missed before game over
game_over = False

# Create the egg class
class Egg:
    def __init__(self):
        self.x = random.randint(0, WIDTH - egg_width)
        self.y = -egg_height
        self.speed = egg_speed

    def update(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, (self.x, self.y, egg_width, egg_height))

# Function to draw the basket
def draw_basket():
    pygame.draw.rect(screen, WHITE, (basket_x, basket_y, basket_width, basket_height))

# Function to display the score
def display_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Function to display the game over message
def display_game_over():
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))

# Main game loop
def game_loop():
    global basket_x, basket_direction, score, missed_eggs, game_over, eggs

    clock = pygame.time.Clock()

    # Main game loop
    while True:
        screen.fill(BLACK)  # Fill the screen with black

        # Check for game over
        if game_over:
            display_game_over()
            pygame.display.update()
            time.sleep(3)  # Wait for a few seconds before quitting
            break

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    basket_direction = -1
                elif event.key == pygame.K_RIGHT:
                    basket_direction = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    basket_direction = 0

        # Update basket position
        if basket_direction == -1 and basket_x > 0:
            basket_x -= basket_speed
        elif basket_direction == 1 and basket_x < WIDTH - basket_width:
            basket_x += basket_speed

        # Create new egg and update existing eggs
        if random.random() < 0.02:  # 2% chance to spawn an egg
            eggs.append(Egg())

        # Update eggs and check for catches
        for egg in eggs[:]:
            egg.update()
            egg.draw()

            # Check if egg caught by basket
            if (egg.y + egg_height >= basket_y and
                basket_x <= egg.x + egg_width and
                basket_x + basket_width >= egg.x):
                eggs.remove(egg)  # Remove the caught egg
                score += 1  # Increase the score
            # Check if egg missed (hit the ground)
            elif egg.y > HEIGHT:
                eggs.remove(egg)  # Remove the missed egg
                missed_eggs += 1
                if missed_eggs >= max_missed:
                    game_over = True  # Game over after too many missed eggs

        # Draw the basket
        draw_basket()

        # Display score
        display_score()

        # Update the display
        pygame.display.update()

        # Frame rate
        clock.tick(60)

# Start the game
game_loop()

# Quit pygame
pygame.quit()
