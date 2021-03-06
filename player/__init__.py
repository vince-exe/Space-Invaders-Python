import pygame
import os
from proiettile import Proiettile


class Player:
    def __init__(self, x, y, directory, nome_file, scalax, scalay):
        self.vita = 200

        self.image = pygame.image.load(os.path.join(directory, nome_file))
        self.image = pygame.transform.scale(self.image, (scalax, scalay))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.lista_proiettili = []

    def add_bullet(self):
        if len(self.lista_proiettili) < 2:
            bullet = Proiettile(self.rect.x, self.rect.width, self.rect.y, self.rect.height, 7, 15)
            bullet.shoot_sound()

            self.lista_proiettili.append(bullet)

    def move(self, LARGHEZZA):
        key_premuta = pygame.key.get_pressed()

        if key_premuta[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5

        if key_premuta[pygame.K_RIGHT] and self.rect.x < LARGHEZZA - self.rect.width:
            self.rect.x += 5

    def shoot(self, window):
        for bullett in self.lista_proiettili:
            bullett.rect.y -= 11

            pygame.draw.rect(window, color=(214, 209, 47), rect=bullett)

            if bullett.rect.y < 0:  # check collision con il bordo mappa
                self.lista_proiettili.remove(bullett)

    def check_collision(self, ondate, font, game):
        for bullet in self.lista_proiettili:
            for nemico_scudo in ondate.nemico_scudo_list:
                if bullet.rect.colliderect(nemico_scudo.rect):  # check collision con il nemico scudo
                    self.lista_proiettili.remove(bullet)

                    game.hit_sound.sound.play()

                    if nemico_scudo.check_morto(bullet):
                        ondate.nemico_scudo_list.remove(nemico_scudo)

                        game.score += 1
                        font.set_text("Score: " + str(game.score), True, (219, 216, 13))

            for shooter in ondate.nemico_shooter_list:
                if bullet.rect.colliderect(shooter.rect):
                    self.lista_proiettili.remove(bullet)

                    game.hit_sound.sound.play()

                    if shooter.check_morto(bullet):
                        ondate.nemico_shooter_list.remove(shooter)

                        game.score += 1
                        font.set_text("Score: " + str(game.score), True, (219, 216, 13))

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def draw_health(self, font_health, window, game):
        font_health.set_text("Health: " + str(self.vita), True, (219, 216, 13))

        font_health.draw(window, 30, 15)

        if self.vita <= 0:
            game.lost = True
