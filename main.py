import pygame
import screens.error as error
import screens.main_menu as menu
import constants

def main():
    # Démmarre le module 
    pygame.init()
    # définit l'écran et sa taille
    screen = pygame.display.set_mode(constants.TAILLE_ECRAN)
    # Définit l'horloge pour connaitre le temps qui a passé
    clock = pygame.time.Clock()
    # Pour savoir quand la boucle du jeu se termine
    running = True
    # Le temps passé entre deux rafraichissement de l'écran en millisecondes
    dt = 0

    # Boucle de l'animation
    while running:
        # Parcourt tous les evenements pour les traiter
        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtre
            if event.type == pygame.QUIT:
                running = False
        # Efface l'écran précédent en remplissant l'écran 
        screen.fill("blue")
        
        menu.ouvrir_menu(screen)
        running=False
        # Comme les dessions sont fait dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par secondes et retourne le temps réel passé
        dt = clock.tick(60) 
    # Termine proprement le module
    pygame.quit()

# Appel au programme principal
main()
