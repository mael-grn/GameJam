import pygame

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
        self.images = [[pygame.transform.scale(img, (125, 125)) for img in direction] for direction in self.images]
        self.rect = self.images[0][0].get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5
        self.direction = 0  # 0 pour droite, 1 pour gauche
        self.walk_step = 0  # 0 pour image 1, 1 pour image 2
        self.last_image_time = pygame.time.get_ticks()  # Temps de la dernière image

    def move(self, keys):
        if keys[pygame.K_q]:
            self.rect.x -= self.speed
            self.direction = 1  # Gauche
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = 0  # Droite

        if keys[pygame.K_z]:
            self.rect.y -= self.speed
            
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
            

        # Vérifie s'il y a un déplacement vertical
        is_vertical_movement = keys[pygame.K_z] or keys[pygame.K_s]
        # Vérifie s'il y a un déplacement horizontal
        is_horizontal_movement = keys[pygame.K_q] or keys[pygame.K_d]

        # Si le personnage se déplace verticalement, alternez entre les images bonhomme1 et bonhomme2
        if is_vertical_movement:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_image_time > 500:  # Change d'image toutes les 0,5 secondes
                self.walk_step = 1 - self.walk_step
                self.last_image_time = current_time

        # Si le personnage se déplace horizontalement, alternez entre les images bonhomme1retourne et bonhomme2retourne
        if is_horizontal_movement:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_image_time > 500:  # Change d'image toutes les 0,5 secondes
                self.walk_step = 1 - self.walk_step
                self.last_image_time = current_time

    def draw(self, screen):
        # Récupère l'image en fonction de la direction et de l'étape de marche
        image = self.images[self.direction][self.walk_step]
        screen.blit(image, self.rect)