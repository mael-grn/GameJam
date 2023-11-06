import pygame

class Projectile:
    def __init__(self, x, y, cote):
        # Charge l'image depuis le nouveau chemin
        cote =0
        self.images = []
        self.imageD = pygame.image.load("./assets/img/projectile.png")
        self.imageG = pygame.image.load("./assets/img/projectileG.png")
        self.imageH = pygame.image.load("./assets/img/projectileH.png")
        self.imageB = pygame.image.load("./assets/img/projectileB.png")

        # Redimensionne le projectile à 20x20 pixels
        self.imageD = pygame.transform.scale(self.imageD, (20, 20))
        self.imageG = pygame.transform.scale(self.imageG, (20, 20))
        self.imageG = pygame.transform.scale(self.imageH, (20, 20))
        self.imageG = pygame.transform.scale(self.imageB, (20, 20))
        #initialise la liste d'image
        self.images.append(self.imageD)
        self.images.append(self.imageG)
        self.images.append(self.imageH)
        self.images.append(self.imageB)

        self.speed = 10  # Vitesse du projectile
        self.image = self.images[cote]
        self.rect = self.images[cote].get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)