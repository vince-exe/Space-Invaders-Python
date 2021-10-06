import pygame
import os

pygame.init()


class Music:
    def __init__(self, volume, loop):
        self.pause = False

        pygame.mixer.music.load(os.path.join('assets', 'background_music.mp3'))
        pygame.mixer.music.set_volume(volume)

        if loop:
            pygame.mixer.music.play(-1)

    def check_pause(self):
        if self.pause:  # riprendi la musica
            pygame.mixer.music.unpause()
            self.pause = False
        else:   # pause la musica
            pygame.mixer.music.pause()
            self.pause = True
