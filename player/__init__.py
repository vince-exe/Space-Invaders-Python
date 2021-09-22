import pygame
import os
from proiettile import Proiettile


class Player:
    def __init__(self, vita, x, y, directory, nome_file, scalax, scalay):
        self.vita = vita
        self.image = pygame.image.load(os.path.join(directory, nome_file))
        self.image = pygame.transform.scale(self.image, (scalax, scalay))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.lista_proiettili = []

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def add_bullet(self):
        if len(self.lista_proiettili) < 2:
            bullet = Proiettile(self.rect.x, self.rect.width, self.rect.y, self.rect.height, 7, 15)
            bullet.shoot_sound()

            self.lista_proiettili.append(bullet)

    def move(self, LARGHEZZA):
        key_premuta = pygame.key.get_pressed()

        if key_premuta[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 5

        if key_premuta[pygame.K_d] and self.rect.x < LARGHEZZA - self.rect.width:
            self.rect.x += 5

    def shoot(self, window):
        for bullett in self.lista_proiettili:
            bullett.rect.y -= 11
            pygame.draw.rect(window, color=(214, 209, 47), rect=bullett)

            if bullett.rect.y < 0:
                self.lista_proiettili.remove(bullett)
                print("distrutto")

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
