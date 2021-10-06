from proiettile import Proiettile

import pygame
import os


class Shooter:
    def __init__(self, x, y):
        self.vita = 100
        self.morto = False
        self.bullet_damage = 50

        self.image = pygame.image.load(os.path.join('assets', 'cecchinoBlu.png'))
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.lista_proiettili = []

    def shoot(self, bullet):
        self.lista_proiettili.append(bullet)

    def update_proiettile(self):
        for bullet in self.lista_proiettili:
            bullet.rect.y += 5

    def check_collision_proiettile(self, player, ALTEZZA):
        for bullet in self.lista_proiettili:
            if bullet.rect.colliderect(player.rect):  # se colpiscono il player
                player.vita -= self.bullet_damage

                self.lista_proiettili.remove(bullet)

            if bullet.rect.y - bullet.rect.height > ALTEZZA:  # se superano lo schermo
                self.lista_proiettili.remove(bullet)

    def check_morto(self, bullet):
        if self.vita == 100:
            self.vita -= bullet.danno

        elif self.vita == 50:
            self.vita -= bullet.danno
            self.morto = True

            return self.morto

    def check_collision_shooter(self, player):
        if self.rect.colliderect(player.rect):
            return True

    def draw_bullet(self, window):
        for bullet in self.lista_proiettili:
            bullet.draw(window)

    def draw_shooter(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
