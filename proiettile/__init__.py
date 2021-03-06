import pygame
import os
pygame.mixer.init()


class Proiettile:
    def __init__(self, x, width, y, height, larghezza, altezza):
        self.danno = 50

        self.rect = pygame.Rect(x + width // 2 - 2, y + height - 15, larghezza, altezza)
        self.sound_shoot = pygame.mixer.Sound(os.path.join('assets', 'shoot.mp3'))
        self.sound_shoot.set_volume(0.1)

    def shoot_sound(self):
        self.sound_shoot.play()

    def draw(self, window):
        pygame.draw.rect(window, color=(214, 209, 47), rect=self.rect)
