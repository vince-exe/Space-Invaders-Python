import random

from scudo_nemico import *
from shooter_nemico import *
from proiettile import *


class Ondate:
    def __init__(self):
        self.nemico_scudo_list = []
        self.nemico_shooter_list = []

        x_scudo = 40
        y_scudo = 100

        for index in range(10):
            if index >= 1:  # dal primo in poi incremento la posizione
                x_scudo += 110
                scudo = NemicoScudo(x_scudo, y_scudo)

            else:  # se è il primo lo piazzi a x = 40 y = 100
                scudo = NemicoScudo(x_scudo, y_scudo)

            self.nemico_scudo_list.append(scudo)

        x_shooter = 45
        y_shooter = 20

        for index in range(10):
            if index >= 1:
                x_shooter += 110
                shooter = Shooter(x_shooter, y_shooter)
            else:
                shooter = Shooter(x_shooter, y_shooter)

            self.nemico_shooter_list.append(shooter)

    def move_ondata_scudo(self):
        for index in self.nemico_scudo_list:
            index.rect.y += 32

    def shoot(self, window):
        if not len(self.nemico_shooter_list) <= 0:
            shooter = random.choice(self.nemico_shooter_list)

            bullet = Proiettile(shooter.rect.x, shooter.rect.width, shooter.rect.y, shooter.rect.height, 7, 15)

            shooter.shoot(window, bullet)

    def draw(self, window):
        for index in self.nemico_scudo_list:  # disegno il nemico scudo
            index.draw(window)

        for index in self.nemico_shooter_list:  # disegno il nemico shooter
            index.draw(window)

        for shooter in self.nemico_shooter_list:
            shooter.update_proiettile()
