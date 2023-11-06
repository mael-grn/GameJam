import pygame
import screens.error as error
import screens.main_menu as menu

def ouvrir_score(screen, dict_score):

    # Définit l'horloge pour connaitre le temps qui a passé
    clock = pygame.time.Clock()
    # Pour savoir quand la boucle du jeu se termine
    running = True
    # Le temps passé entre deux rafraichissement de l'écran en millisecondes
    dt = 0

    retour_color = (97, 195, 161)

    # Boucle de l'animation
    while running:
        

        # Remplit l'écran avec une couleur de fond (avant de dessiner le texte)
        screen.fill((0, 0, 0))

        chemin = "./assets/fonts/pinball.ttf"
        font = pygame.font.Font(chemin, 50) 
        font_big = pygame.font.Font(chemin, 60) 
        
        # Affichage du titre
        titre = font_big.render("SCORES", True, (97, 195, 161))
        titre_rec = titre.get_rect()
        titre_rec.center = (screen.get_width() // 2, 50)
        screen.blit(titre, titre_rec)
        
        # Affichage du bouton retour
        retour = font.render("RETOUR", True, retour_color)
        retour_rec = retour.get_rect()
        retour_rec.center = (150, 50)
        screen.blit(retour, retour_rec)

        from_top = 150

        for pseudo, val in dict_score.items():
            # Affichage du score
            unScore = font.render(f"{pseudo} : {val}", True, (97, 195, 161))
            unScore_rec = unScore.get_rect()
            unScore_rec.center = (screen.get_width() // 2, from_top)
            screen.blit(unScore, unScore_rec)

            from_top += 75

        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.QUIT:
                    running = False

                if retour_rec.collidepoint(event.pos):
                    running=False
                    menu.ouvrir_menu(screen)

            if event.type == pygame.MOUSEMOTION:
                if retour_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    retour_color = (255, 255, 255)
                else:
                    retour_color = (97, 195, 161)

        # Comme les dessins sont faits dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par seconde et retourne le temps réel passé
        clock.tick(60)
    # Termine proprement le module
    pygame.quit()

