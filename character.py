import pygame
import projectile
import game_logic
import constants

#un personnage dispose de codes couleurs par rapport à la carte : il ne peut pas passer sur la couleur noire,
#et la couleur bleu lui fait changer de salle

class Character:
    def __init__(self, x, y):
        # Charge les images depuis les nouveaux chemins
        self.images = [
            [
                pygame.image.load("./assets/img/bonhomme1.png"),
                pygame.image.load("./assets/img/bonhomme2.png")
            ],
            [
                pygame.image.load("./assets/img/bonhomme1retourne.png"),
                pygame.image.load("./assets/img/bonhomme2retourne.png")
            ]
        ]

        # Redimensionne les images à 50x50 pixels
        self.images = [[pygame.transform.scale(img, (95, 95)) for img in direction] for direction in self.images]
        self.rect = self.images[0][0].get_rect()
        self.rect.topleft = (x, y)
        self.speed = constants.CHARACTER_SPEED
        self.direction = 0  # 0 pour droite, 1 pour gauche
        self.walk_step = 0  # 0 pour image 1, 1 pour image 2
        self.last_image_time = pygame.time.get_ticks()  # Temps de la dernière image
    
    def move_left(self):
        self.rect.x -= self.speed
        self.direction = 1  # Gauche
        current_time = pygame.time.get_ticks()
        if current_time - self.last_image_time > constants.ANIMATION_SPEED:  # Change d'image toutes les 0,5 secondes
            self.walk_step = 1 - self.walk_step
            self.last_image_time = current_time
    
    def move_right(self):
        self.rect.x += self.speed
        self.direction = 0  # Droite
        current_time = pygame.time.get_ticks()
        if current_time - self.last_image_time > constants.ANIMATION_SPEED:  # Change d'image toutes les 0,5 secondes
            self.walk_step = 1 - self.walk_step
            self.last_image_time = current_time

    def move_up(self):
        self.rect.y -= self.speed
        current_time = pygame.time.get_ticks()
        if current_time - self.last_image_time > constants.ANIMATION_SPEED:  # Change d'image toutes les 0,5 secondes
            self.walk_step = 1 - self.walk_step
            self.last_image_time = current_time

    def move_down(self):
        self.rect.y += self.speed  
        current_time = pygame.time.get_ticks()
        if current_time - self.last_image_time > constants.ANIMATION_SPEED:  # Change d'image toutes les 0,5 secondes
            self.walk_step = 1 - self.walk_step
            self.last_image_time = current_time

    def get_x(self):
        return self.rect.x
    
    def get_y(self):
        return self.rect.y

    def get_centre_x(self):
        return self.rect.centerx
    def get_centre_y(self):
        return self.rect.centery

    def draw(self, screen):
        # Récupère l'image en fonction de la direction et de l'étape de marche
        image = self.images[self.direction][self.walk_step]
        screen.blit(image, self.rect)