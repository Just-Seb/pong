import pygame
import main_menue
from paddle import Paddle
from ball import Ball


pygame.init()

size = (700, 700)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

number_of_players = 4

### Sprite Creation Start ###

paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 20
paddle1.rect.y = 200

paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 680
paddle2.rect.y = 200

paddle3 = Paddle(WHITE, 100, 10)
paddle3.rect.x = 200
paddle3.rect.y = 20

paddle4 = Paddle(WHITE, 100, 10)
paddle4.rect.x = 200
paddle4.rect.y = 680

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddle1)
all_sprites_list.add(paddle2)
all_sprites_list.add(paddle3)
all_sprites_list.add(paddle4)
all_sprites_list.add(ball)

### Sprite Creation End ###

### Global Variables Start ###

starting_points = 10

clock = pygame.time.Clock()

welcome = "Welcome To 4 Player Pong!"
welcome2 = "(Press Enter To Continue)"
welcome3 = "(Press Enter To Start Playing)"

loser_array = [False, False, False, False]
paddle_array = [paddle1, paddle2, paddle3, paddle4]
score_array = []

for j in range(len(paddle_array)):

    score_array.append(starting_points)

move_array_first_half = [pygame.K_w, pygame.K_i, pygame.K_3, pygame.K_RIGHT]
move_array_second_half = [pygame.K_s, pygame.K_k, pygame.K_1, pygame.K_LEFT]
number_array = [1, 2, 3, 4]

carryOn = True
carryOn_menue = True
carryOn0 = True
carryOn2 = True

winner = "No One Wins :("

### Global Variables End ###


def display_controls():

    font = pygame.font.Font(None, 15)

    text = font.render("Player 1", 1, WHITE)
    screen.blit(text, (30, 350))
    text = font.render("(w,s)", 1, WHITE)
    screen.blit(text, (30, 330))

    text = font.render("Player 2", 1, WHITE)
    screen.blit(text, (630, 350))
    text = font.render("(i,k)", 1, WHITE)
    screen.blit(text, (630, 330))

    text = font.render("Player 4", 1, WHITE)
    screen.blit(text, (350, 670))
    text = font.render("(Right, Left)", 1, WHITE)
    screen.blit(text, (350, 650))

    text = font.render("Player 3", 1, WHITE)
    screen.blit(text, (350, 30))
    text = font.render("(1,3)", 1, WHITE)
    screen.blit(text, (350, 10))

    font = pygame.font.Font(None, 30)
    text = font.render(welcome3, 1, WHITE)
    screen.blit(text, (230, 450))


def display_winner():

    font = pygame.font.Font(None, 90)
    text = font.render(str(winner), 1, WHITE)
    screen.blit(text, (35, 30))


def check_for_winner():

    global winner, carryOn

    if not loser_array[0] and loser_array[1] and loser_array[2] and loser_array[3]:

        winner = "Player 1 Wins!"
        carryOn = False

    if not loser_array[1] and loser_array[0] and loser_array[2] and loser_array[3]:

        winner = "Player 2 Wins!"
        carryOn = False

    if not loser_array[2] and loser_array[0] and loser_array[1] and loser_array[3]:

        winner = "Player 3 Wins!"
        carryOn = False

    if not loser_array[3] and loser_array[0] and loser_array[1] and loser_array[2]:

        winner = "Player 4 Wins!"
        carryOn = False

    return


def display_welcome():

    font = pygame.font.Font(None, 70)
    text = font.render(welcome, 1, WHITE)
    screen.blit(text, (30, 350))
    font = pygame.font.Font(None, 30)
    text = font.render(welcome2, 1, WHITE)
    screen.blit(text, (230, 450))

    return


def check_score():

    global score_array

    if ball.rect.x >= 690:

        if score_array[1] > 0:
            score_array[1] -= 1

        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.x <= 10:

        if score_array[0] > 0:
            score_array[0] -= 1

        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.y > 690:

        if score_array[3] > 0:
            score_array[3] -= 1

        ball.velocity[1] = -ball.velocity[1]

    if ball.rect.y < 10:

        if score_array[2] > 0:
            score_array[2] -= 1

        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2) or pygame.sprite.collide_mask(ball, paddle3) or pygame.sprite.collide_mask(ball, paddle4):
        ball.bounce()

    return


def display_scores():

    font = pygame.font.Font(None, 30)
    text = font.render(str(score_array[0]), 1, WHITE)
    screen.blit(text, (300, 350))
    text = font.render(str(score_array[1]), 1, WHITE)
    screen.blit(text, (400, 350))
    text = font.render(str(score_array[2]), 1, WHITE)
    screen.blit(text, (350, 300))
    text = font.render(str(score_array[3]), 1, WHITE)
    screen.blit(text, (350, 400))

    return


def move_paddles():

    global move_array_first_half, move_array_second_half, paddle_array

    counter = 0

    for paddle in paddle_array:

        if counter <= 1:

            keys = pygame.key.get_pressed()

            first_key = move_array_first_half[counter]
            second_key = move_array_second_half[counter]

            if keys[first_key]:
                paddle.moveUp(10)
            if keys[second_key]:
                paddle.moveDown(10)

        else:

            keys = pygame.key.get_pressed()

            first_key = move_array_first_half[counter]
            second_key = move_array_second_half[counter]

            if keys[first_key]:
                paddle.moveRight(10)
            if keys[second_key]:
                paddle.moveLeft(10)

        counter += 1

    return


def check_loser():

    global loser_array, score_array, move_array_second_half, move_array_first_half

    for i in range(len(score_array)):

        if score_array[i] == 0:

            move_array_first_half[i] = 0
            move_array_second_half[i] = 0
            loser_array[i] = True

    return


def game():

    global carryOn, carryOn_menue, carryOn2

    while carryOn_menue:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                carryOn_menue = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_KP_ENTER:

                    carryOn_menue = False

        main_menue.show_menue()

        pygame.display.flip()

        clock.tick(60)

    while carryOn:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                carryOn = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_x:

                    carryOn = False

        move_paddles()

        all_sprites_list.update()

        check_score()

        screen.fill(BLACK)

        all_sprites_list.draw(screen)

        display_scores()

        check_loser()

        check_for_winner()

        pygame.display.flip()

        clock.tick(60)

    while carryOn2:

        display_winner()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_x:

                    carryOn2 = False

                elif event.key == pygame.K_r:

                    spacer()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


def spacer():

    global carryOn, carryOn_menue, carryOn0, carryOn2

    carryOn = True
    carryOn_menue = True
    carryOn0 = True
    carryOn2 = True

    game()

    return


while carryOn0:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_KP_ENTER:

                carryOn0 = False

    display_welcome()

    pygame.display.flip()

    clock.tick(60)


game()
