import pygame
import projectile
import game_logic
import constants

# Un personnage dispose de codes couleurs par rapport à la carte : il ne peut pas passer sur la couleur noire,
# et la couleur bleu lui fait changer de salle

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
        self.rect.width=50
        self.rect.height=70
        self.rect.center = (x, y)
        self.speed = constants.CHARACTER_SPEED
        self.direction = 0  # 0 pour droite, 1 pour gauche
        self.walk_step = 0  # 0 pour image 1, 1 pour image 2
        self.last_image_time = pygame.time.get_ticks()  # Temps de la dernière image
        self.hp = 3  # Initialisez les HP à leur valeur maximale
        self.hp_timer = 0
        self.heart_image = pygame.image.load("./assets/img/coeur.png")
        self.heart_width, self.heart_height = self.heart_image.get_width(), self.heart_image.get_height()
        #test
        self.invincible = False  # Variable pour gérer l'invincibilité
        self.invincible_start_time = 0  # Temps où l'invincibilité a commencé

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

    def get_rect(self):  # left high
        return self.rect

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

    def take_damage(self, damage):
        if not self.invincible:
            self.hp -= damage
            if self.hp <= 0:
                self.hp = 0  # L'ennemi a 0 points de vie
                self.eliminated = True  # Marquez l'ennemi comme éliminé
            self.invincible = True
            self.invincible_start_time = pygame.time.get_ticks()  # Enregistrez le moment où l'invincibilité a commencé
        

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp  # Assurez-vous que les HP ne dépassent pas la valeur maximale

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def is_alive(self):
        return self.hp > 0

    def update(self):
        # Vérifiez si le personnage est invincible et si la durée d'invincibilité a dépassé 1 seconde
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.invincible_start_time >= 1000:  # 1000 ms = 1 seconde
                self.invincible = False

    def draw_hearts(self, screen):
        heart_spacing = 5  # Espace entre les cœurs
        heart_size = 60  # Taille des cœurs

        for i in range(self.get_hp()):
            x = i * (heart_size + heart_spacing) + 5  # Calcul de la position x en fonction de l'index
            y = 5  # Position y
            heart_image = pygame.transform.scale(self.heart_image, (heart_size, heart_size))
            screen.blit(heart_image, (x, y))

