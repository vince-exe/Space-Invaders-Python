import pygame

pygame.font.init()


class Font:
    def __init__(self, nome, size, text, colore):
        self.font = pygame.font.SysFont(nome, size)
        self.text = self.font.render(text, True, colore)

    def draw(self, window, x, y):
        window.blit(self.text, (x, y))

    def set_text(self, text, bool, colore):
        self.text = self.font.render(text, bool, colore)
