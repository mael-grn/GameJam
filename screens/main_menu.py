import pygame
import pickle
import screens.error as error
import screens.niveau1 as n1
import screens.score as menu_score
import game_logic

def ouvrir_menu(screen) : 
    running = True
    dt=0
    clock = pygame.time.Clock()
    nom_joueur = ""
    #jouer_color = (97, 195, 161)
    #score_color = (97, 195, 161)
    #quitter_color = (97, 195, 161)

    jouer_button_path = "./assets/buttons/normal.png"
    score_button_path = "./assets/buttons/normal.png"
    quitter_button_path = "./assets/buttons/normal.png"

    #chargement de la police
    chemin = "./assets/fonts/pinball.ttf"
    font = pygame.font.Font(chemin, 30) 
    font_big = pygame.font.Font(chemin, 50) 

    while running :

        #arriere plan
        screen.fill("black")

        #chargement du logo
        logo = pygame.image.load("./assets/img/game_logo.jpg")
        #redimmensionner le logo
        logo_small = pygame.transform.scale(logo, (logo.get_width()/2, logo.get_height()/2))
        screen.blit(logo_small, (screen.get_width() // 2 - logo_small.get_width()/2, screen.get_height() // 4 - logo_small.get_height()/2))

        #creation du champs contenant le nom du joueur
        #arriere plan
        player_bg = pygame.image.load("./assets/img/title_bg.png")
        #redimmensionner le logo
        player_bg_big = pygame.transform.scale(player_bg, (player_bg.get_width()*4, player_bg.get_height()*4))
        player_bg_rec = player_bg_big.get_rect()
        player_bg_rec.center = ((screen.get_width() // 2), (screen.get_height() // 3)*2)
        screen.blit(player_bg_big, player_bg_rec)        #texte
        player = font_big.render("PSEUDO : "+nom_joueur, True, (0, 0, 0))
        player_rec = player.get_rect()
        player_rec.center = ((screen.get_width() // 2), (screen.get_height() // 3)*2)
        screen.blit(player, player_rec)

        #creation du bouton jouer
        #arriere plan
        jouer_button = pygame.image.load(jouer_button_path)
        jouer_button_big = pygame.transform.scale(jouer_button, (jouer_button.get_width()*2, jouer_button.get_height()*2))
        jouer_button_rec = jouer_button_big.get_rect()
        jouer_button_rec.center = ((screen.get_width() // 4), (screen.get_height() // 3)*2.5)
        screen.blit(jouer_button_big, jouer_button_rec)
        #texte
        jouer = font.render("PLAY", True, (0,0,0))
        jouer_rec = jouer.get_rect()
        jouer_rec.center = ((screen.get_width() // 4), (screen.get_height() // 3)*2.5)
        screen.blit(jouer, jouer_rec)
        

        #creation du bouton score
        #arriere plan
        score_button = pygame.image.load(score_button_path)
        score_button_big = pygame.transform.scale(score_button, (score_button.get_width()*2, score_button.get_height()*2))
        score_button_rec = score_button_big.get_rect()
        score_button_rec.center = ((screen.get_width() // 4)*2, (screen.get_height() // 3)*2.5)
        screen.blit(score_button_big, score_button_rec)
        #texte
        score = font.render("SCORE", True, (0,0,0))
        score_rec = score.get_rect()
        score_rec.center = ((screen.get_width() // 4)*2, (screen.get_height() // 3)*2.5)
        screen.blit(score, score_rec)


        #creation du bouton quitter
        #arriere plan
        quitter_button = pygame.image.load(quitter_button_path)
        quitter_button_big = pygame.transform.scale(quitter_button, (quitter_button.get_width()*2, quitter_button.get_height()*2))
        quitter_button_rec = quitter_button_big.get_rect()
        quitter_button_rec.center = ((screen.get_width() // 4)*3, (screen.get_height() // 3)*2.5)
        screen.blit(quitter_button_big, quitter_button_rec)
        #texte
        quitter = font.render("QUIT", True, (0,0,0))
        quitter_rec = quitter.get_rect()
        quitter_rec.center = ((screen.get_width() // 4)*3, (screen.get_height() // 3)*2.5)
        screen.blit(quitter, quitter_rec)

        #gestion des evenements
        for event in pygame.event.get():

            #si fermeture fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            #si les touches du clavier sont pressées
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nom_joueur = nom_joueur[:-1]
                else:
                    if len(nom_joueur) < 12:
                        nom_joueur += event.unicode

            #en cas de cliques
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si clique sur bouton quitter
                if quitter_button_rec.collidepoint(event.pos):
                    quitter_button_path = "./assets/buttons/press.png"
                #si clique sur bouton jouer
                if jouer_button_rec.collidepoint(event.pos):
                    jouer_button_path = "./assets/buttons/press.png"
                #si clique sur bouton score
                if score_button_rec.collidepoint(event.pos):
                    score_button_path = "./assets/buttons/press.png"


            if event.type == pygame.MOUSEBUTTONUP:
                # Si clique sur bouton quitter
                if quitter_button_rec.collidepoint(event.pos):
                    game_logic.play_sound("clic")
                    running=False
                    pygame.quit()
                #si clique sur bouton jouer
                if jouer_button_rec.collidepoint(event.pos):
                    if (nom_joueur != "") :
                        game_logic.play_sound("clic")
                        game_logic.ajout_score(nom_joueur)
                        running=False
                        n1.ouvrir_niveau(screen)
                #si clique sur bouton score
                if score_button_rec.collidepoint(event.pos):
                    game_logic.play_sound("clic")
                    running=False
                    menu_score.ouvrir_score(screen, game_logic.get_score())


            if event.type == pygame.MOUSEMOTION:
                if jouer_button_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    jouer_button_path = "./assets/buttons/over.png"
                else:
                    jouer_button_path = "./assets/buttons/normal.png"

                if quitter_button_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    quitter_button_path = "./assets/buttons/over.png"
                else:
                    quitter_button_path = "./assets/buttons/normal.png"

                if score_button_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    score_button_path = "./assets/buttons/over.png"
                else:
                    score_button_path = "./assets/buttons/normal.png"

            

        # Comme les dessions sont fait dans un buffer, permute le buffer
        
        pygame.display.flip()
        # Limite le frame rate à 60 images par secondes et retourne le temps réel passé
        dt = clock.tick(60) 
    
                
