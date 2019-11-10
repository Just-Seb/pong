import pong_functions

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pong_functions.screen.fill(BLACK)


def show_menue():

    pong_functions.screen.fill(BLACK)

    font = pong_functions.pygame.font.Font(None, 70)
    text = font.render("Main Menue", 1, WHITE)
    pong_functions.screen.blit(text, (200, 10))

    font = pong_functions.pygame.font.Font(None, 45)
    text = font.render("Players:", 1, WHITE)
    pong_functions.screen.blit(text, (50, 100))

    font = pong_functions.pygame.font.Font(None, 60)
    text = font.render("<", 1, WHITE)
    pong_functions.screen.blit(text, (200, 92))

    font = pong_functions.pygame.font.Font(None, 60)
    text = font.render(">", 1, WHITE)
    pong_functions.screen.blit(text, (400, 292))

    font = pong_functions.pygame.font.Font(None, 45)
    text = font.render("Lives:", 1, WHITE)
    pong_functions.screen.blit(text, (50, 300))

    font = pong_functions.pygame.font.Font(None, 60)
    text = font.render("<", 1, WHITE)
    pong_functions.screen.blit(text, (200, 292))

    font = pong_functions.pygame.font.Font(None, 60)
    text = font.render(">", 1, WHITE)
    pong_functions.screen.blit(text, (400, 292))

    return
