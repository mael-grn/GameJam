import pygame

def error(screen, error_name = "unknown error") : 
    screen.fill("black")
    # Charger la police de caractères
    police = pygame.font.Font(None, 30)
    # Créer le texte
    titre = police.render(error_name, True, (255, 255, 255))

    # Afficher le texte
    screen.blit(titre, (100, 100))