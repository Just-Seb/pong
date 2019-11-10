import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = (700, 700)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

carryOn = True

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    font = pygame.font.Font(None, 60)

    text = font.render(str(pygame.K_w), 1, WHITE)
    screen.blit(text, (30, 350))

    screen.fill(BLACK)
    pygame.display.flip()
    clock.tick(60)