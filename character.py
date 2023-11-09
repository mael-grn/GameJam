import pygame
import projectile
import game_logic
import constants

# Un personnage dispose de codes couleurs par rapport à la carte : il ne peut pas passer sur la couleur noire,
# et la couleur bleu lui fait changer de salle

class Character:
    def __init__(self, x, y, pseudo):
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
        self.pseudo = pseudo
        self.images = [[pygame.transform.scale(img, (95, 95)) for img in direction] for direction in self.images]
        self.rect = self.images[0][0].get_rect()
        self.rect.width=95
        self.rect.height=120
        self.rect.center = [x, y]
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

        self.piece_image = pygame.image.load("./assets/img/piece.png")
        self.key_image = pygame.image.load("./assets/img/key.png")
        self.pieces = 3

        self.projectiles = []
        self.keys = 0 
        self.last_move = list((0, 0))

    def get_proj(self):
        return self.projectiles
    def add_proj(self, proj):
        game_logic.play_sound("blast")
        self.projectiles.append(proj)
    def del_proj(self,ind):
        del(self.projectiles[ind])

    def move_left(self):
        self.last_move[0] = -1
        self.last_move[1] = 0
        self.rect.x -= self.speed
        self.direction = 1  # Gauche
        current_time = pygame.time.get_ticks()
        if current_time - self.last_image_time > constants.ANIMATION_SPEED:  # Change d'image toutes les 0,5 secondes
            self.walk_step = 1 - self.walk_step
            self.last_image_time = current_time

    def move_right(self):
        self.last_move[0] = 1
        self.last_move[1] = 0
        self.rect.x += self.speed
        self.direction = 0  # Droite
        current_time = pygame.time.get_ticks()
        if current_time - self.last_image_time > constants.ANIMATION_SPEED:  # Change d'image toutes les 0,5 secondes
            self.walk_step = 1 - self.walk_step
            self.last_image_time = current_time

    def move_up(self):
        self.last_move[1] = -1
        self.last_move[0] = 0
        self.rect.y -= self.speed
        current_time = pygame.time.get_ticks()
        if current_time - self.last_image_time > constants.ANIMATION_SPEED:  # Change d'image toutes les 0,5 secondes
            self.walk_step = 1 - self.walk_step
            self.last_image_time = current_time

    def move_down(self):
        self.last_move[1] = 1
        self.last_move[0] = 0
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
        #afficher la hitbox:
        #pygame.draw.rect(screen, (255, 0, 0), self.rect)
        screen.blit(image, self.rect)

    def take_damage(self, damage):
        game_logic.play_sound("takeDamage")
        if not self.invincible:
            self.hp -= damage
            if self.hp <= 0:
                self.hp = 0  # L'ennemi a 0 points de vie
                self.eliminated = True  # Marquez l'ennemi comme éliminé
            self.invincible = constants.TEMP_INVINCIBILITE
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
        heart_spacing = 0 # Espace entre les cœurs
        heart_size = 60  # Taille des cœurs

        for i in range(self.get_hp()):
            x = i * (heart_size + heart_spacing) + 5  # Calcul de la position x en fonction de l'index
            y = 5  # Position y
            heart_image = pygame.transform.scale(self.heart_image, (heart_size, heart_size))
            screen.blit(heart_image, (x, y))

    def draw_keys(self, screen):
        key_spacing = 5
        key_size = 60
        x = screen.get_width() - key_size - key_spacing - 110
        y = 15  # Position y en haut à droite

        # Dessinez l'image de la pièce
        key_image = pygame.transform.scale(self.key_image, (self.key_image.get_width()//15, self.key_image.get_height()//15))
        screen.blit(key_image, (x, y))

        # Affichez le nombre de pièces du personnage à côté de l'image de la pièce
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.keys), True, (255, 255, 255))
        text_x = x - text.get_width() - key_spacing  # Position x pour le texte
        text_y = y + (key_size - text.get_height()) // 2 -15  # Centrer le texte verticalement
        screen.blit(text, (text_x, text_y))

    def draw_pieces(self, screen):
        piece_spacing = 5  # Espace entre l'image de la pièce et le nombre
        piece_size = 50  # Taille de l'image de la pièce
        x = screen.get_width() - piece_size - piece_spacing
        y = 5  # Position y en haut à droite

        # Dessinez l'image de la pièce
        piece_image = pygame.transform.scale(self.piece_image, (piece_size, piece_size))
        screen.blit(piece_image, (x, y))

        # Affichez le nombre de pièces du personnage à côté de l'image de la pièce
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.get_pieces()), True, (255, 255, 255))
        text_x = x - text.get_width() - piece_spacing  # Position x pour le texte
        text_y = y + (piece_size - text.get_height()) // 2  # Centrer le texte verticalement
        screen.blit(text, (text_x, text_y))
        

    def increase_pieces(self, amount):
        game_logic.play_sound("coin")
        game_logic.ajout_score(self.pseudo, 5)
        self.pieces += amount

    def get_pieces(self):
        return self.pieces
    
    def increase_keys(self):
        game_logic.play_sound("coin")
        game_logic.ajout_score(self.pseudo, 15)
        self.keys +=1

    def defeat_boss(self):
        game_logic.ajout_score(self.pseudo, 50)


    def echange_foodtruck(self,entier):
        if self.pieces >=3 and entier ==0:
            self.pieces = self.pieces-3
            self.hp=self.hp+1
        
            
        
            
            
            
        



