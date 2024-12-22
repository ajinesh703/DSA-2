import random
import os
import time

# Grid dimensions
GRID_SIZE = 10

# Initialize the grid
def create_grid(snake, food):
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for segment in snake:
        grid[segment[0]][segment[1]] = 'S'
    grid[food[0]][food[1]] = 'F'
    return grid

# Display the grid
def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join(row))

# Generate random food position
def generate_food(snake):
    while True:
        food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if food not in snake:
            return food

# Main game logic
def play_game():
    # Initial snake position and food
    snake = [(5, 5)]
    food = generate_food(snake)
    direction = 'RIGHT'

    while True:
        grid = create_grid(snake, food)
        display_grid(grid)
        print("Score:", len(snake) - 1)

        # Input direction
        new_direction = input("Enter direction (W/A/S/D): ").strip().upper()
        if new_direction in ['W', 'A', 'S', 'D']:
            direction = new_direction

        # Move the snake
        head = snake[0]
        if direction == 'W':
            new_head = (head[0] - 1, head[1])
        elif direction == 'S':
            new_head = (head[0] + 1, head[1])
        elif direction == 'A':
            new_head = (head[0], head[1] - 1)
        elif direction == 'D':
            new_head = (head[0], head[1] + 1)

        # Check for collisions
        if (
            new_head[0] < 0 or new_head[0] >= GRID_SIZE or
            new_head[1] < 0 or new_head[1] >= GRID_SIZE or
            new_head in snake
        ):
            print("Game Over! Your score is:", len(snake) - 1)
            break

        # Move snake
        snake.insert(0, new_head)
        if new_head == food:
            food = generate_food(snake)
        else:
            snake.pop()

        time.sleep(0.2)

if __name__ == "__main__":
    play_game()
