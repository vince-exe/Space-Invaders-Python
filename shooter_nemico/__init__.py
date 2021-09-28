from proiettile import Proiettile

import pygame
import os


class Shooter:
    def __init__(self, x, y):
        self.vita = 100
        self.image = pygame.image.load(os.path.join('assets', 'cecchinoBlu.png'))
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.lista_proiettili = []

    def shoot(self, window, bullet):
        self.lista_proiettili.append(bullet)

    def update_proiettile(self, ALTEZZA, player):
        for bullet in self.lista_proiettili:
            bullet.rect.y += 5

            if bullet.rect.y - bullet.rect.height > ALTEZZA:  # se superano lo schermo
                self.lista_proiettili.remove(bullet)

            if bullet.rect.colliderect(player.rect):  # se colpiscono il player
                self.lista_proiettili.remove(bullet)

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

        for bullet in self.lista_proiettili:
            bullet.draw(window)
