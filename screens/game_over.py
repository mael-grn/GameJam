import pygame
import screens.main_menu as main_menu

def ouvrir_game_over(screen):
    running = True
    dt = 0
    clock = pygame.time.Clock()

    # Chargement de la police pour l'écran de Game Over
    chemin = "./assets/fonts/pinball.ttf"
    font = pygame.font.Font(chemin, 30)  # Utilisez la même police que le menu principal
    font_big = pygame.font.Font(chemin, 50)

    menu_button_path = "./assets/buttons/normal.png"

    while running:
        # Code pour afficher l'écran de Game Over avec la police
        screen.fill((0, 0, 0))  # Arrière-plan

        #arriere plan
        game_over_bg = pygame.image.load("./assets/img/title_bg.png")
        #redimmensionner le logo
        game_over_bg_big = pygame.transform.scale(game_over_bg, (game_over_bg.get_width()*4, game_over_bg.get_height()*4))
        game_over_bg_rec = game_over_bg_big.get_rect()
        game_over_bg_rec.center = (screen.get_width() // 2, screen.get_height() // 2)
        screen.blit(game_over_bg_big, game_over_bg_rec)   
         #texte
        game_over = font_big.render("GAME OVER", True, (0, 0, 0))
        game_over_rec = game_over.get_rect()
        game_over_rec.center = (screen.get_width() // 2, screen.get_height() // 2)
        screen.blit(game_over, game_over_rec)

        #creation du bouton jouer
        #arriere plan
        menu_button = pygame.image.load(menu_button_path)
        menu_button_big = pygame.transform.scale(menu_button, (menu_button.get_width()*2, menu_button.get_height()*2))
        menu_button_rec = menu_button_big.get_rect()
        menu_button_rec.center = ((screen.get_width() // 2), (screen.get_height() // 3)*2)
        screen.blit(menu_button_big, menu_button_rec)
        #texte
        menu = font.render("MENU", True, (0,0,0))
        menu_rec = menu.get_rect()
        menu_rec.center = ((screen.get_width() // 2), (screen.get_height() // 3)*2)
        screen.blit(menu, menu_rec)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si clique sur bouton quitter
                if menu_button_rec.collidepoint(event.pos):
                    menu_button_path = "./assets/buttons/press.png"

            if event.type == pygame.MOUSEBUTTONUP:
                # Si clique sur bouton quitter
                if menu_button_rec.collidepoint(event.pos):
                    running=False
                    main_menu.ouvrir_menu(screen)

            if event.type == pygame.MOUSEMOTION:
                if menu_button_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    menu_button_path = "./assets/buttons/over.png"
                else:
                    menu_button_path = "./assets/buttons/normal.png"
                    


        pygame.display.flip()
        dt = clock.tick(60)

    # Une fois l'écran de Game Over fermé, retournez au menu principal
    menu.ouvrir_menu(screen)