import pygame
import math
import random
import time

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fidget Spinner Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Fidget spinner settings
spinner_radius = 60
spinner_center = (WIDTH // 2, HEIGHT // 2)
spinner_speed = 0  # Initial speed of the spinner
spinner_max_speed = 20  # Max speed of the spinner
spinner_deceleration = 0.1  # Speed reduction over time
spinner_angle = 0  # Initial angle of the spinner

# Fonts
font = pygame.font.SysFont("Arial", 24)

# Game variables
score = 0
game_over = False

# Function to draw the spinner
def draw_spinner(angle):
    # Draw spinner circle (the base)
    pygame.draw.circle(screen, BLUE, spinner_center, spinner_radius)
    
    # Draw the spinner blades (we'll use 3 blades for simplicity)
    blade_length = 80
    for i in range(3):
        # Calculate the angle of the blade
        blade_angle = math.radians(i * 120 + angle)
        x_end = spinner_center[0] + blade_length * math.cos(blade_angle)
        y_end = spinner_center[1] + blade_length * math.sin(blade_angle)
        pygame.draw.line(screen, WHITE, spinner_center, (x_end, y_end), 5)

# Function to update the spinner's speed
def update_speed(speed, deceleration):
    speed -= deceleration
    if speed < 0:
        speed = 0
    return speed

# Function to display the score
def display_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Main game loop
def game_loop():
    global spinner_speed, spinner_angle, score, game_over

    clock = pygame.time.Clock()

    while not game_over:
        screen.fill(BLACK)  # Fill the screen with black

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the player clicks the mouse, the spinner speed increases
                if event.button == 1:  # Left mouse button
                    if spinner_speed == 0:  # If the spinner was stopped, start spinning
                        spinner_speed = random.randint(10, spinner_max_speed)
                    else:
                        spinner_speed = min(spinner_speed + 5, spinner_max_speed)
                        score += 1  # Increase the score when spinner is clicked

        # Update spinner angle and speed
        spinner_angle += spinner_speed
        if spinner_angle >= 360:
            spinner_angle -= 360  # Keep the angle between 0 and 360 degrees
        
        # Draw the spinner and score
        draw_spinner(spinner_angle)
        display_score()

        # Slow down the spinner
        spinner_speed = update_speed(spinner_speed, spinner_deceleration)

        # Update the display
        pygame.display.update()

        # Frame rate
        clock.tick(60)

    # Display game over message when game ends
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, RED)
    screen.fill(BLACK)  # Clear the screen
    screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
    pygame.display.update()
    time.sleep(3)  # Wait for 3 seconds before quitting

# Start the game
game_loop()

# Quit pygame
pygame.quit()
