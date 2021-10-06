import random

from scudo_nemico import *
from shooter_nemico import *
from proiettile import *

pygame.init()


class Ondate:
    def __init__(self):
        self.nemico_scudo_list = []
        self.nemico_shooter_list = []

        x_scudo = 40
        y_scudo = 200

        for index in range(10):
            if index >= 1:  # dal primo in poi incremento la posizione
                x_scudo += 110
                scudo = NemicoScudo(x_scudo, y_scudo)

            else:  # se è il primo lo piazzi a x = 40 y = 100
                scudo = NemicoScudo(x_scudo, y_scudo)

            self.nemico_scudo_list.append(scudo)

        x_shooter = 45
        y_shooter = 100

        for index in range(10):
            if index >= 1:
                x_shooter += 110
                shooter = Shooter(x_shooter, y_shooter)
            else:
                shooter = Shooter(x_shooter, y_shooter)

            self.nemico_shooter_list.append(shooter)

    def update_ondata(self):
        for scudo_nemico in self.nemico_scudo_list:
            scudo_nemico.update_nemico()

    def shoot(self):
        if not len(self.nemico_shooter_list) <= 0:
            shooter = random.choice(self.nemico_shooter_list)

            bullet = Proiettile(shooter.rect.x, shooter.rect.width, shooter.rect.y, shooter.rect.height, 7, 15)

            shooter.shoot(bullet)

    def check_collision(self, player, ALTEZZA, game):
        for nemico_scudo in self.nemico_scudo_list:    # check collision SCUDO_NEMICO + player
            if nemico_scudo.rect.colliderect(player.rect):
                player.vita -= 25

                self.nemico_scudo_list.remove(nemico_scudo)

            if nemico_scudo.rect.y - nemico_scudo.rect.height >= ALTEZZA:  # check collision SCUDO_NEMICO + limite mappa
                self.nemico_scudo_list.remove(nemico_scudo)

                game.lost = True

        for shooter in self.nemico_shooter_list:
            shooter.check_collision_proiettile(player, ALTEZZA)

    def draw(self, window):
        for nemico_scudo in self.nemico_scudo_list:  # disegno il nemico scudo
            nemico_scudo.draw(window)
        
        for shooter in self.nemico_shooter_list:  # disegno il nemico shooter + proiettili
            shooter.draw_shooter(window)
            shooter.draw_bullet(window)
            shooter.update_proiettile()

    def spawn_orda(self, font_score, game):
        if len(self.nemico_scudo_list) <= 0:
            if len(self.nemico_shooter_list) <= 0:
                x_scudo = 40
                y_scudo = 200

                for index in range(10):
                    if index >= 1:  # dal primo in poi incremento la posizione
                        x_scudo += 110

                        scudo = NemicoScudo(x_scudo, y_scudo)

                    else:  # se è il primo lo piazzi a x = 40 y = 100
                        scudo = NemicoScudo(x_scudo, y_scudo)

                    self.nemico_scudo_list.append(scudo)

                x_shooter = 45
                y_shooter = 100

                for index in range(10):
                    if index >= 1:
                        x_shooter += 110

                        shooter = Shooter(x_shooter, y_shooter)
                    else:
                        shooter = Shooter(x_shooter, y_shooter)

                    self.nemico_shooter_list.append(shooter)

                game.livelli += 1
                font_score.set_text("Livelli: " + str(game.livelli), True, (219, 216, 13))
