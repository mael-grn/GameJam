import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, x, y, image1_path, image2_path):
        super().__init__()  # Appel au constructeur de la classe mère

        # Chargez les deux images de la pièce
        self.image1 = pygame.image.load(image1_path)
        self.image2 = pygame.image.load(image2_path)

        # Redimensionnez les images si nécessaire
        self.image1 = pygame.transform.scale(self.image1, (50, 50))
        self.image2 = pygame.transform.scale(self.image2, (50, 50))

        # Séquence d'images pour l'animation
        self.animation_frames = [self.image1, self.image2]

        # Obtenez le rectangle de l'image
        self.rect = self.image1.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Compteur pour l'animation
        self.frame_counter = 0

    def draw(self, screen):
        # Cette méthode dessine la pièce sur l'écran
        screen.blit(self.animation_frames[self.frame_counter], self.rect)

    def animate(self):
        # Cette méthode permet de passer à l'image suivante dans l'animation
        self.frame_counter = (self.frame_counter + 1) % len(self.animation_frames)