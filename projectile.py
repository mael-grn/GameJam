import pygame
import math
class Projectile:
    def __init__(self, x, y, target_x, target_y):
        # Charge l'image depuis le nouveau chemin
        self.images = []
        self.imageD = pygame.image.load("./assets/img/projectile.png")
        self.imageG = pygame.image.load("./assets/img/projectileG.png")
        self.imageH = pygame.image.load("./assets/img/projectileH.png")
        self.imageB = pygame.image.load("./assets/img/projectileB.png")

        # Redimensionne le projectile à 20x20 pixels
        self.imageD = pygame.transform.scale(self.imageD, (50, 50))
        self.imageG = pygame.transform.scale(self.imageG, (50, 50))
        self.imageH = pygame.transform.scale(self.imageH, (50, 50))
        self.imageB = pygame.transform.scale(self.imageB, (50, 50))
        #initialise la liste d'image
        self.images.append(self.imageD)
        self.images.append(self.imageG)
        self.images.append(self.imageH)
        self.images.append(self.imageB)

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        dx = target_x -x
        dy = target_y -y
        self.angle_rad = math.atan2(dy,dx)
        angle_deg = math.degrees(self.angle_rad)
        self.speed = 5  # Vitesse du projectile
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        self.rect.x += self.speed * math.cos(self.angle_rad)        
        self.rect.y += self.speed * math.sin(self.angle_rad)        
