from scudo_nemico import *


class Ondate:
    def __init__(self):
        self.nemico_scudo_list = []

        x = 40
        for index in range(10):
            if index >= 1:  # dal primo in poi incrementi la posizione
                x += 110
                scudo = NemicoScudo(x, 100)

            else:  # se è il primo lo piazzi a x = 40 y = 100
                scudo = NemicoScudo(x, 100)

            self.nemico_scudo_list.append(scudo)

    def move(self):
        for index in self.nemico_scudo_list:
            index.move()

    def draw(self, window):
        for index in self.nemico_scudo_list:
            index.draw(window)
