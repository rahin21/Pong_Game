import pygame

pygame.init()

# Display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()
icon = pygame.image.load("Capture.PNG")
pygame.display.set_icon(icon)

# color
white = (255, 255, 255)
some = (155, 155, 155)
black = (30, 30, 30)
ash = (50, 50, 50)
blue = (0, 0, 255)
red = (200, 50, 50)

# Ball
x_chng = 0
y_chng = 0
ball = pygame.Rect(390, 300, 20, 20)

# Player
player1 = pygame.Rect(10, 260, 10, 120)
player2 = pygame.Rect(780, 260, 10, 120)
speed_player1 = 0
speed_player2 = 0

# Game Variables
score_1 = 0
score_font = pygame.font.Font("LemonMilk.otf", 20)
score_2 = 0

# Time
current_time = 0
going_time = 0
stating_time_font = pygame.font.Font("LemonMilk.otf", 40)


def show_score(x, y, score):
    screen.blit(score_font.render(f"{int(score)}", True, black), (x, y))


game_active = False

running = True

while running:
    screen.fill((ash))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x_chng = 5
                y_chng = 5
                game_active = True
                going_time = pygame.time.get_ticks()
            if event.key == pygame.K_UP:
                speed_player2 = -5
            if event.key == pygame.K_DOWN:
                speed_player2 = 5
            if event.key == pygame.K_w:
                speed_player1 = -5
            if event.key == pygame.K_s:
                speed_player1 = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speed_player2 = 0
            if event.key == pygame.K_DOWN:
                speed_player2 = 0
            if event.key == pygame.K_w:
                speed_player1 = 0
            if event.key == pygame.K_s:
                speed_player1 = 0

    pygame.draw.line(screen, black, (400, 0), (400, 250), 3)
    pygame.draw.line(screen, black, (400, 370), (400, 600), 3)
    if game_active:
        if ball.top <= 0 or ball.bottom >= 600:
            y_chng *= -1
        if ball.colliderect(player1) or ball.colliderect(player2):
            x_chng *= -1

        if ball.right >= 786:
            score_1 += 1
            going_time = pygame.time.get_ticks()
            ball = pygame.Rect(390, 300, 20, 20)

        if ball.right <= 26:
            score_2 += 1
            going_time = pygame.time.get_ticks()
            ball = pygame.Rect(390, 300, 20, 20)

        if current_time - going_time < 1000:
            screen.blit(stating_time_font.render("1", True, black), (395, 320))

        if 1001 < current_time - going_time < 2000:
            screen.blit(stating_time_font.render("2", True, black), (390, 320))

        if 2001 < current_time - going_time < 3000:
            screen.blit(stating_time_font.render("3", True, black), (390, 320))

        if current_time - going_time > 3000:
            # ball movement
            ball.x += x_chng
            ball.y += y_chng
    
        # Player movement
        player1.y += speed_player1
        player2.y += speed_player2
        if player1.top <= 0 or player1.bottom >= 600:
            speed_player1 = 0
        if player2.top <= 0 or player2.bottom >= 600:
            speed_player2 = 0
        current_time = pygame.time.get_ticks()

        # Score
        show_score(365, 20, score_1)
        show_score(420, 20, score_2)

    pygame.draw.rect(screen, red, ball, 0, 10)
    pygame.draw.rect(screen, red, player1, 0, 20)
    pygame.draw.rect(screen, red, player2, 0, 20)
    
    # Frame rates
    clock.tick(60)
    pygame.display.update()
