import pygame

def show_error(screen, error_name = "unknown error") : 

    running = True
    dt=0
    clock = pygame.time.Clock()

    while True:
        screen.fill("black")
        chemin = "./assets/fonts/pinball.ttf"
        font = pygame.font.Font(chemin, 36)  # Vous pouvez ajuster la taille de la police
        font.set_italic(not font.italic)

        



        # Crée une surface de texte rouge avec le mot "error"
        text_surface = font.render(error_name, True, (255, 0, 0))  # (255, 0, 0) représente la couleur rouge (RVB)

        # Obtient les dimensions de la surface de texte
        text_rect = text_surface.get_rect()

        # Centre la surface de texte sur l'écran
        text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

        # Dessine la surface de texte sur l'écran
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # Comme les dessions sont fait dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par secondes et retourne le temps réel passé
        dt = clock.tick(60) 
