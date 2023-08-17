import pygame
import random

# Initialize pygame
pygame.init()

# Define colors using RGB values
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen dimensions
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20  # Size of each cell for the snake and food

# Define directions as (x, y) changes
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pySnake - @x86kingfischer")

# Function to draw the snake on the screen
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to draw the food on the screen
def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main game loop
def main():
    # Initial snake position and direction
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = RIGHT

    # Randomly place the food
    food = (random.randint(0, (WIDTH//CELL_SIZE) - 1), random.randint(0, (HEIGHT//CELL_SIZE) - 1))
    running = True

    while running:
        screen.fill(WHITE)  # Clear the screen

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT
                elif event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN

        # Move the snake
        head = snake[0]
        new_head = ((head[0] + direction[0]) % (WIDTH//CELL_SIZE), (head[1] + direction[1]) % (HEIGHT//CELL_SIZE))
        snake = [new_head] + snake[:-1]

        # Check if snake eats the food
        if new_head == food:
            snake.append(snake[-1])
            food = (random.randint(0, (WIDTH//CELL_SIZE) - 1), random.randint(0, (HEIGHT//CELL_SIZE) - 1))

        # Check for collisions with itself
        if new_head in snake[1:]:
            running = False

        # Draw everything
        draw_snake(snake)
        draw_food(food)

        pygame.display.flip()  # Update the display
        pygame.time.wait(100)  # Delay to make the game playable

    pygame.quit()  # Close the game window

if __name__ == "__main__":
    main()
