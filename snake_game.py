from browser import document, window

# Canvas settings
canvas = document["gameCanvas"]
context = canvas.getContext("2d")
canvas.width = 500
canvas.height = 500

# Initial game variables
snake = [(50, 50), (40, 50), (30, 50)]  # Snake body (starting position)
direction = "RIGHT"  # Initial movement direction
food = (80, 50)  # Initial food position
game_over = False  # Game over flag

# Snake size and speed
SNAKE_SIZE = 10
SNAKE_SPEED = 100  # Milliseconds between game loops

# Function to start a new game
def start_game(event):
    global snake, direction, food, game_over
    snake = [(50, 50), (40, 50), (30, 50)]  # Reset snake
    direction = "RIGHT"
    food = (80, 50)
    game_over = False
    game_loop()

# Game loop function
def game_loop():
    global snake, food, game_over

    if game_over:
        context.fillStyle = "red"
        context.font = "30px Arial"
        context.fillText("Game Over!", 150, 250)
        return

    # Clear the canvas
    context.clearRect(0, 0, canvas.width, canvas.height)

    # Update the snake's position based on direction
    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= SNAKE_SIZE
    elif direction == "DOWN":
        head_y += SNAKE_SIZE
    elif direction == "LEFT":
        head_x -= SNAKE_SIZE
    elif direction == "RIGHT":
        head_x += SNAKE_SIZE

    # Add new head to the snake
    snake = [(head_x, head_y)] + snake[:-1]

    # Check if the snake eats food
    if (head_x, head_y) == food:
        snake.append(snake[-1])  # Add a new segment to the snake
        food = generate_food()  # Generate new food position

    # Draw the snake
    context.fillStyle = "red"
    for segment in snake:
        context.fillRect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE)

    # Draw the food
    context.fillStyle = "green"
    context.fillRect(food[0], food[1], SNAKE_SIZE, SNAKE_SIZE)

    # Check if the snake collides with the walls or itself
    if head_x < 0 or head_x >= canvas.width or head_y < 0 or head_y >= canvas.height:
        game_over = True

    if (head_x, head_y) in snake[1:]:
        game_over = True

    # Continue the game loop
    window.setTimeout(game_loop, SNAKE_SPEED)

# Function to generate food at a random position
def generate_food():
    food_x = window.Math.floor(window.Math.random() * (canvas.width / SNAKE_SIZE)) * SNAKE_SIZE
    food_y = window.Math.floor(window.Math.random() * (canvas.height / SNAKE_SIZE)) * SNAKE_SIZE
    return (food_x, food_y)

# Event handler for keyboard input
def on_key(event):
    global direction

    # Prevent the snake from reversing
    if event.key == "ArrowUp" and direction != "DOWN":
        direction = "UP"
    elif event.key == "ArrowDown" and direction != "UP":
        direction = "DOWN"
    elif event.key == "ArrowLeft" and direction != "RIGHT":
        direction = "LEFT"
    elif event.key == "ArrowRight" and direction != "LEFT":
        direction = "RIGHT"

# Bind the start game function to the button click
document["start_button"].bind("click", start_game)

# Bind the key press event to change snake direction
document.bind("keydown", on_key)
