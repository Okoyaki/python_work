import sys
import pygame
from random import randint

from settings import Settings
from star import Star


class StarSet:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Star Set")

        self.stars = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавишы."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_fleet(self):
        """Создание флота вторжения."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца.
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (star_width)
        number_stars_x = available_space_x // (2 * star_width)

        """Определяет количество рядов, помещающихся на экране."""
        available_space_y = (self.settings.screen_height -
                             (star_height))
        number_rows = available_space_y // (2 * star_height)

        # Создание флота вторжения.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, alien_number, row_number):
        """Создание приешльца и размещение его в ряду."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + (star_width * 2 + randint(-10, 10)) * alien_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star_height * row_number
        self.stars.add(star)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = StarSet()
    ai.run_game()
