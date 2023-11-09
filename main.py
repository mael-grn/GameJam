import pygame
import screens.error as error
import screens.main_menu as menu
import constants
import game_logic
import sys

def main(difficulty):
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

    game_logic.set_difficulty(difficulty)

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

difficulty = "normal"

if "demo" in sys.argv:
    difficulty = "demo"
elif "easy" in sys.argv:
    difficulty = "easy"
elif "hard" in sys.argv:
    difficulty = "hard"

# Appel au programme principal
main(difficulty)
