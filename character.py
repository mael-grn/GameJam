import pygame

class Character:
    def __init__(self, x, y, cote):
        # Charge l'image depuis le nouveau chemin
        self.images = []
        self.imageD = pygame.image.load("./assets/img/character.png")
        self.imageG = pygame.image.load("./assets/img/characterG.png")
        # Redimensionne le personnage à 50x50 pixels
        self.imageD = pygame.transform.scale(self.imageD, (125, 125))
        self.imageG = pygame.transform.scale(self.imageG, (125, 125))
        self.images.append(self.imageD)
        self.images.append(self.imageG)
        self.image = self.images[cote]
        self.rect = self.images[cote].get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_q]:
            self.rect.x -= self.speed
            self.cote = 1
            self.image = self.images[self.cote]

        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.cote =0
            self.image = self.images[self.cote]

        if keys[pygame.K_z]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)