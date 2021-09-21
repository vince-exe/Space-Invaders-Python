import pygame


class Proiettile:
    def __init__(self, x, width, y, height, larghezza, altezza):
        self.rect = pygame.Rect(x + width // 2 - 2, y + height - 15, larghezza, altezza)
