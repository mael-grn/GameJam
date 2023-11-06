import pygame
import character
import screens.error as error

def ouvrir_niveau(screen):

    # Définit l'horloge pour connaître le temps qui a passé
    clock = pygame.time.Clock()
    # Pour savoir quand la boucle du jeu se termine
    running = True
    # Le temps passé entre deux rafraîchissements de l'écran en millisecondes
    dt = 0

    # Crée un personnage
    character_obj = character.Character(640, 360)  # Position initiale du personnage

    # Boucle de l'animation
    while running:
        # Parcourt tous les événements pour les traiter
        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtre
            if event.type == pygame.QUIT:
                running = False
        # Efface l'écran précédent en remplissant l'écran 
        screen.fill((0, 0, 255))  # Remplace "blue" par (0, 0, 255) pour définir la couleur bleue

        # Affiche le personnage
        character_obj.move(pygame.key.get_pressed())
        character_obj.draw(screen)

        # Comme les dessins sont faits dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par seconde et retourne le temps réel passé
        dt = clock.tick(60) 

    # Termine proprement le module
    pygame.quit()

# Appel au programme principal
main()
