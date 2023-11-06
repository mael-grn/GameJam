import pygame
import pickle
import screens.error as error
import screens.niveau1 as n1
import screens.score as menu_score

def ouvrir_menu(screen) : 
    running = True
    dt=0
    clock = pygame.time.Clock()
    nom_joueur = ""
    jouer_color = (97, 195, 161)
    score_color = (97, 195, 161)
    quitter_color = (97, 195, 161)

    dict_score = {}
    #recuperation des scores sauvegardés
    try:
        with open("./data/score.pkl", "rb") as fichier:
            dict_score = pickle.load(fichier)
    except (EOFError, FileNotFoundError):
        # Gérer le cas où le fichier est vide ou n'existe pas
        dictionnaire_charge = {}

    def ajout_score(pseudo, score=0) :
        dict_score[pseudo] = score
        with open("./data/score.pkl", "wb") as fichier:
            pickle.dump(dict_score, fichier)

    while running :

        #arriere plan
        screen.fill("black")

        #chargement de la police
        chemin = "./assets/fonts/pinball.ttf"
        font = pygame.font.Font(chemin, 50) 
        font_big = pygame.font.Font(chemin, 60) 

        #chargement du logo
        logo = pygame.image.load("./assets/img/game_logo.jpg")
        #redimmensionner le logo
        logo_small = pygame.transform.scale(logo, (logo.get_width()/2, logo.get_height()/2))
        screen.blit(logo_small, (screen.get_width() // 2 - logo_small.get_width()/2, screen.get_height() // 4 - logo_small.get_height()/2))

        #creation du champs contenant le nom du joueur
        player = font_big.render("PSEUDO : "+nom_joueur, True, (97, 195, 161))
        player_rec = player.get_rect()
        player_rec.center = ((screen.get_width() // 2), (screen.get_height() // 3)*2)
        screen.blit(player, player_rec)

        #creation du bouton quitter
        quitter = font.render("QUITTER", True, quitter_color)
        quitter_rec = quitter.get_rect()
        quitter_rec.center = ((screen.get_width() // 4)*3, (screen.get_height() // 3)*2.5)
        screen.blit(quitter, quitter_rec)

        #creation du bouton score
        score = font.render("SCORE", True, score_color)
        score_rec = score.get_rect()
        score_rec.center = ((screen.get_width() // 4)*2, (screen.get_height() // 3)*2.5)
        screen.blit(score, score_rec)

        #creation du bouton jouer
        jouer = font.render("JOUER", True, jouer_color)  # (255, 0, 0) représente la couleur rouge (RVB)
        jouer_rec = jouer.get_rect()
        jouer_rec.center = ((screen.get_width() // 4), (screen.get_height() // 3)*2.5)
        screen.blit(jouer, jouer_rec)

        #gestion des evenements
        for event in pygame.event.get():

            #si les touches du clavier sont pressées
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nom_joueur = nom_joueur[:-1]
                else:
                    nom_joueur += event.unicode

            #en cas de cliques
            if event.type == pygame.MOUSEBUTTONDOWN:

                #si fermeture fenetre
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                # Si clique sur bouton quitter
                if quitter_rec.collidepoint(event.pos):
                    running=False
                    pygame.quit()
                #si clique sur bouton jouer
                if jouer_rec.collidepoint(event.pos):

                    if (nom_joueur in dict_score) | (nom_joueur == "") :
                        jouer_color = (255, 0, 0)
                    else:
                        ajout_score(nom_joueur)
                        running=False
                        n1.ouvrir_niveau(screen)
                #si clique sur bouton score
                if score_rec.collidepoint(event.pos):
                    running=False
                    menu_score.ouvrir_score(screen, dict_score)

            if event.type == pygame.MOUSEMOTION:
                if jouer_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    jouer_color = (255, 255, 255)
                else:
                    jouer_color = (97, 195, 161)

                if quitter_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    quitter_color = (255, 255, 255)
                else:
                    quitter_color = (97, 195, 161)

                if score_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    score_color = (255, 255, 255)
                else:
                    score_color = (97, 195, 161)

            

        # Comme les dessions sont fait dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par secondes et retourne le temps réel passé
        dt = clock.tick(60) 
    
                
