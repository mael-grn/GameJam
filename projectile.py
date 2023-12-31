import pygame
import math
import constants

class Projectile:
    def __init__(self, x, y, target_x, target_y,path, character=False):
        # Charge l'image depuis le nouveau chemin
        self.image = pygame.image.load(path)

        # Redimensionne le projectile à 20x20 pixels
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        dx = target_x -x
        dy = target_y -y
        self.angle_rad = math.atan2(dy,dx)
        angle_deg = math.degrees(self.angle_rad)
        self.speed = constants.PROJ_SPEED  # Vitesse du projectile
        if character:
            self.speed = 5 #changer la vitesse seuelemtn pour les enemy
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        self.rect.x += self.speed * math.cos(self.angle_rad)        
        self.rect.y += self.speed * math.sin(self.angle_rad)  
    def get_x(self):
        return self.rect.x     
    def get_y(self):
        return self.rect.y 
