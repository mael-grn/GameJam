import pygame
class Key:
    def __init__(self, x, y, picked=False):

        self.image = pygame.image.load("./assets/img/key.png")
        self.small = pygame.transform.scale(self.image, (self.image.get_width()//10, self.image.get_height()//10))
        self.rect = self.small.get_rect()
        self.rect.width=self.small.get_width()
        self.rect.height=self.small.get_height()
        self.rect.center = (x, y)
        self.picked = picked
        
    def draw(self, screen):
            screen.blit(self.small, self.rect)

    def get_rect(self):
        return self.rect
    
