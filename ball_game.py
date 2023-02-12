import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 700
screen_height = 500

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Pong")

# Load font
font = pygame.font.Font(None, 36)

# Initialize clock
clock = pygame.time.Clock()

# Set paddle dimensions
paddle_width = 15
paddle_height = 100

# Set paddle speeds
paddle_speed = 5

# Initialize paddle positions
left_paddle_y = (screen_height / 2) - (paddle_height / 2)
right_paddle_y = (screen_height / 2) - (paddle_height / 2)

# Set ball dimensions
ball_size = 15

# Set ball speeds
ball_speed_x = 5
ball_speed_y = 5

# Initialize ball position
ball_x = (screen_width / 2) - (ball_size / 2)
ball_y = (screen_height / 2) - (ball_size / 2)

# Set score
left_score = 0
right_score = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move right paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        right_paddle_y += paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce ball off top and bottom walls
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y = -ball_speed_y

    # Check for ball hitting left paddle
    if ball_x <= paddle_width and ball_y >= left_paddle_y and ball_y <= left_paddle_y + paddle_height:
        ball_speed_x = -ball_speed_x

    # Check for ball hitting right paddle
    if ball_x >= screen_width - paddle_width - ball_size and ball_y >= right_paddle_y and ball_y <= right_paddle_y + paddle_height:
        ball_speed_x = -ball_speed_x

    # Check for ball missing left paddle
    if ball_x <= 0:
        right_score += 1
        ball_x = (screen_width / 2) - (ball_size / 2)
        ball_y = (screen_height / 2) - (ball_size / 2)

    # Check for ball missing right paddle
    if ball_x >= screen_width - ball_size:
        left_score += 1
        ball_x = (screen_width / 2) - (ball_size / 2)
        ball_y = (screen_height / 2) - (ball_size / 2)

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw left paddle
    left_paddle = pygame.Rect(0, left_paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, (255, 255, 255), left_paddle)

    # Draw right paddle
    right_paddle = pygame.Rect(screen_width - paddle_width, right_paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, (255, 255, 255), right_paddle)

    # Draw ball
    ball = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
    pygame.draw.rect(screen, (255, 255, 255), ball)

    # Draw score
    left_score_text = font.render("{}".format(left_score), True, (255, 255, 255))
    right_score_text = font.render("{}".format(right_score), True, (255, 255, 255))
    screen.blit(left_score_text, (screen_width / 4, 20))
    screen.blit(right_score_text, (screen_width / 4 * 3, 20))

    # Update screen
    pygame.display.update()

    # Tick clock
    clock.tick(60)

# Quit Pygame
pygame.quit()