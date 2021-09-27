import pygame

from font import Font

pygame.init()


class Game:
    def __init__(self):
        # GAME SETTINGS
        self.FPS = 60
        self.esci = False
        self.score = 0
        livello = 0

        # EVENTI
        self.movimento_ondata = 2000
        self.spara_alieno = 1000

        # CLOCK_FPS
        self.clock = pygame.time.Clock()

        # FONT
        self.font_score = Font("comicsans", 60, "Score ", (219, 216, 13))

    def set_fps(self, FPS):
        self.clock.tick(FPS)
