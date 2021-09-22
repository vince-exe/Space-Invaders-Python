import pygame
import os


class Music:
    def __init__(self):
        pygame.mixer.music.load(os.path.join('assets', 'background_music.mp3'))

    @staticmethod
    def play():
        pygame.mixer.music.play(-1)  # loop

    @staticmethod
    def stop():
        pygame.mixer.music.stop()
