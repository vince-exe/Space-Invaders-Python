import pygame
import os


class NemicoScudo:
    def __init__(self, x, y):
        self.vita = 100
        self.scudo = 100
        self.image = pygame.image.load(os.path.join('assets', 'scudo.png'))
        self.image = pygame.transform.scale(self.image, (100, 80))
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.movimento = 32

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update_nemico(self):
        self.rect.y += self.movimento
