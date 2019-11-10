import pong_functions

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pong_functions.screen.fill(BLACK)


def show_menue():

    font = pong_functions.pygame.font.Font(None, 15)
    pong_functions.screen.fill(BLACK)
    text = font.render("Players:", 1, WHITE)
    pong_functions.screen.blit(text, (30, 350))

    return
