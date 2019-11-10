import pong_functions, main_menue

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pong_functions.pygame.display.set_caption("Pong")

while pong_functions.carryOn0:

    for event in pong_functions.pygame.event.get():

        if event.type == pong_functions.pygame.KEYDOWN:

            if event.key == pong_functions.pygame.K_KP_ENTER:

                pong_functions.carryOn0 = False

    pong_functions.display_welcome()

    pong_functions.pygame.display.flip()

    pong_functions.clock.tick(60)


while pong_functions.carryOn_menue:

    for event in pong_functions.pygame.event.get():

        if event.type == pong_functions.pygame.QUIT:

            pong_functions.carryOn_menue = False

        elif event.type == pong_functions.pygame.KEYDOWN:

            if event.key == pong_functions.pygame.K_KP_ENTER:

                pong_functions.carryOn_menue = False

    main_menue.show_menue()

    pong_functions.pygame.display.flip()

    pong_functions.clock.tick(60)


while pong_functions.carryOn1:

    for event in pong_functions.pygame.event.get():

        if event.type == pong_functions.pygame.KEYDOWN:

            if event.key == pong_functions.pygame.K_KP_ENTER:

                pong_functions.carryOn1 = False

    pong_functions.screen.fill(BLACK)

    pong_functions.all_sprites_list.draw(pong_functions.screen)

    pong_functions.display_controls()

    pong_functions.pygame.display.flip()

    pong_functions.clock.tick(60)


while pong_functions.carryOn:

    for event in pong_functions.pygame.event.get():
        if event.type == pong_functions.pygame.QUIT:
            pong_functions.carryOn = False
        elif event.type == pong_functions.pygame.KEYDOWN:
            if event.key == pong_functions.pygame.K_x:
                pong_functions.carryOn = False

    pong_functions.move_paddles()

    pong_functions.all_sprites_list.update()

    pong_functions.check_score()

    pong_functions.screen.fill(BLACK)

    pong_functions.all_sprites_list.draw(pong_functions.screen)

    pong_functions.display_scores()

    pong_functions.check_loser()

    pong_functions.check_for_winner()

    pong_functions.pygame.display.flip()

    pong_functions.clock.tick(60)


while pong_functions.carryOn2:

    pong_functions.display_winner()

    for event in pong_functions.pygame.event.get():

        if event.type == pong_functions.pygame.KEYDOWN:

            if event.key == pong_functions.pygame.K_x:

                pong_functions.carryOn2 = False

    pong_functions.pygame.display.flip()

    pong_functions.clock.tick(60)

pong_functions.pygame.quit()
