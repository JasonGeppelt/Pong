import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Paddle properties
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5  # Adjust paddle speed

# Ball properties
BALL_SIZE = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Initialize paddles
paddle_a = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Initialize ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_velocity = [BALL_SPEED_X, BALL_SPEED_Y]

# Score
score_a = 0
score_b = 0

# Font for displaying the score
font = pygame.font.Font(None, 36)

# Clock to control game speed
clock = pygame.time.Clock()
FPS = 60  # Adjust desired frames per second

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    keys = pygame.key.get_pressed()
    # Move paddles based on user input
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_a.bottom < HEIGHT:
        paddle_a.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b.y += PADDLE_SPEED

    # Move the ball
    ball.x += ball_velocity[0]
    ball.y += ball_velocity[1]

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_velocity[1] = -ball_velocity[1]

    # Ball collision with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_velocity[0] = -ball_velocity[0]

    # Ball out of bounds
    if ball.left <= 0:
        score_b += 1
        ball_velocity[0] = BALL_SPEED_X
        ball_velocity[1] = BALL_SPEED_Y
        ball.topleft = (WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2)
    elif ball.right >= WIDTH:
        score_a += 1
        ball_velocity[0] = -BALL_SPEED_X
        ball_velocity[1] = BALL_SPEED_Y
        ball.topleft = (WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2)

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display the score
    score_display = font.render(f'Player A: {score_a}  Player B: {score_b}', True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - score_display.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
