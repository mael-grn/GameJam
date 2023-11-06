import pygame
import pickle
import screens.error as error
import screens.niveau1 as n1

def ouvrir_menu(screen) : 
    running = True
    dt=0
    clock = pygame.time.Clock()


    while running :

        #arriere plan
        screen.fill("black")

        #chargement de la police
        chemin = "./assets/fonts/pinball.ttf"
        font = pygame.font.Font(chemin, 36)  # Vous pouvez ajuster la taille de la police

        #chargement du logo
        logo = pygame.image.load("./assets/img/game_logo.jpg")
        #redimmensionner le logo
        logo_small = pygame.transform.scale(logo, (logo.get_width()/2, logo.get_height()/2))
        screen.blit(logo_small, (screen.get_width() // 2 - logo_small.get_width()/2, screen.get_height() // 3 - logo_small.get_height()/2))

        #creation du bouton quitter
        quitter = font.render("QUITTER", True, (255, 0, 0))  # (255, 0, 0) représente la couleur rouge (RVB)
        quitter_rec = quitter.get_rect()
        quitter_rec.center = ((screen.get_width() // 3)*2, (screen.get_height() // 3)*2)
        screen.blit(quitter, quitter_rec)

        #creation du bouton jouer
        jouer = font.render("JOUER", True, (255, 0, 0))  # (255, 0, 0) représente la couleur rouge (RVB)
        jouer_rec = jouer.get_rect()
        jouer_rec.center = ((screen.get_width() // 3), (screen.get_height() // 3)*2)
        screen.blit(jouer, jouer_rec)

        #gestion des evenements
        for event in pygame.event.get():

            #en cas de cliques
            if event.type == pygame.MOUSEBUTTONDOWN:

                #si fermeture fenetre
                if event.type == pygame.QUIT:
                    running=False
                    pygame.quit()
                # Si clique sur bouton quitter
                if quitter_rec.collidepoint(event.pos):
                    running=False
                    pygame.quit()
                #si clique sur bouton jouer
                if jouer_rec.collidepoint(event.pos):
                    running=False
                    n1.ouvrir_niveau(screen)

        # Comme les dessions sont fait dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par secondes et retourne le temps réel passé
        dt = clock.tick(60) 
    
                
    