import pygame
class Key:
    def __init__(self, x, y, picked=False):

        self.image = pygame.image.load("./assets/img/key.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//2, self.image.get_height()//2))
        self.rect = self.image.get_rect()
        self.rect.width=self.image.get_width()
        self.rect.height=self.image.get_height()
        self.rect.center = (x, y)
        self.picked = picked
        
    def draw(self, screen):
            screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect
    
