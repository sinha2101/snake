import pygame
import time
import random

# Initialize pygame
pygame.init()

# Game Window Size
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)

# Snake Settings
snake_size = 10
snake_speed = 15

# Fonts
font = pygame.font.SysFont("bahnschrift", 25)

# Function to Display Score
def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    win.blit(text, [10, 10])

# Main Game Function
def game():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    snake = []
    length = 1

    # Generate Food
    food_x = round(random.randrange(0, WIDTH - snake_size) / 10.0) * 10
    food_y = round(random.randrange(0, HEIGHT - snake_size) / 10.0) * 10

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            win.fill(BLACK)
            text = font.render("Game Over! Press C to Play Again or Q to Quit", True, RED)
            win.blit(text, [WIDTH // 6, HEIGHT // 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -snake_size, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = snake_size, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -snake_size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, snake_size

        # Update Snake Position
        x += dx
        y += dy

        # Check Boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Draw Game
        win.fill(BLACK)
        pygame.draw.rect(win, RED, [food_x, food_y, snake_size, snake_size])

        # Update Snake Body
        snake_head = [x, y]
        snake.append(snake_head)
        if len(snake) > length:
            del snake[0]

        # Check for Collision with Itself
        for block in snake[:-1]:
            if block == snake_head:
                game_close = True

        # Draw Snake
        for block in snake:
            pygame.draw.rect(win, GREEN, [block[0], block[1], snake_size, snake_size])

        # Check Food Collision
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_size) / 10.0) * 10
            food_y = round(random.randrange(0, HEIGHT - snake_size) / 10.0) * 10
            length += 1

        # Show Score
        show_score(length - 1)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the Game
game()
