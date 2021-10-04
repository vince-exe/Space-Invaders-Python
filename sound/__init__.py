import pygame
import os


class Sound:
    def __init__(self, directory, nome_file, volume):
        self.sound = pygame.mixer.Sound(os.path.join(directory, nome_file))
        self.sound.set_volume(volume)