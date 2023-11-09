import pygame
import screens.error as error
import screens.main_menu as menu
import game_logic
import io
import constants
def ouvrir_credit(screen):

    # Définit l'horloge pour connaitre le temps qui a passé
    clock = pygame.time.Clock()
    # Pour savoir quand la boucle du jeu se termine
    running = True
    # Le temps passé entre deux rafraichissement de l'écran en millisecondes
    dt = 0

    retour_color = (97, 195, 161)

    page=1
    retour_button_path = "./assets/buttons/simple_normal.png"


    # Boucle de l'animation
    while running:
        
        
        # Remplit l'écran avec une couleur de fond (avant de dessiner le texte)
        screen.fill((0, 0, 0))

        background_image = pygame.image.load("./assets/img/EVeil A.png")
        background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
        screen.blit(background_image, (0, 0))
        
        font = pygame.font.Font(constants.ROBOTO_PATH, 14) 
        font_big = pygame.font.Font(constants.PINBALL_PATH, 50)
        font_small = pygame.font.Font(constants.PINBALL_PATH, 20)
        
        # Affichage du titre
        #arriere plan
        titre_bg = pygame.image.load("./assets/img/title_bg.png")
        #redimmensionner le logo
        titre_bg_big = pygame.transform.scale(titre_bg, (titre_bg.get_width()*4, titre_bg.get_height()*4))
        titre_bg_rec = titre_bg_big.get_rect()
        titre_bg_rec.center = ((screen.get_width() // 2), 50)
        screen.blit(titre_bg_big, titre_bg_rec)
        #texte
        titre = font_big.render("Credits", True, (0,0,0))
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


        from_top = 185 #marge des score 

        lignesP1 = [
            "Tileset:",
            "    Intérieur Pixel:",
            "        lien site: https://opengameart.org/content/lpc-submissions-merged",
            "        Graphiste : Sharm (https://opengameart.org/users/sharm)",
            "        Contributeur: William Thompson (https://opengameart.org/users/williamthompsonj)",
            "        Créateur: Daniel Eddeland",
            "        Participations:",
            "            Lanea Zimmerman (AKA Sharm)",
            "            Stephen Challener (AKA Redshrike)",
            "            Charles Sanchez (AKA CharlesGabriel)",
            "            Manuel Riecke (AKA MrBeast)",
            "            Daniel Armstrong (AKA HughSpectrum)",
            "        lien vers la licence:",
            "            CC-BY-SA 3.0 : http://creativecommons.org/licenses/by-sa/3.0/",
            "            GNU GPL 3.0 : http://www.gnu.org/licenses/gpl-3.0.html",
            "        Aucune modification n'a été effectuée."
        ]

        lignesP2 = [
            "    Intérieur Cyberpunk Pixel:",
            "        lien site:https://livingtheindie.itch.io/pixel-cyberpunk-interior",
            "        Créé par dylestorm (www.livingtheindie.com) - @livingtheindie",
            "        Licence d'actif",
            "        Aucune modifications n'a été effectuée.",
            "    Foodtruck Tiles:",
            "        lien site:https://www.deviantart.com/pkmnalexandrite/art/Food-Trucks-Tiles-742809303",
            "        Créateur:https://www.deviantart.com/pkmnalexandrite",
            "        Aucune modifications n'a été effectuée.",
            "Jaquette:",
            "    Photo IUT2:",
            "        lien site:https://commons.wikimedia.org/wiki/IUT_2_-_Grenoble.JPG",
            "        Nom auteur:Milky",
            "        Date:5 décembre 2007",
            "        Lieu:I.U.T. 2 sur la place Doyen Gosse à Grenoble",
            "        licence:",
            "            Licence art libre (Copyleft) : http://artlibre.org/licence/lal/en/"
        ]
        lignesP3 = [
            "Musiques:",
            "    Acceuil:",
            "        Lien:https://pixabay.com/fr/music/beats-good-night-160166/",
            "        Crédit:https://pixabay.com/fr/users/fassounds-3433550/",
            "        Lien licence:https://pixabay.com/service/terms/https://pixabay.com/license-summary/",
            "    Jeu:",
            "        Lien:https://pixabay.com/music/dance-utopia-cosmic-trance-mix-7523/",
            "        Crédit:https://pixabay.com/users/juliush-3433550/",
            "        Lien licence:https://pixabay.com/service/terms/https://pixabay.com/license-summary/",
            "   Musique de fin:",
            "        Lien:https:https://pixabay.com/fr/music/ambiant-bathroom-chill-background-music-14977/",
            "        Crédit:https://pixabay.com/fr/users/chillmore-25283030/",
            "        Lien licence:https://pixabay.com/service/terms/https://pixabay.com/license-summary/",
            "    Bruitage:",
            "        Lien licence:https://pixabay.com/service/terms/https://pixabay.com/license-summary/"
            "    Réveil:",
            "        Lien:https:https://lasonotheque.org/detail-2814-reveil-mecanique-sonnerie-11.html",
            "        Sons additionnels : Joseph SARDIN - LaSonotheque.org",
            "        Crédit:https://BigSoundBank.com",
            "        Lien licence:https://pixabay.com/service/terms/https://pixabay.com/license-summary/",
        ligneP4 = [
            "Équipe:",
            "    Conjard Maxime - Codeur, concepteur et musicien",
            "    Garnier Maël - Codeur, concepteur et chef de projet",
            "    Goumarre Yoann - Codeur, concepteur et narrateur",
            "    Despesse Chloé - Designer, secrétaire et codeur"
        ]

        lignes_to_display = lignesP1
        if page==2:
            lignes_to_display = lignesP2
        elif page==3:
            lignes_to_display=lignesP3
        elif page==4:
            lignes_to_display = ligneP4

        #arriere plan des scores
        credit_bg = pygame.image.load("./assets/img/list_simple.png")
        #redimmensionner le logo
        credit_bg_big = pygame.transform.scale(credit_bg, (credit_bg.get_width()*4, credit_bg.get_height()*4))
        credit_bg_rec = credit_bg_big.get_rect()
        credit_bg_rec.center = ((screen.get_width() // 2), (screen.get_width() // 2)-100)
        screen.blit(credit_bg_big, credit_bg_rec)

        for ligne in lignes_to_display:
            # Affichage du score
            uneLigne = font.render(ligne, True, (0, 0, 0))
            uneLigne_rec = uneLigne.get_rect()
            uneLigne_rec.bottomleft = (100, from_top)
            screen.blit(uneLigne, uneLigne_rec)

            from_top += font.get_height() +10     

        num_page = font.render(str(page) + "/4", True, (0, 0, 0))
        num_page_rec = num_page.get_rect()
        num_page_rec.bottomleft = (screen.get_width()-50, screen.get_height()-20)
        screen.blit(num_page, num_page_rec)

        from_top += font.get_height() +10      

        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtre
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour_button_rec.collidepoint(event.pos):
                    retour_button_path = "./assets/buttons/simple_press.png"

            
            if event.type == pygame.MOUSEBUTTONUP:
                if retour_button_rec.collidepoint(event.pos):
                    running=False
                    menu.ouvrir_menu(screen)
                
            if event.type == pygame.MOUSEMOTION:
                if retour_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    retour_button_path = "./assets/buttons/simple_over.png"
                else:
                    retour_button_path = "./assets/buttons/simple_normal.png"
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and page>1:
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    page = page-1
                if event.key == pygame.K_RIGHT and page<4:
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    page = page+1
                

        # Comme les dessins sont faits dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par seconde et retourne le temps réel passé
        clock.tick(60)
    # Termine proprement le module
    pygame.quit()

