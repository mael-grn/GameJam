import pygame

def show_error(screen, error_name = "unknown error") : 
    screen.fill("black")
    font = pygame.font.Font(None, 36)  # Vous pouvez ajuster la taille de la police

    # Crée une surface de texte rouge avec le mot "error"
    text_surface = font.render(error_name, True, (255, 0, 0))  # (255, 0, 0) représente la couleur rouge (RVB)

    # Obtient les dimensions de la surface de texte
    text_rect = text_surface.get_rect()

    # Centre la surface de texte sur l'écran
    text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

    # Dessine la surface de texte sur l'écran
    screen.blit(text_surface, text_rect)