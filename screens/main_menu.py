import pygame
import pickle
import screens.error as error
import screens.niveau1 as n1
import screens.score as menu_score
import game_logic
import screens.credit as menu_credit
import constants

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
    credit_button_path = "./assets/buttons/normal.png"
    quitter_button_path = "./assets/buttons/normal.png"

    #chargement de la police

    font = pygame.font.Font(constants.PINBALL_PATH, 30) 
    font_big = pygame.font.Font(constants.PINBALL_PATH, 50) 
    font_small = pygame.font.Font(constants.ROBOTO_PATH, 15) 

    text_info = "Veuillez rentrer un pseudo pour jouer"

    while running :

        #arriere plan
        background_image = pygame.image.load("./assets/img/EVeil A.png")
        background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
        screen.blit(background_image, (0, 0))

        #chargement du logo
        #logo = pygame.image.load("./assets/img/game_logo.jpg")
        #redimmensionner le logo
        #logo_small = pygame.transform.scale(logo, (logo.get_width()/2, logo.get_height()/2))
        #screen.blit(logo_small, (screen.get_width() // 2 - logo_small.get_width()/2, screen.get_height() // 4 - logo_small.get_height()/2))

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
        jouer_button_big = pygame.transform.scale(jouer_button, (jouer_button.get_width()*4, jouer_button.get_height()*4))
        jouer_button_rec = jouer_button_big.get_rect()
        jouer_button_rec.center = ((screen.get_width() // 2), (screen.get_height() // 3)*1.4)
        screen.blit(jouer_button_big, jouer_button_rec)
        #texte
        jouer = font_big.render("PLAY", True, (0,0,0))
        jouer_rec = jouer.get_rect()
        jouer_rec.center = ((screen.get_width() // 2), (screen.get_height() // 3)*1.4)
        screen.blit(jouer, jouer_rec)

        if nom_joueur == "":
            text_info = "Veuillez rentrer un pseudo pour jouer"
        elif nom_joueur in game_logic.get_score():
            text_info = "Ce pseudo à dejà été utilisé"
        else:
            text_info = "ce pseudo est valide"
        
        info = font_small.render(text_info, True, (0,0,0))
        info_rec = info.get_rect()
        info_rec.center = ((screen.get_width() // 2), (screen.get_height() // 3)*1.8)
        screen.blit(info, info_rec)
        

        #creation du bouton score
        #arriere plan
        score_button = pygame.image.load(score_button_path)
        score_button_big = pygame.transform.scale(score_button, (score_button.get_width()*2, score_button.get_height()*2))
        score_button_rec = score_button_big.get_rect()
        score_button_rec.center = ((screen.get_width() // 4), (screen.get_height() // 3)*2.5)
        screen.blit(score_button_big, score_button_rec)
        #texte
        score = font.render("SCORE", True, (0,0,0))
        score_rec = score.get_rect()
        score_rec.center = ((screen.get_width() // 4), (screen.get_height() // 3)*2.5)
        screen.blit(score, score_rec)

        #creation du bouton credit
        #arriere plan
        credit_button = pygame.image.load(credit_button_path)
        credit_button_big = pygame.transform.scale(credit_button, (credit_button.get_width()*2, credit_button.get_height()*2))
        credit_button_rec = credit_button_big.get_rect()
        credit_button_rec.center = ((screen.get_width() // 4)*2, (screen.get_height() // 3)*2.5)
        screen.blit(credit_button_big, credit_button_rec)
        #texte
        credit = font.render("CREDIT", True, (0,0,0))
        credit_rec = credit.get_rect()
        credit_rec.center = ((screen.get_width() // 4)*2, (screen.get_height() // 3)*2.5)
        screen.blit(credit, credit_rec)


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
                    #si clique sur bouton jouer
                if credit_button_rec.collidepoint(event.pos):
                    credit_button_path = "./assets/buttons/press.png"
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
                    if (nom_joueur != "") and not nom_joueur in game_logic.get_score() :
                        game_logic.play_sound("clic")
                        game_logic.set_score(nom_joueur)
                        running=False
                        n1.ouvrir_niveau(screen, nom_joueur)
                #si clique sur bouton score
                if score_button_rec.collidepoint(event.pos):
                    game_logic.play_sound("clic")
                    running=False
                    menu_score.ouvrir_score(screen, game_logic.get_score())
                    #si clique sur bouton score
                if credit_button_rec.collidepoint(event.pos):
                    game_logic.play_sound("clic")
                    running=False
                    menu_credit.ouvrir_credit(screen)


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
                if credit_button_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    credit_button_path = "./assets/buttons/over.png"
                else:
                    credit_button_path = "./assets/buttons/normal.png"

            

        # Comme les dessions sont fait dans un buffer, permute le buffer
        
        pygame.display.flip()
        # Limite le frame rate à 60 images par secondes et retourne le temps réel passé
        dt = clock.tick(60) 
    
                
