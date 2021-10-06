import pygame

from font import Font
from sound import Sound
from music import Music

pygame.init()


class Game:
    # Game Settings
    FPS = 60
    esci = False
    score = 0
    livelli = 0

    # Events
    movimento_ondata = 2000
    spara_alieno = 1000
    lost = False

    # Clock Fps
    clock = pygame.time.Clock()

    # Fonts
    font_score = Font("comicsans", 60, "Score: ", (219, 216, 13))
    font_health = Font("comicsans", 60, "Health: ", (219, 216, 13))
    font_lose = Font("comicsans", 90, "You lost", (219, 216, 13))
    font_livelli = Font("comicsans", 60, "Levels: ", (219, 216, 13))

    # Sound / Music
    hit_sound = Sound('assets', 'hit_sound.mp3', 0.1)

    music = Music(0.7, True)

    def set_fps(self, FPS):
        self.clock.tick(FPS)

    def draw_loser(self, font, window, LARGHEZZA, ALTEZZA):
        pygame.mixer.music.stop()

        font.set_text("Hai Perso", True, (255, 0, 0))

        font.draw(window, LARGHEZZA // 2 - 150, ALTEZZA // 2 - font.text.get_height())

        pygame.display.update()

        pygame.time.delay(3000)

        self.esci = True

    @classmethod
    def config_difficulty(cls, ondate):
        if Game.livelli >= 4:
            for scudo_nemico in ondate.nemico_scudo_list:
                scudo_nemico.movimento = 40

        if Game.livelli >= 10:
            for scudo_nemico in ondate.nemico_scudo_list:
                scudo_nemico.movimento = 55

        if Game.livelli >= 15:
            for scudo_nemico in ondate.nemico_scudo_list:
                scudo_nemico.movimento = 60

            for shooter in ondate.nemico_shooter_list:
                shooter.bullet_damage = 100

    def draw(self, window, ondate, player):
        self.font_score.draw(window, 960, 15)
        self.font_livelli.draw(window, 965, 790)

        ondate.draw(window)
        player.draw(window)

    @staticmethod
    def run(window, LARGHEZZA, player, ondate):
        player.move(LARGHEZZA)
        player.shoot(window)

        Game.config_difficulty(ondate)
