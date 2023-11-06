import pygame

class Character:
    def __init__(self, x, y):
        # Charge l'image depuis le nouveau chemin
        self.image = pygame.image.load("./assets/img/character.png")
        # Redimensionne le personnage à 50x50 pixels
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_q]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_z]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)