import pygame
import screens.error as error
import screens.main_menu as menu
import game_logic
import io
def ouvrir_score(screen, dictionnaire_score):

    # Définit l'horloge pour connaitre le temps qui a passé
    clock = pygame.time.Clock()
    # Pour savoir quand la boucle du jeu se termine
    running = True
    # Le temps passé entre deux rafraichissement de l'écran en millisecondes
    dt = 0

    retour_color = (97, 195, 161)
    dict_score = {}
    dict_score = dictionnaire_score

    retour_button_path = "./assets/buttons/simple_normal.png"

    reset_button_path = "./assets/buttons/normal.png"

    # Boucle de l'animation
    while running:
        
        
        # Remplit l'écran avec une couleur de fond (avant de dessiner le texte)
        screen.fill((0, 0, 0))

        background_image = pygame.image.load("./assets/img/EVeil A.png")
        background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
        screen.blit(background_image, (0, 0))

        chemin = "./assets/fonts/pinball.ttf"
        font = pygame.font.Font(chemin, 27) 
        font_big = pygame.font.Font(chemin, 50)
        font_small = pygame.font.Font(chemin, 20)
        
        # Affichage du titre
        #arriere plan
        titre_bg = pygame.image.load("./assets/img/title_bg.png")
        #redimmensionner le logo
        titre_bg_big = pygame.transform.scale(titre_bg, (titre_bg.get_width()*4, titre_bg.get_height()*4))
        titre_bg_rec = titre_bg_big.get_rect()
        titre_bg_rec.center = ((screen.get_width() // 2), 50)
        screen.blit(titre_bg_big, titre_bg_rec)
        #texte
        titre = font_big.render("MEILLEURS SCORES", True, (0,0,0))
        titre_rec = titre.get_rect()
        titre_rec.center = (screen.get_width() // 2, 50)
        screen.blit(titre, titre_rec)
        
        # Affichage du bouton retour
        #arriere plan
        retour_button = pygame.image.load(retour_button_path)
        retour_button_big = pygame.transform.scale(retour_button, (retour_button.get_width(), retour_button.get_height()))
        retour_button_rec = retour_button_big.get_rect()
        retour_button_rec.center = (20, 20)
        screen.blit(retour_button_big, retour_button_rec)
        #texte
        retour = font_small.render("<-", True, (0,0,0))
        retour_rec = retour.get_rect()
        retour_rec.center = (20, 20)
        screen.blit(retour, retour_rec)

        # Affichage du bouton retour
        #arriere plan
        reset_button = pygame.image.load(reset_button_path)
        reset_button_big = pygame.transform.scale(reset_button, (reset_button.get_width()*1.5, reset_button.get_height()*1.5))
        reset_button_rec = reset_button_big.get_rect()
        reset_button_rec.center = (screen.get_width()- 60,screen.get_height()- 50)
        screen.blit(reset_button_big, reset_button_rec)
        #texte
        reset = font_small.render("RESET", True, (0,0,0))
        reset_rec = retour.get_rect()
        reset_rec.center = (screen.get_width()-75, screen.get_height()-50)
        screen.blit(reset, reset_rec)

        from_top = 175 #marge des score 

        #arriere plan des scores
        score_bg = pygame.image.load("./assets/img/list.png")
        #redimmensionner le logo
        score_bg_big = pygame.transform.scale(score_bg, (score_bg.get_width()*4, score_bg.get_height()*4))
        score_bg_rec = score_bg_big.get_rect()
        score_bg_rec.center = ((screen.get_width() // 2), (screen.get_width() // 2)-100)
        screen.blit(score_bg_big, score_bg_rec)

        # Variable de compteur pour le nombre d'itérations
        compteur_iterations = 0



        for pseudo, val in dict_score.items():
            if compteur_iterations >= 14:
                break  # Sortir de la boucle si nous avons atteint 14 itérations
            
            # Affichage du score
            unScore = font.render(f"{pseudo} : {val}", True, (0, 0, 0))
            unScore_rec = unScore.get_rect()
            unScore_rec.center = (screen.get_width() // 2, from_top)
            screen.blit(unScore, unScore_rec)

            from_top += score_bg_rec.height // 14 -1

            # Incrémenter le compteur d'itérations
            compteur_iterations += 1

        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtre
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour_button_rec.collidepoint(event.pos):
                    retour_button_path = "./assets/buttons/simple_press.png"
                if reset_button_rec.collidepoint(event.pos):
                    reset_button_path = "./assets/buttons/press.png"
            
            if event.type == pygame.MOUSEBUTTONUP:
                if retour_button_rec.collidepoint(event.pos):
                    running=False
                    menu.ouvrir_menu(screen)
                if reset_button_rec.collidepoint(event.pos):
                    with io.open("./data/score.pkl", "w") as f:
                        f.write("")


                    menu.ouvrir_menu(screen)

            if event.type == pygame.MOUSEMOTION:
                if retour_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    retour_button_path = "./assets/buttons/simple_over.png"
                else:
                    retour_button_path = "./assets/buttons/simple_normal.png"
                if reset_button_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    reset_button_path = "./assets/buttons/over.png"
                else:
                    reset_button_path = "./assets/buttons/normal.png"

        # Comme les dessins sont faits dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par seconde et retourne le temps réel passé
        clock.tick(60)
    # Termine proprement le module
    pygame.quit()

