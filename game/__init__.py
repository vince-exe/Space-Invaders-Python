import pygame

from font import Font

pygame.init()


class Game:
    def __init__(self):
        # GAME SETTINGS
        self.FPS = 60
        self.esci = False
        self.score = 0

        # EVENTI
        self.movimento_ondata = 2000
        self.spara_alieno = 1000
        self.lost = False

        # CLOCK_FPS
        self.clock = pygame.time.Clock()

    def set_fps(self, FPS):
        self.clock.tick(FPS)

    def draw_loser(self, font, window, LARGHEZZA, ALTEZZA, music):
        music.stop()

        font.set_text("Hai Perso", True, (255, 0, 0))

        font.draw(window, LARGHEZZA // 2 - 150, ALTEZZA // 2 - font.text.get_height())

        pygame.display.update()

        pygame.time.delay(3000)

        self.esci = True
