from scudo_nemico import *


class Ondate:
    def __init__(self):
        self.nemico_scudo_list = []

        contatore = 40

        for index in range(11):
            if index > 1:
                contatore += 110

                scudo = NemicoScudo(contatore, 100)
            else:
                scudo = NemicoScudo(contatore, 100)

            self.nemico_scudo_list.append(scudo)

    def draw(self, window):
        for index in range(len(self.nemico_scudo_list)):
            self.nemico_scudo_list[index].draw(window)
