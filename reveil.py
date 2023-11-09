import pygame

class Reveil:
    def __init__(self, x, y, image1_path):
        self.image = pygame.image.load(image1_path)
        self.rect = self.image.get_rect()
        self.rect.width=self.image.get_width()
        self.rect.height=self.image.get_height()
        self.rect.center = (x, y)        
    def draw(self, screen):
            screen.blit(self.image, self.rect)
    def set_img(self,image_path):
        self.image = pygame.image.load(image_path)
    def get_rect(self):
        return self.rect

    def check_collision(self, character_rect):
        return self.rect.colliderect(character_rect)