import pygame
import screens.main_menu as menu

def ouvrir_game_over(screen):
    running = True
    dt = 0
    clock = pygame.time.Clock()

    # Chargement de la police pour l'écran de Game Over
    chemin = "./assets/fonts/pinball.ttf"
    font = pygame.font.Font(chemin, 50)  # Utilisez la même police que le menu principal
    font_big = pygame.font.Font(chemin, 60)

    # Bouton "Menu Principal"
    menu_button_color = (97, 195, 161)
    menu_button = font.render("Menu Principal", True, menu_button_color)
    menu_button_rect = menu_button.get_rect()
    menu_button_rect.center = (screen.get_width() // 2, screen.get_height() // 1.5)

    while running:
        # Code pour afficher l'écran de Game Over avec la police
        screen.fill((0, 0, 0))  # Arrière-plan

        # Crée une surface de texte rouge avec le mot "Game Over"
        game_over_text = font_big.render("Game Over", True, (255, 0, 0))  # Rouge (RVB)
        game_over_rect = game_over_text.get_rect()
        game_over_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        screen.blit(game_over_text, game_over_rect)

        # Afficher le bouton "Menu Principal"
        screen.blit(menu_button, menu_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            # Vérifiez si le bouton "Menu Principal" est cliqué
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button_rect.collidepoint(event.pos):
                    running = False  # Quittez l'écran de Game Over
                    menu.ouvrir_menu(screen)  # Retournez au menu principal

        pygame.display.flip()
        dt = clock.tick(60)

    # Une fois l'écran de Game Over fermé, retournez au menu principal
    menu.ouvrir_menu(screen)