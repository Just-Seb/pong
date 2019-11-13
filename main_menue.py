import pong_functions

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

carryOn_pause = True

area_players_plus = pong_functions.pygame.Rect(400, 92, 30, 30)

area_players_minus = pong_functions.pygame.Rect(200, 92, 30, 30)

area_points_plus = pong_functions.pygame.Rect(400, 292, 30, 30)

area_points_minus = pong_functions.pygame.Rect(200, 292, 30, 30)


def show_menue():

    global carryOn_pause

    pong_functions.screen.fill(BLACK)

    font = pong_functions.pygame.font.Font(None, 70)
    text = font.render("Main Menue", 1, WHITE)
    pong_functions.screen.blit(text, (200, 10))

    font = pong_functions.pygame.font.Font(None, 45)
    text = font.render("Players:", 1, WHITE)
    pong_functions.screen.blit(text, (50, 100))

    text = font.render(str(pong_functions.number_of_players), 1, WHITE)
    pong_functions.screen.blit(text, (250, 100))

    font = pong_functions.pygame.font.Font(None, 60)
    text = font.render("<", 1, WHITE)
    pong_functions.screen.blit(text, (200, 92))

    text = font.render(">", 1, WHITE)
    pong_functions.screen.blit(text, (400, 92))

    font = pong_functions.pygame.font.Font(None, 45)
    text = font.render("Lives:", 1, WHITE)
    pong_functions.screen.blit(text, (50, 300))

    text = font.render(str(pong_functions.starting_points), 1, WHITE)
    pong_functions.screen.blit(text, (250, 300))

    font = pong_functions.pygame.font.Font(None, 60)
    text = font.render("<", 1, WHITE)
    pong_functions.screen.blit(text, (200, 292))

    text = font.render(">", 1, WHITE)
    pong_functions.screen.blit(text, (400, 292))

    font = pong_functions.pygame.font.Font(None, 65)
    text = font.render("Enter", 1, WHITE)
    pong_functions.screen.blit(text, (250, 500))

    font = pong_functions.pygame.font.Font(None, 30)
    text = font.render("(press v to see layout)", 1, WHITE)
    pong_functions.screen.blit(text, (400, 600))

    for event in pong_functions.pygame.event.get():

        if event.type == pong_functions.pygame.KEYDOWN and event.key == pong_functions.pygame.K_v:

            while carryOn_pause:

                for event in pong_functions.pygame.event.get():

                    if event.type == pong_functions.pygame.KEYDOWN:

                        if event.key == pong_functions.pygame.K_ESCAPE:

                            carryOn_pause = False

                pong_functions.screen.fill(BLACK)

                pong_functions.all_sprites_list.draw(pong_functions.screen)

                pong_functions.display_controls()

                pong_functions.pygame.display.flip()

                pong_functions.clock.tick(60)

        if event.type == pong_functions.pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if area_players_plus.collidepoint(event.pos):

                    pong_functions.number_of_players += 1

                    if pong_functions.starting_points == 4:

                        pong_functions.starting_points = 4

                if area_players_minus.collidepoint(event.pos):

                    pong_functions.number_of_players -= 1

                    if pong_functions.number_of_players == 0:

                        pong_functions.number_of_players = 0

                if area_points_plus.collidepoint(event.pos):

                    pong_functions.starting_points += 1

                if area_points_minus.collidepoint(event.pos):

                    pong_functions.starting_points -= 1

                    if pong_functions.starting_points == 0:

                        pong_functions.starting_points = 0

    carryOn_pause = True

    return
