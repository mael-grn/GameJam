import pygame
import time
class Enemy:
    def __init__(self, name, x, y, size, hp, image_path, attaque):
        self.attaque = attaque
        self.name = name
        self.x = x
        self.y = y
        self.size = size
        self.hp = hp
        self.image = pygame.image.load(image_path)  # Chargez l'image de l'ennemi depuis le chemin fourni
        self.image = pygame.transform.scale(self.image, (size, size))  # Redimensionnez l'image à la taille souhaitée
        self.rect = self.image.get_rect()
        self.projectlies = []
        # Ajustez la taille du rectangle de collision (hitbox) ici
        hitbox_width = size - 30  # Réduisez la largeur du rectangle de collision de 10 pixels
        hitbox_height = size - 30  # Réduisez la hauteur du rectangle de collision de 10 pixels

        # Ajustez l'emplacement du rectangle de collision pour le centrer sur l'image
        self.rect.width = hitbox_width
        self.rect.height = hitbox_height
        self.rect.topleft = (x + 5, y + 5)  # Ajoutez 5 pixels à la position pour centrer le rectangle

        self.speed = 5  # Vitesse de déplacement de l'ennemi
        self.eliminated = False  # Par défaut, l'ennemi n'est pas éliminé
        self.last_deplacement =0

        self.last_shot_time = 0 
    def set_img(self,image_path):
        self.image = pygame.image.load(image_path)  # Chargez l'image de l'ennemi depuis le chemin fourni
    def get_proj(self):
        return self.projectlies
    def add_proj(self, proj):
        self.projectlies.append(proj)
        self.last_shot_time = time.time()


    def del_proj(self,ind):
        del(self.projectlies[ind])
    def move_left(self):
        self.rect.x -= self.speed
        self.last_deplacement = time.time()
    def move_right(self):
        self.rect.x += self.speed
        self.last_deplacement = time.time()
    def move_up(self):
        self.rect.y -= self.speed
        self.last_deplacement = time.time()
    def move_down(self):
        self.rect.y += self.speed
        self.last_deplacement = time.time()
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0  # L'ennemi a 0 points de vie
            self.eliminated = True  # Marquez l'ennemi comme éliminé

    def is_alive(self):
        return self.hp > 0
    def get_centre_x(self):
        return self.rect.centerx
    def get_centre_y(self):
        return self.rect.centery
    def draw(self, screen):
        if not self.eliminated:  # Dessinez l'ennemi uniquement s'il n'est pas éliminé
            screen.blit(self.image, self.rect)
